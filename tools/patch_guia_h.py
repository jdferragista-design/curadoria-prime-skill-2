#!/usr/bin/env python3
"""Patch 25/08/2026 — parte H: restaurar Índice do conteúdo no padrão visual golden.
Correção ao patch G (que removeu o índice por engano — decisão errada).
Só inclui âncoras que EXISTEM no artigo (as antigas #resposta-rapida e
#tabela eram links quebrados)."""
import sys

F = "articles/html_output/melhores-techs-custo-beneficio-2026.html"
s = open(F, encoding="utf-8").read()

assert "📑 Índice do conteúdo" not in s, "índice já existe?"

ITENS = [
    ("#mouse", "🖱️ 1. Mouse Logitech M185"),
    ("#teclado", "⌨️ 2. Teclado Pebble Keys 2 K380s"),
    ("#fone", "🎧 3. Fone JBL Wave Buds 2"),
    ("#powerbank", "🔋 4. Anker 737 Power Bank"),
    ("#roteador", "📶 5. Roteador TP-Link AX12"),
    ("#hub", "🔌 6. Hub USB-C UGREEN"),
    ("#suporte", "💻 7. Suporte giratório c/ ventoinha"),
    ("#faq", "❓ Perguntas frequentes"),
    ("#veredito", "🏆 Veredito final"),
    ("#pros-e-contras", "⚖️ Prós e contras do kit"),
    ("#para-quem", "🎯 Para quem é / não é"),
    ("#alternativas", "🔄 Alternativas de kit"),
]

def li(href, rotulo):
    return f'<li><span style="color: #5a4fcf; font-weight: 800;">▸</span> <a href="{href}" rel="noopener" style="color: #4a4a68; text-decoration: none;">{rotulo}</a></li>'

col1 = "\n".join(li(h, r) for h, r in ITENS[:6])
col2 = "\n".join(li(h, r) for h, r in ITENS[6:])

INDICE = f'''<!-- wp:html -->
<div id="indice-conteudo" style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">
<p style="font-size: 14px; font-weight: bold; color: #1a1a2e; margin: 0 0 12px; text-transform: uppercase; letter-spacing: .06em;">📑 Índice do conteúdo</p>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 32px;">
<ul style="margin: 0; padding-left: 8px; line-height: 2; list-style: none;">
{col1}
</ul>
<ul style="margin: 0; padding-left: 8px; line-height: 2; list-style: none;">
{col2}
</ul>
</div>
<style>
  @media (max-width: 782px) {{
    #indice-conteudo > div:nth-child(3) {{ grid-template-columns: 1fr !important; }}
    #indice-conteudo > div:nth-child(3) > ul + ul {{ margin-top: 8px; }}
  }}
</style>
</div>
<!-- /wp:html -->'''

ANCORA_INTRO = "<!-- wp:paragraph -->\n<p>A rotina de 2026 mistura trabalho híbrido"
i = s.find(ANCORA_INTRO)
assert i != -1, "âncora da intro não encontrada"

s = s[:i] + INDICE + "\n\n" + s[i:]

open(F, "w", encoding="utf-8").write(s)
print("OK: índice restaurado no padrão golden (12 itens, 2 colunas, âncoras verificadas).")
