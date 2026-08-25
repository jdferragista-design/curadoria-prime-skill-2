#!/usr/bin/env python3
"""Patch 25/08/2026 — parte G: alinhar 5 seções ao padrão golden.
1) Índice do conteúdo: REMOVIDO (não existe nos modelos golden).
2) FAQ: perguntas/respostas viram cards do padrão lista-golden.
3) 'Como chegamos às notas' + 'Notas por critério': substituídos pelo bloco
   de avaliação golden (grid 3×2 + badge de nota geral) e box amarelo 🧮.
4) Escolha Rápida: 3 blocos FIXOS lado a lado (repeat(3,1fr)) c/ fallback mobile."""
import re
import sys
sys.path.insert(0, "tools")
from patch_guia_g_blocks_a import BLOCO_AVALIACAO
from patch_guia_g_blocks_b import BLOCO_COMO_CHEGAMOS, ESCOLHA_RAPIDA, FAQ_CARD

F = "articles/html_output/melhores-techs-custo-beneficio-2026.html"
WP_OPEN, WP_CLOSE = "<!-- wp:html -->", "<!-- /wp:html -->"
s = open(F, encoding="utf-8").read()

def bloco_contendo(s, ancora):
    i = s.find(ancora)
    assert i != -1, f"âncora não encontrada: {ancora[:60]}"
    bs = s.rfind(WP_OPEN, 0, i)
    be = s.find(WP_CLOSE, i) + len(WP_CLOSE)
    return bs, be

# ── 1) REMOVER Índice do conteúdo ──
bs, be = bloco_contendo(s, "📑 Índice do conteúdo")
s = s[:bs].rstrip() + "\n\n" + s[be:].lstrip("\n")

# ── 2) FAQ → cards golden ──
pat = re.compile(
    r'<!-- wp:heading \{"level":3\} -->\n<h3 class="wp-block-heading">([^<]+)</h3>\n'
    r'<!-- /wp:heading -->\n\n<!-- wp:paragraph -->\n<p>(.*?)</p>\n<!-- /wp:paragraph -->',
    re.S,
)
n_faq = 0
def _faq(m):
    global n_faq
    n_faq += 1
    return FAQ_CARD.format(q=m.group(1), a=m.group(2))
s = pat.sub(_faq, s)
assert n_faq == 6, f"esperado 6 FAQs, convertido {n_faq}"

# ── 3) Como chegamos + Notas por critério → bloco de avaliação golden + 🧮 ──
bs, _ = bloco_contendo(s, "📊 Como chegamos às notas")
je = s.find('<!-- wp:heading {"anchor":"veredito"} -->')
assert je != -1
be = s.rfind(WP_CLOSE, 0, je) + len(WP_CLOSE)
s = s[:bs] + BLOCO_AVALIACAO + "\n\n" + BLOCO_COMO_CHEGAMOS + "\n\n" + s[be:]

# ── 4) Escolha Rápida → 3 blocos lado a lado ──
bs, be = bloco_contendo(s, "⚡ Escolha Rápida")
s = s[:bs] + ESCOLHA_RAPIDA + "\n\n" + s[be:]

open(F, "w", encoding="utf-8").write(s)
print(f"OK: índice removido, {n_faq} FAQs em cards, avaliação golden + 🧮 inseridos, escolha rápida 3 colunas.")
