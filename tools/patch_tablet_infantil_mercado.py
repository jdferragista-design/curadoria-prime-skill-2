#!/usr/bin/env python3
"""Patch tablet-infantil 25/08/2026 — capturas reais do editor p/ Multi Kid Pad NB425.

Aplica dados reais (ML 4,4/5 129 opinioes / Amazon 2,9/5 24 globais / R$ 856,75 Pix
e R$ 884,44 Amazon), recalcula a nota do Multi para 7,0/10, corrige o HTML quebrado
do indice, alinha mainEntityOfPage ao canonical e remove afirmacoes que os dados
contradizem. Cada substituicao exige count==1 (aborta se divergir).
"""

from pathlib import Path

P = Path(__file__).resolve().parent.parent / "articles/html_output" \
    / "tablet-infantil-dia-das-criancas-2026-3-melhores.html"

REPL = [
    # S1 — hero: preco do Multi (sem <strong> no preco)
    ('<strong style="color:#FFDAB9;">Multi Kid Pad NB425 Laranja</strong> (10,1" 6GB/128GB, a partir de R$ 899)',
     '<strong style="color:#FFDAB9;">Multi Kid Pad NB425 Laranja</strong> (10,1" 6GB/128GB, a partir de R$ 856,75 no Pix)'),

    # S2 — badge nota (hero) — intervalo real com Tab A9 (4,9/5)
    ('<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ 4,7/5 em +8 mil opiniões</span>',
     '<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ Notas reais: 2,9 a 4,9/5 (Amazon e ML)</span>'),

    # S3 — badge verificado
    ('<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">🕒 Verificado: 08/08/2026</span>',
     '<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">🕒 Verificado: 08/08/2026 · Kid Pad e Tab A9: 25/08</span>'),

    # S4 — titulo do box de avaliacoes
    ('<span style="font-size: 12px; font-weight: 400; color: #64748b;">(dados coletados em 08/08/2026)</span>',
     '<span style="font-size: 12px; font-weight: 400; color: #64748b;">(dados coletados em 08/08/2026 · Kid Pad e Tab A9 reavaliados em 25/08/2026)</span>'),

    # S5 — card de avaliacao do Multi (dados reais ML + Amazon)
    ('<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #3485DB;">Mercado Livre — Multi Kid Pad NB425 Laranja</strong><br>⭐ <strong>4,8/5</strong> · <strong>~1.200 opiniões</strong> · 🏆 <strong>Mais vendido infantil</strong><br><span style="color:#475569;">Melhor nota do comparativo, com volume alto de opiniões para um modelo menos conhecido.</span>\n'
     '</div>',
     '<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #3485DB;">Multi Kid Pad NB425 Laranja</strong><br>ML: ⭐ <strong>4,4/5</strong> · <strong>129 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span><br>Amazon: ⭐ <strong>2,9/5</strong> · <strong>24 classificações globais</strong> (10 avaliadas no Brasil)<br><span style="color:#475569;">Elogios por resistência e tamanho de tela; críticas por travamentos, superaquecimento e bateria que para de carregar.</span>\n'
     '</div>'),

    # S6 — comentario ao editor (box avaliacoes)
    ('<!-- NOTA AO EDITOR: resumos acima baseados no consenso geral das avaliações coletadas em 08/08/2026.\n'
     '     Antes de publicar, se quiser citação textual, cole 1–2 avaliações reais por produto\n'
     '     (nome semi-anonimizado + data + plataforma) confirmando na página do varejo — regra anti-alucinação da casa. -->',
     '<!-- NOTA AO EDITOR: Multi Kid Pad (ML 4,4/5 · 129; Amazon 2,9/5 · 24) e Tab A9 (ML 4,9/5 · 1.345) reavaliados em 25/08/2026.\n'
     '     Positivo Vision Tab 7 aguarda recaptura para fechar o ranking. Citação textual só com avaliação real\n'
     '     (nome semi-anonimizado + data + plataforma) confirmada na página do varejo — regra anti-alucinação da casa. -->'),

    # S7 — resposta rapida (card Multi)
    ('<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#166534;">🏆 Melhor geral (custo-benefício)</p>\n'
     '<strong>Multi Kid Pad NB425 Laranja</strong> (a partir de <strong>R$ 899</strong>): tela 10,1" IPS, 6GB/128GB, bateria 6.000 mAh e controle parental completo. Capa com alça. Ideal de 4 a 10 anos.',
     '<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#166534;">🟢 Melhor custo-benefício (tela grande)</p>\n'
     '<strong>Multi Kid Pad NB425 Laranja</strong> (a partir de <strong>R$ 856,75</strong> no Pix, ML): tela 10,1" IPS, 6GB/128GB, bateria 6.000 mAh e controle parental. Capa com alça. Ressalva: relatos de defeito de bateria e travamentos. Ideal de 4 a 10 anos.'),

    # S8 — resposta rapida (card Tab A9)
    ('<strong>Galaxy Tab A9 (com Samsung Kids)</strong> (<strong>R$ 898–1.299</strong>): Samsung Kids + Google Family Link, capa infantil avulsa (R$60-110) e atualizações mais longas. Melhor para pais que querem controle total pelo celular. <span style="font-size:12px; color:#64748b;">Kids Edition importada sem estoque BR — usar Tab A9 normal.</span>',
     '<strong>Galaxy Tab A9 (com Samsung Kids)</strong> (a partir de <strong>R$ 1.114</strong> no Pix, ML): Samsung Kids + Google Family Link, capa infantil avulsa e atualizações mais longas — e a melhor avaliação do comparativo. <span style="font-size:12px; color:#64748b;">Amazon sem estoque em 25/08 — ver anúncio no ML.</span>'),

    # S9 — card de avaliacao do Tab A9 (dados reais ML; Amazon sem estoque)
    ('<div style="background: #fff; border: 1px solid #ffd499; border-left: 4px solid #FF9900; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #FF9900;">Amazon — Galaxy Tab A9 (com Samsung Kids)</strong><br>⭐ <strong>4,5/5</strong> · <strong>4.663 avaliações</strong> (modelo A9+ 11" — mesmo Samsung Kids) <br><span style="color:#475569;">Maior base de avaliações do comparativo — dado mais estatisticamente estável dos três.</span>\n'
     '</div>',
     '<div style="background: #fff; border: 1px solid #ffd499; border-left: 4px solid #FF9900; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #FF9900;">Mercado Livre — Galaxy Tab A9 64GB (Loja oficial Samsung)</strong><br>⭐ <strong>4,9/5</strong> · <strong>~1.345 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO<br><span style="color:#475569;">Melhor avaliação do comparativo: fluido, boa tela e atualizações longas. Amazon sem estoque do Tab A9 em 25/08 — o anúncio atual é o A9+ 11", outro aparelho.</span>\n'
     '</div>'),

        # S10 — tabela: cabeçalho do preço
    ('<td style="padding: 11px 14px;"><strong>Preço (verificado em 08/08/2026)</strong>',
     '<td style="padding: 11px 14px;"><strong>Preço (re-verificado 25/08)</strong>'),

    # S11 — tabela: preco Multi
    ('<td style="padding: 11px 14px; text-align: center;"><strong>R$ 899</strong></td>',
     '<td style="padding: 11px 14px; text-align: center;"><strong>R$ 856,75</strong> (Pix, ML)</td>'),

    # S12 — tabela: preco Tab A9
    ('<td style="padding: 11px 14px; text-align: center;">R$ 898–1.299*</td>',
     '<td style="padding: 11px 14px; text-align: center;">R$ 1.114 (Pix, ML)</td>'),

    # S13 — H2 do Multi
    ('<h2 id="multikid" class="wp-block-heading">🏆 Multi Kid Pad NB425 Laranja: o melhor custo-benefício geral — 9,0/10</h2>',
     '<h2 id="multikid" class="wp-block-heading">🟢 Multi Kid Pad NB425 Laranja: melhor custo-benefício em tela grande, com ressalva de durabilidade — 7,0/10</h2>'),

    # S14 — indice: nota do Multi
    ('<span>3️⃣ <a href="#multikid">Multi Kid Pad NB425 Laranja (9,0/10)</a></span>',
     '<span>3️⃣ <a href="#multikid">Multi Kid Pad NB425 Laranja (7,0/10)</a></span>'),

    # S15 — tabela: nota Multi
    ('<td style="padding: 11px 14px; text-align: center;"><strong>9,0/10</strong></td><td style="padding: 11px 14px; text-align: center;"><strong>8,5/10</strong></td><td style="padding: 11px 14px; text-align: center;"><strong>8,5/10</strong></td>',
     '<td style="padding: 11px 14px; text-align: center;"><strong>7,0/10</strong></td><td style="padding: 11px 14px; text-align: center;"><strong>8,5/10</strong></td><td style="padding: 11px 14px; text-align: center;"><strong>8,5/10</strong></td>'),

    # S16 — FAQ (HTML): resposta "qual o melhor"
    ('<p style="margin: 0; font-size: 14px; line-height: 1.65;">Para a maioria (4-10 anos), o Multi Kid Pad NB425 Laranja: tela 10,1", 6GB/128GB, bateria 6.000 mAh e controle parental completo por cerca de R$ 899. Quem prioriza controle máximo deve considerar o Galaxy Tab A9 com Samsung Kids.</p>',
     '<p style="margin: 0; font-size: 14px; line-height: 1.65;">Para a maioria (4-10 anos), o Galaxy Tab A9 com Samsung Kids é a opção mais confiável: controle parental robusto, atualizações longas e a melhor avaliação do comparativo (4,9/5 no ML). Para tela grande e custo menor, o Multi Kid Pad NB425 (R$ 856,75 no Pix) — com atenção aos relatos de defeito de bateria e travamentos. Para o orçamento mais curto, o Positivo Vision Tab 7.</p>'),

    # S17 — veredito: bloco Multi (nota e rotulo)
    ('<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px; text-align: center;">\n'
     '<p style="margin: 0 0 6px; font-size: 13px; font-weight: 700; color: #166534;">🏆 MULTI KID PAD NB425</p>\n'
     '<p style="margin: 0; font-size: 30px; font-weight: 800; color: #166534;">8.9<span style="font-size: 14px;">/10</span></p>\n'
     '<p style="margin: 6px 0 0; font-size: 12.5px; color: #166534;">Melhor geral</p>\n'
     '</div>',
     '<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px; text-align: center;">\n'
     '<p style="margin: 0 0 6px; font-size: 13px; font-weight: 700; color: #166534;">🟢 MULTI KID PAD NB425</p>\n'
     '<p style="margin: 0; font-size: 30px; font-weight: 800; color: #166534;">7.0<span style="font-size: 14px;">/10</span></p>\n'
     '<p style="margin: 6px 0 0; font-size: 12.5px; color: #166534;">Tela grande e preço baixo</p>\n'
     '</div>'),

    # S18 — veredito: Galaxy 8.7 -> 8.5 (consistencia)
    ('<p style="margin: 0; font-size: 30px; font-weight: 800; color: #1e40af;">8.7<span style="font-size: 14px;">/10</span></p>',
     '<p style="margin: 0; font-size: 30px; font-weight: 800; color: #1e40af;">8.5<span style="font-size: 14px;">/10</span></p>'),

    # S19 — veredito: Vision 8.3 -> 8.5 (consistencia)
    ('<p style="margin: 0; font-size: 30px; font-weight: 800; color: #92400e;">8.3<span style="font-size: 14px;">/10</span></p>',
     '<p style="margin: 0; font-size: 30px; font-weight: 800; color: #92400e;">8.5<span style="font-size: 14px;">/10</span></p>'),

    # S20 — resumo final do veredito
    ('<p><strong>Em resumo:</strong> para o Dia das Crianças 2026, a escolha é por idade e bolso. Até 6 anos e orçamento curto → <strong>Positivo Vision Tab 7 (R$ 383)</strong>. Uso geral 4-10 anos com melhor tela/bateria → <strong>Multi Kid Pad NB425 Laranja (R$ 759-899)</strong>. Controle parental máximo e marca premium → <strong>Galaxy Tab A9 com Samsung Kids + capa (R$ 898–1.299 + capa)</strong>. Nenhum é compra errada — o melhor é o que equilibra <strong>quanto você pode gastar e quanto controle você quer ter</strong>. E lembre-se: configure o Family Link/Samsung Kids <strong>antes</strong> de entregar o presente.</p>',
     '<p><strong>Em resumo:</strong> para o Dia das Crianças 2026, a escolha é por perfil. <strong>Confiabilidade e controle parental máximo</strong> → <strong>Galaxy Tab A9 com Samsung Kids + capa (R$ 1.114 no Pix + capa avulsa)</strong>, o mais bem avaliado (4,9/5 no ML). <strong>Tela grande com o menor preço</strong> → <strong>Multi Kid Pad NB425 (R$ 856,75 no Pix)</strong>, com ressalvas: relatos de defeito de bateria, superaquecimento e travamentos — confira as avaliações recentes antes de comprar. <strong>Primeiro tablet barato</strong> → <strong>Positivo Vision Tab 7</strong>. Nenhum é compra errada — o melhor é o que equilibra <strong>quanto você pode gastar e quanto controle você quer ter</strong>. E lembre-se: configure o Family Link/Samsung Kids <strong>antes</strong> de entregar o presente.</p>'),

    # S21 — card compra Multi: titulo/preco
    ('Multi Kid Pad NB425 Laranja <span style="font-weight: 400; color: #888; font-size: 14px;">10,1" 6GB/128GB | R$ 899</span>',
     'Multi Kid Pad NB425 Laranja <span style="font-weight: 400; color: #888; font-size: 14px;">10,1" 6GB/128GB | R$ 856,75 (Pix) · R$ 884,44 (Amazon)</span>'),

    # S22 — card compra Multi: badge
    ('<span style="background: linear-gradient(135deg,#FF6B6B 0%,#9B2226 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 800;">⭐ Recomendado 4–10 anos</span>',
     '<span style="background: linear-gradient(135deg,#FF6B6B 0%,#9B2226 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 800;">🟢 Custo-benefício (tela grande) 4–10 anos</span>'),

    # S23 — card compra Multi: nota
    ('<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 9,0/10. Tela grande, 128GB e bateria de 6.000 mAh. Capa com alça e Google Kids Space. O equilíbrioideal entre diversão e segurança.</p>',
     '<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 7,0/10. Tela grande de 10,1", 128GB e bom preço. Ressalvas de durabilidade: há relatos de bateria frágil, superaquecimento e travamentos. Capa com alça e Google Kids Space.</p>'),

    # S24 — card compra Multi: href Amazon para a URL da captura do editor
    ('href="https://link.amazon/B0aqSxjTU"',
     'href="https://link.amazon/B0alnCFJU"'),

        # S25 — hero: preco do Tab A9 (sem <strong> no preco)
    ('<strong style="color:#FFDAB9;">Samsung Galaxy Tab A9 (com Samsung Kids)</strong> (8,7" + capa infantil, a partir de R$ 899)',
     '<strong style="color:#FFDAB9;">Samsung Galaxy Tab A9 (com Samsung Kids)</strong> (8,7" + capa infantil, a partir de R$ 1.114 no Pix)'),

    # S26 — card compra A9: titulo/preco
    ('Galaxy Tab A9 (com Samsung Kids) + capa <span style="font-weight: 400; color: #888; font-size: 14px;">8,7" 4GB/64GB | R$ 898–1.299 + capa</span>',
     'Galaxy Tab A9 (com Samsung Kids) + capa <span style="font-weight: 400; color: #888; font-size: 14px;">8,7" 4GB/64GB | R$ 1.114 (Pix, ML) + capa</span>'),

    # S27 — card compra A9: nota
    ('<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. Controle parental mais rigoroso e suporte nacional. Ideal para pais que querem gerenciar tudo pelo celular. <em>Kids Edition importada sem estoque em 11/08/2026 — kit BR é Tab A9 normal (SM-X110) + capa infantil avulsa.</em></p>',
     '<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. Controle parental mais rigoroso, suporte nacional e a melhor avaliação do comparativo (4,9/5 no ML, ~1.345 opiniões). <em>Kit BR é o Tab A9 normal (SM-X110) + capa infantil avulsa (R$ 60–110); Kids Edition importada sem estoque. Amazon sem estoque do Tab A9 em 25/08/2026 — o anúncio atual é o A9+ 11", outro aparelho.</em></p>'),

    # S28 — card compra A9: CTA (remove Amazon que aponta p/ produto errado/sem estoque)
    ('<a style="background: linear-gradient(135deg, #ff9900 0%, #ff8500 100%); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://www.amazon.com.br/SAMSUNG-alto-falantes-qu%C3%A1druplos-atualizado-multijanela/dp/B0CLFH7CCV" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver na Amazon — Tab A9+ 11"</a>\n'
     '<a style="background: linear-gradient(135deg, #1428A0 0%, #0a1550 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://lista.mercadolivre.com.br/tab-a9" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver no Mercado Livre — kits com capa</a>',
     '<span style="display:block; font-size:12.5px; background:#fffbeb; border:1px solid #fde68a; border-radius:8px; padding:8px 12px; color:#78350f; margin-bottom:10px; line-height:1.6;">⚠️ <strong>Amazon sem estoque do Tab A9</strong> (verificado em 25/08/2026) — o anúncio atual da Amazon é o <strong>Tab A9+ 11"</strong>, outro aparelho, por isso não há botão da Amazon aqui.</span>\n'
     '<a style="background: linear-gradient(135deg, #1428A0 0%, #0a1550 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://lista.mercadolivre.com.br/tab-a9" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver no Mercado Livre — Tab A9 64GB · R$ 1.114 Pix</a>'),

    # S29 — JSON-LD: ratingValues
    ('"ratingValue": "8.9",', '"ratingValue": "7.0",'),
    ('"ratingValue": "8.7",', '"ratingValue": "8.5",'),
    ('"ratingValue": "8.3",', '"ratingValue": "8.5",'),

    # S30 — JSON-LD: FAQ answer
    ('"text": "Para a maioria (4-10 anos), o Multi Kid Pad NB425 Laranja: tela 10,1 polegadas, 6GB/128GB, bateria 6.000 mAh e controle parental completo por cerca de R$ 899."',
     '"text": "Para a maioria (4-10 anos), o Galaxy Tab A9 com Samsung Kids é a opção mais confiável. Para tela grande e custo menor, o Multi Kid Pad NB425 (a partir de R$ 856,75 no Pix), com atenção aos relatos de defeito de bateria."'),

    # S31 — fontes: reavaliacao de 25/08
    ('preços e avaliações coletados em 08/08/2026 em Amazon e Mercado Livre.',
     'preços e avaliações coletados em 08/08/2026 em Amazon e Mercado Livre; Kid Pad NB425 e Galaxy Tab A9 reavaliados em 25/08/2026 (Kid Pad: ML R$ 856,75 · Amazon R$ 884,44 · Tab A9: ML R$ 1.114 no Pix, Amazon sem estoque).'),

    # S32 — nota ao editor (fontes)
    ('<!-- NOTA AO EDITOR: re-verificar preços/estoque em 10/09/2026 antes de publicar (véspera da Semana da Criança). -->',
     '<!-- NOTA AO EDITOR: re-verificar preços/estoque em 10/09/2026 antes de publicar (véspera da Semana da Criança). Kid Pad NB425 e Tab A9 recapturados em 25/08; falta recapturar o Positivo Vision Tab 7 para fechar o ranking final. -->'),

    # S33 — bloco avaliacao topo: justificativa de satisfacao (dados reais)
    ('<div style="font-size:12.5px;color:#64748b;margin-top:6px;">Avaliações consistentes em Amazon e ML; relatos de pais sobre durabilidade e uso infantil.</div>',
     '<div style="font-size:12.5px;color:#64748b;margin-top:6px;">Avaliações divergentes entre os três: Kid Pad NB425 com queixas de bateria e travamento (Amazon 2,9/5); Tab A9 com 4,9/5 e volume alto; Positivo com nota intermediária.</div>'),

    # S34 — mainEntityOfPage alinhado ao canonical
    ('"mainEntityOfPage": "https://curadoriaprime.com/tablet-infantil-dia-das-criancas-2026/"',
     '"mainEntityOfPage": "https://curadoriaprime.com/tablet-infantil-dia-das-criancas-2026-3-melhores/"'),

    # S35 — alt da imagem do card Multi
    ('alt="Multi Kid Pad NB425 Laranja 10,1 polegadas com capa com alça — melhor tablet infantil Dia das Crianças 2026"',
     'alt="Multi Kid Pad NB425 Laranja 10,1 polegadas com capa com alça — opção de tela grande e custo-benefício"'),

    # FIX A — indice quebrado: bloco de avaliacao engolido pelo href do item 10
    ('<span>🔟 <a href="#<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:18px 20px;margin:28px 0;font-size:13.5px;line-height:1.7;color:#334155;">',
     '<span>🔟 <a href="#veredito">Veredito final</a></span>\n'
     '</div>\n'
     '</div>\n'
     '<!-- /wp:html -->\n'
     '\n'
     '<!-- wp:html -->\n'
     '<div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;padding:18px 20px;margin:28px 0;font-size:13.5px;line-height:1.7;color:#334155;">'),

    # FIX B — remover a cauda quebrada: so o resíduo do item 10 apos o bloco de avaliacao
    ('</div>\n</div>\nveredito">Veredito final</a></span>\n</div>\n</div>\n<!-- /wp:html -->',
     '</div>\n</div>'),

        # S36 — badge hero: faixa de preco atual (Tab A9 ate 1.124 em outros meios)
    ('<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">💰 De R$ 499 a R$ 1.299</span>',
     '<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">💰 De R$ 499 a R$ 1.124</span>'),

    # FIM-MARKER
]


def main() -> None:
    text = P.read_text(encoding="utf-8")
    for i, (old, new) in enumerate(REPL, 1):
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"[{i}] old com count={n} (esperado 1):\n{old[:120]!r}")
        text = text.replace(old, new)
    P.write_text(text, encoding="utf-8")
    print(f"OK: {len(REPL)} substituicoes aplicadas em {P.name}")


if __name__ == "__main__":
    main()