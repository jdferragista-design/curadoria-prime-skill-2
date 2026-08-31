#!/usr/bin/env python3
"""Patch B (25/08/2026) — complemento do patch_tablet_a9_convencional.py.
Aplica as edições 1-5 que ficaram apenas em memória na primeira execução
(a parte 2 do script relia o arquivo do disco e as descartou):
hero, índice, intro, resposta rápida, cabeçalho da tabela + legenda dos
asteriscos, e texto da resposta no JSON-LD (acceptedAnswer)."""
import io

F = "articles/html_output/tablet-infantil-dia-das-criancas-2026-3-melhores.html"
s = io.open(F, encoding="utf-8").read()


def trocar(txt, velho, novo):
    n = txt.count(velho)
    assert n == 1, f"esperado 1, encontrado {n}: {velho[:80]!r}"
    return txt.replace(velho, novo)


# 1) Legenda do hero
s = trocar(s,
    'Galaxy Tab A9 usa Samsung Kids + capa infantil avulsa (modelo Kids Edition importado sem estoque BR em 11/08/2026)',
    'Galaxy Tab A9 usa Samsung Kids + capa infantil avulsa — tablet convencional em modo Kids, não modelo infantil de fábrica (Kids Edition importada sem estoque BR em 11/08/2026)')

# 2) Rótulo no índice
s = trocar(s,
    '🛡️ 2. Galaxy Tab A9 + Kids (8,5/10)',
    '🛡️ 2. Galaxy Tab A9 em modo Kids (8,5/10)')

# 3) Parágrafo de introdução
s = trocar(s,
    'o <strong>Galaxy Tab A9 com Samsung Kids</strong> (Tab A9 normal 8,7" + capa infantil avulsa — Kids Edition importada sem estoque BR em 11/08/2026, mesmo Samsung Kids nativo)',
    'o <strong>Galaxy Tab A9 em modo Samsung Kids</strong> (atenção: é um <strong>tablet convencional</strong>, não um modelo infantil de fábrica — Tab A9 normal 8,7" configurado com Samsung Kids + capa infantil avulsa; a Kids Edition importada está sem estoque BR em 11/08/2026)')

# 4) Card da resposta rápida
s = trocar(s,
    '<strong style="display: block; margin-bottom: 6px; color: #1e40af;">🛡️ Mais seguro</strong><strong>Galaxy Tab A9 (com Samsung Kids)</strong> — R$ 1.114 no Pix (ML):',
    '<strong style="display: block; margin-bottom: 6px; color: #1e40af;">🛡️ Mais seguro (convencional em modo Kids)</strong><strong>Galaxy Tab A9</strong>, tablet convencional configurado com Samsung Kids — R$ 1.114 no Pix (ML):')

# 5a) Cabeçalho da coluna na tabela comparativa
s = trocar(s,
    '<th style="padding: 12px 14px; text-align: center;">Galaxy A9 + Kids</th>',
    '<th style="padding: 12px 14px; text-align: center;">Galaxy A9 (modo Kids)*</th>')

# 5b) Legenda dos asteriscos após a tabela
s = trocar(s,
    '<strong>8,5/10</strong></td></tr>\n</tbody>\n</table>\n</div>\n<!-- /wp:html -->',
    '<strong>8,5/10</strong></td></tr>\n</tbody>\n</table>\n<p style="font-size: 12px; color: #64748b; margin: 10px 0 0;">* O <strong>Galaxy Tab A9 é um tablet convencional de entrada</strong> (tela TFT 90 Hz, não IPS) usado em modo Samsung Kids com capa infantil avulsa — diferente dos outros dois, não é um modelo infantil de fábrica.</p>\n</div>\n<!-- /wp:html -->')

# 6) Texto da resposta no JSON-LD (FAQPage acceptedAnswer)
s = trocar(s,
    '"text": "Para a maioria (4-10 anos), o Galaxy Tab A9 com Samsung Kids é a opção mais confiável.',
    '"text": "Para a maioria (4-10 anos), o Galaxy Tab A9 em modo Samsung Kids — um tablet convencional configurado para crianças — é a opção mais confiável.')

io.open(F, "w", encoding="utf-8").write(s)
print("OK patch B: hero, índice, intro, resposta rápida, tabela+legenda e JSON-LD atualizados.")
