#!/usr/bin/env python3
"""Patch 24/08/2026 — parte D: aviso de que os Anker 737 da Amazon e do ML são itens diferentes."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    # 1) Card âncora (topo): nota curta sob os CTAs
    ("<a style=\"background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,0.3);\" href=\"https://meli.la/2uyvRWS\" target=\"_blank\" rel=\"sponsored noopener noreferrer\">🛍️ Ver no ML — R$ 639,00 cupom</a>\n</div>\n</div>",
     "<a style=\"background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,0.3);\" href=\"https://meli.la/2uyvRWS\" target=\"_blank\" rel=\"sponsored noopener noreferrer\">🛍️ Ver no ML — R$ 639,00 cupom</a>\n</div>\n<p style=\"margin: 10px 0 0; font-size: 12.5px; color: #92400e;\">⚠️ Modelos diferentes por loja — veja o aviso completo na seção 4.</p>\n</div>"),
    # 2) Parágrafo da seção 4: explicitar que a Amazon não tem o de 24K
    ("A versão do Mercado Livre (A1289) tem 24.000mAh e 140W com display digital.",
     "A versão do Mercado Livre (A1289) tem 24.000mAh e 140W com display digital — <strong>este modelo de 24K não é vendido na Amazon</strong>."),
    # 3) Card da seção 4: box de aviso completo após os CTAs
    ("<a style=\"background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;\" href=\"https://meli.la/2uyvRWS\" target=\"_blank\" rel=\"sponsored noopener noreferrer\">🛍️ ML — R$ 639,00 cupom</a>\n</div>\n</div>",
     "<a style=\"background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;\" href=\"https://meli.la/2uyvRWS\" target=\"_blank\" rel=\"sponsored noopener noreferrer\">🛍️ ML — R$ 639,00 cupom</a>\n</div>\n<div style=\"background:#fffbeb;border:1px solid #fde68a;border-left:4px solid #f59e0b;border-radius:8px;padding:10px 14px;margin-top:12px;font-size:13px;color:#78350f;line-height:1.6;\"><strong>⚠️ Atenção: são itens diferentes.</strong> Na <strong>Amazon</strong> você encontra apenas o modelo <strong>A1695 — 25.000mAh / 165W</strong> (R$ 748,99). Já o modelo <strong>A1289 — 24.000mAh / 140W</strong>, mais barato (R$ 639 com cupom), existe <strong>somente no Mercado Livre</strong> — a Amazon não tem o de 24K. Confira o modelo na página do anúncio antes de fechar a compra.</div>\n</div>"),
    # 4) Pontos de atenção: reforço
    ("<strong style=\"color: #991b1b;\">Anker modelos diferentes:</strong> Amazon vende A1695 (25K/165W), ML vende A1289 (24K/140W)",
     "<strong style=\"color: #991b1b;\">Anker modelos diferentes:</strong> são itens distintos — a Amazon só tem o A1695 (25K/165W); o A1289 (24K/140W) é exclusivo do Mercado Livre"),
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
print(f"OK: {len(PARES)} substituições aplicadas (parte D).")
