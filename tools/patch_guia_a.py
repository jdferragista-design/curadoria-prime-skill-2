#!/usr/bin/env python3
"""Patch 24/08/2026 — recaptura de mercado do guia volta-as-aulas (parte A: substituições pontuais)."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    # title tag
    ("<title>Guia Volta às Aulas Tech 2026: 7 Itens de R$ 67 a R$ 637</title>",
     "<title>Guia Volta às Aulas Tech 2026: 7 Itens de R$ 69 a R$ 639</title>"),
    # hero parágrafo
    ("que somam <strong style=\"color:#93c5fd;\">R$ 1.569</strong> e cobrem",
     "que somam <strong style=\"color:#93c5fd;\">R$ 1.563,97</strong> e cobrem"),
    ("Analisamos <strong>especificações oficiais, preços reais de 05/08/2026 e +90 mil avaliações de compradores</strong>",
     "Analisamos <strong>especificações oficiais, preços reais de 24/08/2026 e +60 mil avaliações de compradores</strong>"),
    # hero badges
    ("⭐ 4,8/5 média em +90 mil avaliações", "⭐ 4,8/5 média em +60 mil avaliações"),
    ("💰 Total: R$ 1.569</span>", "💰 Total: R$ 1.564</span>"),
    ("🕒 Atualizado: 05/08/2026", "🕒 Atualizado: 24/08/2026"),
    # metodologia
    ("(preços oficiais e conteúdo das caixas checados em 05/08/2026)",
     "(preços oficiais e conteúdo das caixas checados em 05/08 e 24/08/2026)"),
    # box prova social — rótulo de datas
    ("🗣️ O que dizem os compradores <span style=\"font-size: 12px; font-weight: 400; color: #64748b;\">(dados coletados em 05/08/2026 na Amazon e Mercado Livre)</span>",
     "🗣️ O que dizem os compradores <span style=\"font-size: 12px; font-weight: 400; color: #64748b;\">(avaliações coletadas em 05/08/2026 · preços re-verificados em 24/08/2026)</span>"),
    # card âncora Anker
    ("Anker 737 Power Bank <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 636,64 | 25.000mAh 165W</span>",
     "Anker 737 Power Bank <span style=\"font-weight: 400; color: #888; font-size: 14px;\">R$ 639,00 | 24–25K · 140–165W</span>"),
    (">🛍️ Ver na Amazon — R$ 636,64</a>", ">🛍️ Ver na Amazon — R$ 748,99</a>"),
    (">🛍️ Ver no ML — R$ 644,00</a>", ">🛍️ Ver no ML — R$ 639,00 cupom</a>"),
    # por que montar este kit
    ("<strong style=\"color: #166534;\">Preços verificados:</strong> todos capturados em 05/08/2026 nas 2 maiores lojas",
     "<strong style=\"color: #166534;\">Preços verificados:</strong> todos recapturados em 24/08/2026 nas 2 maiores lojas"),
    ("<strong style=\"color: #166534;\">Prova social:</strong> +90 mil avaliações somadas entre os 7 produtos",
     "<strong style=\"color: #166534;\">Prova social:</strong> +60 mil avaliações somadas entre os 7 produtos"),
    ("<strong style=\"color: #166534;\">Total acessível:</strong> R$ 1.569 para o kit completo",
     "<strong style=\"color: #166534;\">Total acessível:</strong> R$ 1.564 para o kit completo"),
    # pontos de atenção
    ("<strong style=\"color: #991b1b;\">Roteador:</strong> diferença de 43% entre lojas (R$ 179 ML vs R$ 315 Amazon)",
     "<strong style=\"color: #991b1b;\">Roteador:</strong> quase o dobro do preço na Amazon (R$ 315 vs R$ 169,15 no ML)"),
    ("<strong style=\"color: #991b1b;\">Suporte sem ventoinha:</strong> dissipação passiva apenas — não resfria ativamente o notebook",
     "<strong style=\"color: #991b1b;\">Vendedores terceiros:</strong> suporte e hub são vendidos por lojas parceiras na Amazon — prazos e devolução podem variar"),
    # intro linha 102
    ("com <strong>preços verificados em 05/08/2026</strong> na Amazon e Mercado Livre",
     "com <strong>preços re-verificados em 24/08/2026</strong> na Amazon e Mercado Livre"),
    # índice
    ("<a href=\"#suporte\" rel=\"noopener\">Suporte PRINCASE</a>",
     "<a href=\"#suporte\" rel=\"noopener\">Suporte giratório</a>"),
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
print(f"OK: {len(PARES)} substituições aplicadas.")
