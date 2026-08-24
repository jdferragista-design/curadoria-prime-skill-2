#!/usr/bin/env python3
"""Patch 24/08/2026 — parte B1: h2s das seções e cards de produto."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    ("<h2 id=\"mouse\" class=\"wp-block-heading\">🖱️ 1. Mouse sem fio Logitech M185 — R$ 67,19</h2>",
     "<h2 id=\"mouse\" class=\"wp-block-heading\">🖱️ 1. Mouse sem fio Logitech M185 — R$ 68,90</h2>"),
    ("<h2 id=\"teclado\" class=\"wp-block-heading\">⌨️ 2. Teclado Logitech Pebble Keys 2 K380 — R$ 192,05</h2>",
     "<h2 id=\"teclado\" class=\"wp-block-heading\">⌨️ 2. Teclado Logitech Pebble Keys 2 K380s — R$ 197,99</h2>"),
    ("O <strong>Pebble Keys 2 K380</strong> é o teclado compacto",
     "O <strong>Pebble Keys 2 K380s</strong> é o teclado compacto"),
    ("<h2 id=\"fone\" class=\"wp-block-heading\">🎧 3. Fone JBL Wave Buds 2 — R$ 235,00</h2>",
     "<h2 id=\"fone\" class=\"wp-block-heading\">🎧 3. Fone JBL Wave Buds 2 — R$ 232,00</h2>"),
    ("<h2 id=\"powerbank\" class=\"wp-block-heading\">🔋 4. Anker 737 Power Bank — R$ 636,64</h2>",
     "<h2 id=\"powerbank\" class=\"wp-block-heading\">🔋 4. Anker 737 Power Bank — R$ 639,00</h2>"),
    ("<h2 id=\"roteador\" class=\"wp-block-heading\">📶 5. Roteador TP-Link Archer AX12 — R$ 179,10</h2>",
     "<h2 id=\"roteador\" class=\"wp-block-heading\">📶 5. Roteador TP-Link Archer AX12 (EX1500) — R$ 169,15</h2>"),
    ("<h2 id=\"hub\" class=\"wp-block-heading\">🔌 6. Hub USB-C UGREEN 5 em 1 — R$ 89,00</h2>",
     "<h2 id=\"hub\" class=\"wp-block-heading\">🔌 6. Hub USB-C UGREEN 5 em 1 — R$ 99,00</h2>"),
    ("Mouse Logitech M185 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 67,19 | Ambidestro</span>",
     "Mouse Logitech M185 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 68,90 | Ambidestro</span>"),
    (">🛍️ Amazon — R$ 67,19</a>", ">🛍️ Amazon — R$ 68,90</a>"),
    (">🛍️ ML — R$ 67,89</a>", ">🛍️ ML — R$ 97,37</a>"),
    ("Teclado Pebble Keys 2 K380 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 192,05 | Bluetooth</span>",
     "Teclado Pebble Keys 2 K380s <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 197,99 | Bluetooth</span>"),
    (">🛍️ Amazon — R$ 193,99</a>", ">🛍️ Amazon — R$ 197,99</a>"),
    (">🛍️ ML — R$ 192,05</a>", ">🛍️ ML — R$ 198,80</a>"),
    ("JBL Wave Buds 2 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 235,00 | ANC + 40h</span>",
     "JBL Wave Buds 2 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 232,00 | ANC + 40h</span>"),
    (">🛍️ Amazon — R$ 235,00</a>", ">🛍️ Amazon — R$ 232,00</a>"),
    (">🛍️ ML — R$ 289,80</a>", ">🛍️ ML — R$ 349,00</a>"),
    ("Anker 737 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 636,64 | 25.000mAh 165W</span>",
     "Anker 737 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 639,00 | 24–25K · 140–165W</span>"),
    (">🛍️ Amazon — R$ 636,64</a>", ">🛍️ Amazon — R$ 748,99</a>"),
    (">🛍️ ML — R$ 644,00</a>", ">🛍️ ML — R$ 639,00 cupom</a>"),
    ("TP-Link Archer AX12 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 179,10 | Wi-Fi 6</span>",
     "TP-Link Archer AX12 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 169,15 | Wi-Fi 6</span>"),
    (">🛍️ Amazon — R$ 314,90</a>", ">🛍️ Amazon — R$ 315,00</a>"),
    (">🛍️ ML — R$ 179,10</a>", ">🛍️ ML — R$ 169,15</a>"),
    ("Hub UGREEN 5 em 1 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 89,00 | HDMI 4K</span>",
     "Hub UGREEN 5 em 1 <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 99,00 | HDMI 4K</span>"),
    (">🛍️ ML — R$ 89,00</a>", ">🛍️ ML — R$ 99,00</a>"),
    ("As <strong>30.181 avaliações na Amazon</strong> com nota 4,7★ comprovam a confiabilidade.",
     "As avaliações positivas de compradores na Amazon e no Mercado Livre comprovam a confiabilidade."),
]

erros = 0
for old, new in PARES:
    n = src.count(old)
    if n != 1:
        print(f"ERRO ({n}x): {old[:80]}...")
        erros += 1
    else:
        src = src.replace(old, new)

if erros:
    print(f"{erros} substituição(ões) falharam — nada foi gravado.")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(src)
print(f"OK: {len(PARES)} substituições aplicadas (parte B1).")
