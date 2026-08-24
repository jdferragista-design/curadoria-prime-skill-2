#!/usr/bin/env python3
"""Patch 25/08/2026 — parte E: reposicionamento editorial do guia.
De 'volta às aulas' (dessazonalizado) para 'melhores techs custo-benefício
para trabalhar e estudar' (evergreen). Novo slug/canonical e arquivo."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

# (old, new, contagem_esperada)
PARES = [
    # ── cabeçalho interno ──
    ("GUIA VOLTA ÀS AULAS TECH 2026 — 7 ESSENCIAIS",
     "MELHORES TECHS CUSTO-BENEFÍCIO 2026 — TRABALHO E ESTUDO — 7 ESSENCIAIS", 1),
    ("  • Palavra-chave foco: guia volta às aulas tech 2026",
     "  • Palavra-chave foco: melhores techs custo-benefício", 1),
    ("  • Título SEO: Guia Volta às Aulas Tech 2026: 7 Itens de R$ 69 a R$ 639",
     "  • Título SEO: 7 Melhores Techs Custo-Benefício para Trabalhar e Estudar (2026)", 1),
    ("  • URL (slug): /guia-volta-as-aulas-tech-2026-7-itens/",
     "  • URL (slug): /melhores-techs-custo-beneficio-2026/", 1),
    ("    \"Guia volta às aulas tech 2026: mouse, teclado, fone, power bank, roteador, hub e suporte. 7 essenciais de R$ 69 a R$ 639. Veja o veredito.\"",
     "    \"Os 7 techs com melhor custo-benefício para trabalhar e estudar em 2026: mouse, teclado, fone ANC, power bank, roteador, hub e suporte. De R$ 69 a R$ 639.\"", 1),
    # ── head ──
    ("<title>Guia Volta às Aulas Tech 2026: 7 Itens de R$ 69 a R$ 639</title>",
     "<title>7 Melhores Techs Custo-Benefício para Trabalhar e Estudar (2026)</title>", 1),
    ("<link rel=\"canonical\" href=\"https://curadoriaprime.com/guia-volta-as-aulas-tech-2026-7-itens/\">",
     "<link rel=\"canonical\" href=\"https://curadoriaprime.com/melhores-techs-custo-beneficio-2026/\">", 1),
    # ── hero ──
    ("📌 Guia Premium — Volta às Aulas 2026",
     "📌 Guia Premium — Melhores Techs 2026", 1),
    ("Montamos o <strong style=\"color:#93c5fd;\">guia volta às aulas tech 2026</strong> completo:",
     "Montamos o <strong style=\"color:#93c5fd;\">guia dos melhores techs custo-benefício de 2026</strong> para trabalhar e estudar:", 1),
    ("Guia volta às aulas tech 2026: 7 essenciais que somam R$ 1.564",
     "Melhores techs custo-benefício 2026: 7 essenciais que somam R$ 1.564", 1),
    # ── prova social (JBL) ──
    ("— o queridinho da volta às aulas.</em>",
     "— o queridinho para quem estuda e trabalha.</em>", 1),
    # ── intro ──
    ("<p>A volta às aulas de 2026 pede mais do que caderno e mochila. Com aulas híbridas, trabalhos em grupo online e a rotina cada vez mais digital, ter um <strong>guia volta às aulas tech 2026</strong> bem montado faz toda a diferença entre estudar com conforto ou lutar contra equipamentos que travam, descarregam ou desconectam no pior momento.</p>",
     "<p>A rotina de 2026 mistura trabalho híbrido, aulas online e tudo o que vive na nuvem — e pede mais do que caderno e mochila. Montar um setup com os <strong>melhores techs custo-benefício</strong> faz toda a diferença entre render no trabalho e nos estudos ou lutar contra equipamentos que travam, descarregam ou desconectam no pior momento.</p>", 1),
    # ── FAQ visível ──
    ("<h3 class=\"wp-block-heading\">1. Quanto custa o guia volta às aulas tech 2026 completo?</h3>",
     "<h3 class=\"wp-block-heading\">1. Quanto custa o kit completo dos melhores techs custo-benefício?</h3>", 1),
    # ── veredito ──
    ("O <strong>guia volta às aulas tech 2026</strong> entrega exatamente o que promete",
     "O <strong>guia dos melhores techs custo-benefício de 2026</strong> entrega exatamente o que promete", 1),
    # ── última atualização ──
    ("<strong>Produtos em análise:</strong> 7 itens do guia volta às aulas tech 2026<br>",
     "<strong>Produtos em análise:</strong> 7 itens tech para trabalhar e estudar<br>", 1),
    # ── JSON-LD ──
    ("\"headline\": \"Guia Volta às Aulas Tech 2026: 7 Essenciais de R$ 69 a R$ 639\"",
     "\"headline\": \"7 Melhores Techs Custo-Benefício para Trabalhar e Estudar (2026)\"", 1),
    ("\"description\": \"Guia volta às aulas tech 2026: mouse, teclado, fone, power bank, roteador, hub e suporte. 7 essenciais de R$ 67 a R$ 637. Veja o veredito.\"",
     "\"description\": \"Os 7 techs com melhor custo-benefício para trabalhar e estudar: mouse, teclado, fone, power bank, roteador, hub e suporte. De R$ 69 a R$ 639. Veja o veredito.\"", 1),
    ("\"mainEntityOfPage\": \"https://curadoriaprime.com/guia-volta-as-aulas-tech-2026-7-itens/\"",
     "\"mainEntityOfPage\": \"https://curadoriaprime.com/melhores-techs-custo-beneficio-2026/\"", 1),
    ("\"name\": \"Guia Volta às Aulas Tech 2026\"",
     "\"name\": \"Melhores Techs Custo-Benefício 2026 para Trabalhar e Estudar\"", 1),
    ("{ \"@type\": \"Question\", \"name\": \"Quanto custa o guia volta às aulas tech 2026 completo?\"",
     "{ \"@type\": \"Question\", \"name\": \"Quanto custa o kit completo dos melhores techs custo-benefício?\"", 1),
]

ALT_OLD = " — guia volta às aulas tech 2026\""
ALT_NEW = " — melhores techs custo-benefício 2026\""

erros = 0
for old, new, exp in PARES:
    n = src.count(old)
    if n != exp:
        print(f"ERRO ({n}x, esperado {exp}): {old[:90]}...")
        erros += 1
    else:
        src = src.replace(old, new)

# alts das imagens de produto (8: 6 produtos + anker duplicado no card âncora + suporte novo)
n_alt = src.count(ALT_OLD)
if n_alt != 8:
    print(f"ERRO alts ({n_alt}x, esperado 8)")
    erros += 1
else:
    src = src.replace(ALT_OLD, ALT_NEW)

if erros:
    print(f"{erros} substituição(ões) falharam — nada foi gravado.")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(src)
print(f"OK: {len(PARES)} pares + {n_alt} alts aplicados (parte E).")
