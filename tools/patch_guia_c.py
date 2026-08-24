#!/usr/bin/env python3
"""Patch 24/08/2026 — parte C: resíduos (escolha rápida, tiers, header Rank Math, metodologia)."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    # escolha rápida
    ("<strong>🎓 Orçamento apertado:</strong> comece com Mouse M185 (R$ 67) + JBL Wave Buds 2 (R$ 235) = <strong>R$ 302</strong>",
     "<strong>🎓 Orçamento apertado:</strong> comece com Mouse M185 (R$ 68,90) + JBL Wave Buds 2 (R$ 232) = <strong>R$ 300,90</strong>"),
    ("<strong>💻 Estudo em casa:</strong> adicione Roteador AX12 (R$ 179) + Suporte PRINCASE (R$ 170) = <strong>R$ 651</strong>",
     "<strong>💻 Estudo em casa:</strong> adicione Roteador AX12 (R$ 169,15) + Suporte giratório c/ ventoinha (R$ 157,93) = <strong>R$ 627,98</strong>"),
    ("<strong>🚀 Guia completo:</strong> todos os 7 produtos = <strong>R$ 1.569</strong>",
     "<strong>🚀 Guia completo:</strong> todos os 7 produtos = <strong>R$ 1.563,97</strong>"),
    # para quem NÃO é
    ("kit completo custa R$ 1.569 — considere montar por partes",
     "kit completo custa R$ 1.564 — considere montar por partes"),
    # comparativo de kits
    ("Guia Premium (R$ 1.569)", "Guia Premium (R$ 1.564)"),
    # header Rank Math (reaplicar)
    ("  • Título SEO: Guia Volta às Aulas Tech 2026: 7 Itens de R$ 67 a R$ 637\n  • URL (slug): /guia-volta-as-aulas-tech-2026-7-itens/\n  • Meta descrição:\n    \"Guia volta às aulas tech 2026: mouse, teclado, fone, power bank, roteador, hub e suporte. 7 essenciais de R$ 67 a R$ 637. Veja o veredito.\"\n  ⚠️ PRÉ-PUBLICAÇÃO: re-verificar preços/links (última coleta 05/08/2026) e\n  subir imagens para o Media (hero + 7 produtos) antes de agendar.",
     "   • Título SEO: Guia Volta às Aulas Tech 2026: 7 Itens de R$ 69 a R$ 639\n   • URL (slug): /guia-volta-as-aulas-tech-2026-7-itens/\n  • Meta descrição:\n    \"Guia volta às aulas tech 2026: mouse, teclado, fone, power bank, roteador, hub e suporte. 7 essenciais de R$ 69 a R$ 639. Veja o veredito.\"\n   ✅ MERCADO (24/08/2026): preços/links re-verificados — 14 capturas novas no\n   LEDGER. Total do kit: R$ 1.563,97. Seção 7 REESCRITA: os links hoje\n   entregam um suporte giratório 360° com ventoinha (não é o antigo PRINCASE).\n   ⚠️ PRÉ-PUBLICAÇÃO: subir imagens no WP Media antes de agendar —\n   hero-kit-volta-aulas-2026.jpg + 7 fotos (foto do suporte deve ser a do\n   modelo giratório c/ ventoinha: uploads/2026/08/suporte-giratorio-notebook-ventoinha.jpg)."),
    # metodologia: lista de fabricantes sem PRINCASE
    ("(Logitech, JBL, Anker, TP-Link, UGREEN, PRINCASE)",
     "(Logitech, JBL, Anker, TP-Link, UGREEN)"),
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
print(f"OK: {len(PARES)} substituições aplicadas (parte C).")
