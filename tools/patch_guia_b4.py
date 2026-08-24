#!/usr/bin/env python3
"""Patch 24/08/2026 — parte B4: tabela comparativa e reescrita da seção 7 (suporte)."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

TD = "<td style=\"padding: 10px 14px; border-bottom: 1px solid #e2e8f0;\">"
PARES = [
    # ── tabela: células de preço (contexto de célula garante unicidade pós-B1) ──
    (f"{TD}R$ 67,19 Pix</td>", f"{TD}R$ 68,90 Pix</td>"),
    (f"{TD}R$ 67,89 Pix</td>", f"{TD}R$ 97,37</td>"),
    (f"{TD}<strong>R$ 67,19</strong></td>", f"{TD}<strong>R$ 68,90</strong></td>"),
    (f"{TD}R$ 193,99</td>", f"{TD}R$ 197,99</td>"),
    (f"{TD}R$ 192,05 Pix</td>", f"{TD}R$ 198,80</td>"),
    (f"{TD}<strong>R$ 192,05</strong></td>", f"{TD}<strong>R$ 197,99</strong></td>"),
    (f"{TD}R$ 235,00</td>", f"{TD}R$ 232,00</td>"),
    (f"{TD}R$ 289,80 Pix</td>", f"{TD}R$ 349,00</td>"),
    (f"{TD}<strong>R$ 235,00</strong></td>", f"{TD}<strong>R$ 232,00</strong></td>"),
    (f"{TD}R$ 636,64 Pix</td>", f"{TD}R$ 748,99 (A1695)</td>"),
    (f"{TD}R$ 644,00 cupom</td>", f"{TD}R$ 639,00 cupom (A1289)</td>"),
    (f"{TD}<strong>R$ 636,64</strong></td>", f"{TD}<strong>R$ 639,00</strong></td>"),
    (f"{TD}R$ 314,90</td>", f"{TD}R$ 315,00</td>"),
    (f"{TD}R$ 179,10 Pix</td>", f"{TD}R$ 169,15 Pix</td>"),
    (f"{TD}<strong>R$ 179,10</strong></td>", f"{TD}<strong>R$ 169,15</strong></td>"),
    (f"{TD}R$ 89,00 Pix</td>", f"{TD}R$ 99,00</td>"),
    (f"{TD}<strong>R$ 89,00</strong></td>", f"{TD}<strong>R$ 99,00</strong></td>"),
    # ── tabela: linha do suporte renomeada + preços ──
    ("<strong>💻 Suporte PRINCASE</strong>", "<strong>💻 Suporte giratório c/ ventoinha</strong>"),
    (f"{TD}R$ 170,05 Pix</td>", f"{TD}R$ 157,93 Pix</td>"),
    (f"{TD}R$ 183,90 Pix</td>", f"{TD}R$ 188,00</td>"),
    (f"{TD}<strong>R$ 170,05</strong></td>", f"{TD}<strong>R$ 157,93</strong></td>"),
    # ── tabela: avaliações não verificáveis → traço; total e soma ──
    (f"{TD}4,9★ (6.442)</td>", f"{TD}—</td>"),
    (f"{TD}4,7★ (79)</td>", f"{TD}—</td>"),
    ("<strong>R$ 1.569,03</strong></td>", "<strong>R$ 1.563,97</strong></td>"),
    ("+90 mil avaliações</td>", "+60 mil avaliações</td>"),
    # ── seção 7: h2, parágrafo, card, imagem e CTAs ──
    ("<h2 id=\"suporte\" class=\"wp-block-heading\">💻 7. Suporte Notebook PRINCASE — R$ 170,05</h2>",
     "<h2 id=\"suporte\" class=\"wp-block-heading\">💻 7. Suporte de Notebook Giratório 360° c/ Ventoinha — R$ 157,93</h2>"),
    ("<p>O <strong>Suporte PRINCASE</strong> é o upgrade ergonômico que seu pescoço agradece. Com <strong>altura ajustável, base antiderrapante e design aberto</strong> que melhora a dissipação de calor, ele eleva o notebook à altura dos olhos e mantém a postura correta durante horas de estudo. Estrutura de alumínio resistente, compatível com notebooks de 10 a 17 polegadas.</p>",
     "<p>Este <strong>suporte giratório 360° com ventoinha integrada</strong> resolve dois problemas de quem estuda horas seguidas: ergonomia e calor. Feito em metal com haste reforçada (suporta até 10 kg), ajusta a altura entre <strong>4 cm e 26 cm</strong>, gira sobre a base para compartilhar a tela e conta com refrigeração ativa que ajuda a dissipar o calor do notebook. Base e plataforma com silicone antiderrapante, compatível com notebooks de 10 a 17 polegadas.</p>"),
    ("Suporte PRINCASE <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 170,05 | Alumínio</span>",
     "Suporte giratório 360° c/ ventoinha <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 157,93 | Metal + cooler</span>"),
    ("<img src=\"https://m.media-amazon.com/images/I/41Ol4c-56KL._AC_SL1500_.jpg\" alt=\"Suporte para notebook PRINCASE em alumínio com altura ajustável — guia volta às aulas tech 2026\"",
     "<!-- ⚠️ EDITOR: subir a foto correta do suporte giratório c/ ventoinha no WP Media antes de publicar -->\n<img src=\"https://curadoriaprime.com/wp-content/uploads/2026/08/suporte-giratorio-notebook-ventoinha.jpg\" alt=\"Suporte de notebook giratório 360° em metal com ventoinha — guia volta às aulas tech 2026\""),
    (">🛍️ Amazon — R$ 170,05</a>", ">🛍️ Amazon — R$ 157,93</a>"),
    (">🛍️ ML — R$ 183,90</a>", ">🛍️ ML — R$ 188,00</a>"),
]

erros = 0
for old, new in PARES:
    n = src.count(old)
    if n != 1:
        print(f"ERRO ({n}x): {old[:90]}...")
        erros += 1
    else:
        src = src.replace(old, new)

if erros:
    print(f"{erros} substituição(ões) falharam — nada foi gravado.")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(src)
print(f"OK: {len(PARES)} substituições aplicadas (parte B4).")
