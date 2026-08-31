#!/usr/bin/env python3
"""Patch 25/08/2026 — correção editorial: o Galaxy Tab A9 NÃO é um tablet infantil.
Reenquadra todo o artigo deixando explícito que o Tab A9 é um TABLET CONVENCIONAL
configurado com modo Samsung Kids + capa avulsa (diferente dos modelos infantis
dedicados Kid Pad e Vision Tab 7). Também adiciona legenda para os asteriscos
da tabela comparativa (TFT 90Hz, capa avulsa)."""
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

# 5) Cabeçalho da tabela + legenda dos asteriscos
s = trocar(s,
    '<th style="padding: 12px 14px; text-align: center;">Galaxy A9 + Kids</th>',
    '<th style="padding: 12px 14px; text-align: center;">Galaxy A9 (modo Kids)*</th>')
s = trocar(s,
    '<strong>8,5/10</strong></td></tr>\n</tbody>\n</table>\n</div>\n<!-- /wp:html -->',
    '<strong>8,5/10</strong></td></tr>\n</tbody>\n</table>\n<p style="font-size: 12px; color: #64748b; margin: 10px 0 0;">* O <strong>Galaxy Tab A9 é um tablet convencional de entrada</strong> (tela TFT 90 Hz, não IPS) usado em modo Samsung Kids com capa infantil avulsa — diferente dos outros dois, não é um modelo infantil de fábrica.</p>\n</div>\n<!-- /wp:html -->')


# ── parte 2 ──
s = io.open(F, encoding="utf-8").read()

# 6) H2 e parágrafo da seção do A9
s = trocar(s,
    '<h2 id="taba9kids" class="wp-block-heading">🛡️ Galaxy Tab A9 (com Samsung Kids): o mais seguro para pais exigentes — 8,5/10</h2>',
    '<h2 id="taba9kids" class="wp-block-heading">🛡️ Galaxy Tab A9 em modo Kids: o tablet convencional que fica mais seguro para crianças — 8,5/10</h2>')
s = trocar(s,
    '<p>O <strong>Galaxy Tab A9 com Samsung Kids</strong> é a escolha de quem quer <strong>controle total pelo próprio celular</strong>.',
    '<p><strong>Aviso honesto: o Tab A9 não é um tablet infantil de fábrica</strong> — é um tablet convencional de entrada que vira a opção mais segura deste guia quando configurado com o modo <strong>Samsung Kids</strong> e uma capa infantil. É a escolha de quem quer <strong>controle total pelo próprio celular</strong>.')

# 7) Card de idade 9–12
s = trocar(s,
    '<strong style="display: block; margin-bottom: 6px; color: #1e40af;">🧑 9–12 anos → Galaxy Tab A9 com Samsung Kids</strong>Hardware Samsung + controle que acompanha o crescimento. Depois dos 10, dá para sair do modo Kids e usar como tablet &#8220;de gente grande&#8221;.',
    '<strong style="display: block; margin-bottom: 6px; color: #1e40af;">🧑 9–12 anos → Galaxy Tab A9 em modo Kids</strong>É um tablet convencional: hardware Samsung + controle que acompanha o crescimento. Depois dos 10, sai do modo Kids e vira o tablet &#8220;de gente grande&#8221; da criança — vantagem que os modelos infantis dedicados não têm.')

# 8) Bullet "para quem NÃO vale"
s = trocar(s,
    'os três têm hardware de brinquedo robusto, não de produtividade — considere um tablet convencional.',
    'Kid Pad e Vision têm hardware infantil dedicado e o Tab A9 é um convencional de entrada — nenhum substitui um aparelho de produtividade.')

# 9) FAQ "melhor tablet" e FAQ "diferença"
s = trocar(s,
    'Para a maioria (4-10 anos), o Galaxy Tab A9 com Samsung Kids é a opção mais confiável: controle parental robusto',
    'Para a maioria (4-10 anos), o Galaxy Tab A9 em modo Samsung Kids — um tablet convencional configurado para crianças — é a opção mais confiável: controle parental robusto')
s = trocar(s,
    'Tablet infantil já vem com capa protetora, Kids Space e loja curada. Tablet "normal" com Family Link tem hardware melhor e dura mais anos, mas exige que os pais configurem tudo manualmente.',
    'Tablet infantil já vem com capa protetora, Kids Space e loja curada (Kid Pad e Vision Tab 7). Tablet "normal" tem hardware melhor e dura mais anos, mas exige configuração manual pelos pais — é o caso do Tab A9 deste comparativo (Samsung Kids + Family Link + capa avulsa).')

# 10) Veredito (badge + parágrafo)
s = trocar(s,
    '🛡️ GALAXY TAB A9 + KIDS</p>',
    '🛡️ GALAXY TAB A9 (MODO KIDS)</p>')
s = trocar(s,
    '<strong>Confiabilidade e controle parental máximo</strong> → <strong>Galaxy Tab A9 com Samsung Kids + capa (R$ 1.114 no Pix + capa avulsa)</strong>, o mais bem avaliado (4,9/5 no ML).',
    '<strong>Confiabilidade e controle parental máximo</strong> → <strong>Galaxy Tab A9 em modo Samsung Kids + capa (R$ 1.114 no Pix + capa avulsa)</strong>, o mais bem avaliado (4,9/5 no ML) — e por ser convencional, dura mais depois que a criança crescer.')

# 11) Card de compra Samsung
s = trocar(s,
    'Galaxy Tab A9 (com Samsung Kids) + capa <span style="font-weight: 400; color: #888; font-size: 14px;">8,7" 4GB/64GB | R$ 1.114 (Pix, ML) + capa</span>',
    'Galaxy Tab A9 em modo Samsung Kids + capa <span style="font-weight: 400; color: #888; font-size: 14px;">convencional · 8,7" 4GB/64GB | R$ 1.114 (Pix, ML) + capa</span>')
s = trocar(s,
    'Nota 8,5/10. Controle parental mais rigoroso, suporte nacional e a melhor avaliação do comparativo (4,9/5 no ML, ~1.345 opiniões).',
    'Nota 8,5/10. <strong>Tablet convencional (não é modelo infantil de fábrica)</strong>: o rigor vem do modo Samsung Kids. Suporte nacional e a melhor avaliação do comparativo (4,9/5 no ML, ~1.345 opiniões).')

# 12) JSON-LD
s = trocar(s,
    '"name": "Samsung Galaxy Tab A9 com Samsung Kids",',
    '"name": "Samsung Galaxy Tab A9 em modo Samsung Kids",')

io.open(F, "w", encoding="utf-8").write(s)
print("OK: A9 reenquadrado como tablet convencional em todo o artigo.")

