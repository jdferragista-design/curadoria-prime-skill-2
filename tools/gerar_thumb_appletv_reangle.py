#!/usr/bin/env python3
# Thumb+hero do re-angle Apple TV 4K (25/09/2026).
# Fonte do produto: WP media 4533 (apple-tv-4k-hero-oficial.jpg) salva local como
# ./appletv-hero-oficial.jpg — fundo branco, Apple TV + Siri Remote, validada por visao.
# Output: thumb-apple-tv-reangle.jpg (destaque 5132) / hero-apple-tv-reangle.jpg (hero 5133).
src = open("/home/ubuntu/curadoria-prime-skill-2/tools/gerar_thumb_hero.py", encoding="utf-8").read()
lib = src[:src.find("# ---- produtos ----")]
exec(compile(lib, "golden_lib", "exec"), globals())

prod = cutout_white("./appletv-hero-oficial.jpg", thresh=42, erode=3)
bbox = prod.getbbox()
prod = prod.crop(bbox)
print("crop:", prod.size)

build(W_PX, H_PX, prod, "APPLE TV 4K", "AGORA OU ESPERAR?", "REVIEW ATUALIZADO — SETEMBRO 2026",
      prod_h_ratio=0.50, base_ratio=0.84).save("./thumb-apple-tv-reangle.jpg", quality=90)
print("thumb v4 ok")

build(970, 546, prod, "", "", "", with_text=False, prod_h_ratio=0.64).save("./hero-apple-tv-reangle.jpg", quality=90)
print("hero v4 ok")
