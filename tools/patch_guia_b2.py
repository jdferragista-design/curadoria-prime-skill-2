#!/usr/bin/env python3
"""Patch 24/08/2026 — parte B2: FAQ, contras, fontes, datas e JSON-LD."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    # FAQ texto
    ("soma <strong>R$ 1.569,03</strong> (menores preços de 05/08/2026)",
     "soma <strong>R$ 1.563,97</strong> (menores preços de 24/08/2026)"),
    # contras / upgrade
    ("<strong style=\"color: #991b1b;\">Investimento alto à vista:</strong> R$ 1.569 pelo kit completo",
     "<strong style=\"color: #991b1b;\">Investimento alto à vista:</strong> R$ 1.564 pelo kit completo"),
    ("o Anker 737 custa 40% do valor total do kit",
     "o Anker 737 custa ~41% do valor total do kit"),
    ("economize ~R$ 487", "economize ~R$ 490"),
    # fontes / última atualização / aviso afiliado
    ("preços e avaliações coletados em 05/08/2026 na Amazon e Mercado Livre.",
     "preços re-verificados em 24/08/2026 na Amazon e Mercado Livre."),
    ("<strong>📌 Última atualização:</strong> 05/08/2026",
     "<strong>📌 Última atualização:</strong> 24/08/2026"),
    ("Os preços mencionados foram verificados em <strong>05/08/2026</strong>.",
     "Os preços mencionados foram verificados em <strong>24/08/2026</strong>."),
    ("Preços e disponibilidade verificados em 05/08/2026 e sujeitos a alteração pelos varejistas.",
     "Preços e disponibilidade verificados em 24/08/2026 e sujeitos a alteração pelos varejistas."),
    # JSON-LD: headline, mainEntityOfPage, dateModified, script duplo
    ("\"headline\": \"Guia Volta às Aulas Tech 2026: 7 Essenciais de R$ 67 a R$ 637\"",
     "\"headline\": \"Guia Volta às Aulas Tech 2026: 7 Essenciais de R$ 69 a R$ 639\""),
    ("\"mainEntityOfPage\": \"https://curadoriaprime.com/kit-volta-as-aulas-tech-2026/\"",
     "\"mainEntityOfPage\": \"https://curadoriaprime.com/guia-volta-as-aulas-tech-2026-7-itens/\""),
    ("</script></script>", "</script>"),
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
print(f"OK: {len(PARES)} substituições aplicadas (parte B2).")
