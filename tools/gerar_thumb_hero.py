#!/usr/bin/env python3
# Gera thumbnail (1280x720) + hero (970x546) no estilo golden da Curadoria Prime
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

W_PX = 1280; H_PX = 720
random.seed(42)

def lerp(a, b, t): return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def bg_gradient(w, h):
    img = Image.new("RGB", (w, h))
    px = img.load()
    navy = (13, 16, 48)      # base: azul-marinho profundo
    mid  = (28, 22, 84)
    purple = (74, 32, 130)   # topo: roxo
    for y in range(h):
        t = y / (h - 1)
        c = lerp(purple, mid, t / 0.55) if t < 0.55 else lerp(mid, navy, (t - 0.55) / 0.45)
        for x in range(w):
            px[x, y] = c
    return img

def add_rays(img, cx, cy, n=14, color=(255, 0, 170), max_len=1.4):
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    W, H = img.size
    for i in range(n):
        ang = math.radians(-180 + 360 * i / n + random.uniform(-6, 6))
        spread = math.radians(random.uniform(3.5, 7))
        L = max_len * W * random.uniform(0.55, 1.0)
        pts = [(cx, cy),
               (cx + L * math.cos(ang - spread), cy + L * math.sin(ang - spread)),
               (cx + L * math.cos(ang + spread), cy + L * math.sin(ang + spread))]
        d.polygon(pts, fill=color + (random.randint(14, 30),))
    img_rgba = img.convert("RGBA")
    out = Image.alpha_composite(img_rgba, overlay)
    return out

def add_particles(img, n=90):
    d = ImageDraw.Draw(img)
    W, H = img.size
    for _ in range(n):
        x, y = random.randint(0, W - 1), random.randint(0, int(H * 0.75))
        r = random.choice([1, 1, 2, 2, 3])
        a = random.randint(60, 160)
        col = random.choice([(255, 255, 255, a), (180, 200, 255, a), (255, 140, 220, a)])
        d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    return img

def add_spotlight(img, cx, cy, radius, color=(120, 90, 255)):
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(glow)
    for r in range(radius, 0, -6):
        a = int(38 * (1 - r / radius))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (a,))
    return Image.alpha_composite(img, glow)

def cutout_white(path, thresh=42, erode=3):
    """Remove fundo branco por floodfill a partir das bordas (preserva branco interno)."""
    im = Image.open(path).convert("RGB")
    sentinel = (255, 0, 255)
    w, h = im.size
    from PIL import ImageDraw as ID
    for corner in [(0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (0, h // 2), (w - 1, h // 2), (w // 2, h - 1)]:
        try:
            ID.floodfill(im, corner, sentinel, thresh=thresh)
        except Exception:
            pass
    rgba = im.convert("RGBA")
    px = rgba.load()
    for y in range(h):
        for x in range(w):
            if px[x, y][:3] == sentinel:
                px[x, y] = (0, 0, 0, 0)
    # erode alpha para eliminar halo branco residual + suavizar borda
    from PIL import ImageFilter as IF
    a = rgba.split()[3].filter(IF.MinFilter(erode))
    a = a.filter(IF.GaussianBlur(0.8))
    rgba.putalpha(a)
    # defringe: pixels quase-brancos encostados em transparencia viram transparentes
    px2 = rgba.load()
    aw, ah = rgba.size
    kill = []
    for yy in range(ah):
        for xx in range(aw):
            r, g, b, aa = px2[xx, yy]
            if aa > 0 and r > 235 and g > 235 and b > 230:
                near_transp = False
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    if 0 <= xx+dx < aw and 0 <= yy+dy < ah and px2[xx+dx, yy+dy][3] == 0:
                        near_transp = True
                        break
                if near_transp:
                    kill.append((xx, yy))
    for xx, yy in kill:
        px2[xx, yy] = (0, 0, 0, 0)
    return rgba

def place_product(canvas, prod, cx, base_y, target_h, reflect=True):
    prod = prod.resize((int(prod.width * target_h / prod.height), target_h), Image.LANCZOS)
    # sombra de contato suave (oval borrada, integrada ao chao)
    sh_layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh_layer)
    sw = int(prod.width * 0.52)
    sd.ellipse([cx - sw, base_y - 4, cx + sw, base_y + 16], fill=(0, 0, 0, 70))
    sh_layer = sh_layer.filter(ImageFilter.GaussianBlur(9))
    canvas.alpha_composite(sh_layer)
    d = ImageDraw.Draw(canvas)
    px = cx - prod.width // 2
    py = base_y - prod.height
    canvas.alpha_composite(prod, (px, py))
    if reflect:
        mir = prod.transpose(Image.FLIP_TOP_BOTTOM)
        mask = Image.new("L", mir.size, 0)
        md = ImageDraw.Draw(mask)
        fade_h = mir.height
        for y in range(fade_h):
            md.line([(0, y), (mir.width, y)], fill=int(70 * (1 - y / fade_h)))
        mir.putalpha(mask)
        canvas.alpha_composite(mir, (px, base_y + 6))

def gradient_text(img, text, font, cx, top_y, c1, c2, outline=(10, 10, 25), stroke=8, shadow=(0, 0, 0, 200), shadow_off=10):
    d = ImageDraw.Draw(img)
    bbox = d.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = cx - tw // 2 - bbox[0]
    y = top_y - bbox[1]
    # sombra dura 3D (extrudada)
    for off in range(shadow_off, 4, -2):
        d.text((x + off, y + off), text, font=font, fill=shadow, stroke_width=stroke, stroke_fill=shadow)
    d.text((x, y), text, font=font, fill=outline, stroke_width=stroke, stroke_fill=outline)
    # gradiente vertical aplicado ao texto
    grad = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(grad)
    gd.text((x, y), text, font=font, fill=(255, 255, 255, 255), stroke_width=stroke, stroke_fill=(255, 255, 255, 255))
    strip = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(strip)
    for yy in range(y, y + th):
        t = (yy - y) / max(th - 1, 1)
        sd.line([(0, yy), (img.width, yy)], fill=lerp(c1, c2, t) + (255,))
    mask = grad.split()[3]
    out = Image.composite(strip, img, mask)
    img.paste(out)
    return y + th

def flat_text(img, text, font, cx, top_y, fill=(255, 255, 255, 255), stroke=0, stroke_fill=(0, 0, 0, 160), shadow_off=4):
    d = ImageDraw.Draw(img)
    bbox = d.textbbox((0, 0), text, font=font, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    x = cx - tw // 2 - bbox[0]
    y = top_y - bbox[1]
    d.text((x + shadow_off, y + shadow_off), text, font=font, fill=(0, 0, 0, 150), stroke_width=stroke, stroke_fill=(0, 0, 0, 150))
    d.text((x, y), text, font=font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return y + (bbox[3] - bbox[1])

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def build(w, h, product, title1, title2, support, with_text=True, prod_h_ratio=0.52, base_ratio=0.80):
    img = bg_gradient(w, h).convert("RGBA")
    cx, cy = w // 2, int(h * 0.62)
    img = add_rays(img, cx, int(h * 0.45), n=16)
    img = add_spotlight(img, cx, int(h * 0.55), int(w * 0.34))
    # piso refletivo: linha do horizonte
    floor = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fd = ImageDraw.Draw(floor)
    horizon = int(h * 0.78)
    for y in range(horizon, h):
        t = (y - horizon) / (h - horizon)
        fd.line([(0, y), (w, y)], fill=(int(18 + 26 * t), int(14 + 18 * t), int(52 + 40 * t), 255))
    img = Image.alpha_composite(Image.new("RGBA", (w, h), (0, 0, 0, 0)), img)
    base = bg_gradient(w, h).convert("RGBA")
    base = add_rays(base, cx, int(h * 0.45), n=16)
    base = add_spotlight(base, cx, int(h * 0.55), int(w * 0.34))
    fd2 = ImageDraw.Draw(base)
    for y in range(horizon, h):
        t = (y - horizon) / (h - horizon)
        fd2.line([(0, y), (w, y)], fill=(int(16 + 22 * t), int(12 + 16 * t), int(46 + 34 * t)))
    base = add_particles(base.convert("RGBA"))
    place_product(base, product, cx, int(h * base_ratio), int(h * prod_h_ratio))
    if with_text:
        f1 = ImageFont.truetype(FONT_BOLD, int(w * 0.075))
        f2 = ImageFont.truetype(FONT_BOLD, int(w * 0.052))
        f3 = ImageFont.truetype(FONT_BOLD, int(w * 0.026))
        y_end = gradient_text(base, title1, f1, cx, int(h * 0.05), (255, 138, 0), (255, 235, 59))
        y_end = gradient_text(base, title2, f2, cx, y_end + int(h * 0.03), (0, 229, 255), (68, 138, 255), stroke=5)
        flat_text(base, support, f3, cx, y_end + int(h * 0.035), fill=(255, 255, 255, 255))
    return base.convert("RGB")

# ---- produtos ----
swl = cutout_white("./switch-produto.webp")
mk8 = cutout_white("./mk8-box.webp")

# thumbnails 1280x720
build(W_PX, H_PX, swl, "SWITCH LITE", "VALE A PENA?", "REVIEW COMPLETO 2026", prod_h_ratio=0.46, base_ratio=0.86).save("./thumb-switch-lite.jpg", quality=90)
build(W_PX, H_PX, mk8, "MARIO KART 8", "VALE A PENA?", "REVIEW COMPLETO 2026", prod_h_ratio=0.44, base_ratio=0.86).save("./thumb-mario-kart.jpg", quality=90)
# heroes 970x546 (mesma linguagem, sem texto de impacto)
build(970, 546, swl, "", "", "", with_text=False, prod_h_ratio=0.58).save("./hero-switch-lite.jpg", quality=90)
build(970, 546, mk8, "", "", "", with_text=False, prod_h_ratio=0.62).save("./hero-mario-kart.jpg", quality=90)

# ---------- SUPER MARIO BROS. WONDER ----------
wonder = cutout_white("./wonder-box.webp", thresh=60, erode=5)
build(W_PX, H_PX, wonder, "SUPER MARIO BROS.", "WONDER — VALE A PENA?", "REVIEW COMPLETO 2026",
      prod_h_ratio=0.44, base_ratio=0.86).save("./thumb-super-mario-bros-wonder.jpg", quality=90)
build(970, 546, wonder, "", "", "", with_text=False, prod_h_ratio=0.62).save("./hero-super-mario-bros-wonder.jpg", quality=90)
print("wonder geradas")

print("geradas imagens")