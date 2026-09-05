#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-angle Apple TV 4K — aplica todas as edicoes editoriais sobre o raw do WP.
Uso: python3 reangle_apple_tv.py  (restaura do backup, aplica, ancora, valida)"""
import re, json, shutil, sys

RAW = "/home/ubuntu/curadoria-prime-skill-2/articles/wp_raw_backups/4537-apple-tv-4k-pre-reangle-2026-09-04.html"
OUT = "/home/ubuntu/curadoria-prime-skill-2/articles/html_output/apple-tv-4k-reangle-2026-09.html"

shutil.copy(RAW, OUT)
c = open(OUT, encoding="utf-8").read()
n_subs = 0

def conv(s):
    """Converte string do formato 'renderizado' para variantes do 'raw' do WP."""
    return (s.replace("&#8220;", "\u201c").replace("&#8221;", "\u201d")
             .replace("&#8217;", "\u2019")
             .replace('decoding="async" ', "")
             .replace('rel="noopener nofollow"', 'rel="noopener"'))

def conv2(s):
    """Variante com aspas retas (o editor re-salvou o post e o WP normalizou)."""
    return (conv(s).replace("\u201c", '"').replace("\u201d", '"')
            .replace("\u2019", "'"))

def rep(old, new, count=1):
    global c, n_subs
    for fn in (lambda x: x, conv, conv2):
        o2, n2 = fn(old), fn(new)
        if c.count(o2) == count:
            c = c.replace(o2, n2)
            n_subs += 1
            return
    raise AssertionError(f"CONTAGEM {c.count(old)} != {count}: {old[:70]!r}")

# ── PARTE 1: meta, hero, badges, metodologia, prova social ──────────────
rep("""<!-- META DESCRIÇÃO SEO (copiar no Rank Math — 143c · ~845px/920px):
Apple TV 4K vale a pena em 2026? Review com preço real de hoje (R$ 1.505 a R$ 2.804), specs oficiais, comparativo e o alerta da nova geração.
--""",
"""<!-- META DESCRIÇÃO SEO (copiar no Rank Math — 139c · ~820px/920px):
Apple TV 4K: comprar agora ou esperar a nova geração? Evento Apple em 9/9, preço oficial, estoque e veredito com dados de 04/09/2026.
--""")

rep("""Afinal, a <strong style="color:#2997ff;">Apple TV 4K vale a pena</strong> em 2026? Cruzamos <strong>especificações oficiais da Apple, preços reais de 10/08/2026</strong> — de <strong style="color:#2997ff;">R$ 1.505 a R$ 2.804</strong> — e os <strong>rumores da nova geração</strong> (não confirmados) para você decidir: comprar agora ou esperar.""",
"""Afinal, <strong style="color:#2997ff;">comprar a Apple TV 4K agora ou esperar a nova geração?</strong> A Apple confirmou evento para <strong>9 de setembro</strong>, Amazon e catálogo nacional esgotaram e a loja oficial segue a <strong style="color:#2997ff;">R$ 2.499</strong>. Cruzamos ficha oficial, preços verificados em <strong>04/09/2026</strong> e os rumores da 4ª geração (não confirmados) para você decidir.""")

rep("⭐ 4,7/5 em 384 avaliações Amazon", "⭐ 4,7/5 em 383 avaliações Amazon")
rep("⭐ 4,9/5 em 210 opiniões ML", "⭐ 4,9/5 em 220 opiniões ML")
rep("💰 R$ 1.505 a R$ 2.804 (10/08/2026)", "💰 R$ 2.499 nacional (04/09/2026)")
rep("🕒 Atualizado: 10/08/2026", "🕒 Atualizado: 04/09/2026")
rep("(preços verificados nas lojas em 10/08/2026, conteúdo da caixa e condições das ofertas checados na fonte)",
    "(preços verificados nas lojas em 04/09/2026, conteúdo da caixa e condições das ofertas checados na fonte)")
rep("(dados coletados em 10/08/2026 na Amazon e Mercado Livre)", "(dados coletados em 04/09/2026 na Amazon e Mercado Livre)")
rep("⭐ <strong>4,9/5</strong> · <strong>210 opiniões</strong> · +500 vendidos", "⭐ <strong>4,9/5</strong> · <strong>220 opiniões</strong> · +500 vendidos")

# ── PARTE 2: intro, resposta rapida, onde-comprar (cabecalho) ───────────
rep("""E há ainda um terceiro fator, exclusivo de 2026: <strong>a nova geração apontada pelos rumores para setembro</strong>. Vamos por partes. 👇""",
"""E há ainda um terceiro fator, exclusivo deste início de setembro: <strong>a Apple confirmou evento para 9/9</strong> — e a imprensa especializada aponta uma nova Apple TV 4K como uma das apostas da keynote. Vamos por partes. 👇""")

rep("""A imprensa especializada aponta uma <strong>nova geração para a partir de setembro/2026</strong> (chip A17 Pro e Wi-Fi 7 — <em>rumor, não confirmado pela Apple</em>). Se a sua não urgir e você quer o hardware mais novo, aguardar algumas semanas é racional. Detalhes na <a href="#esperar" style="color:#92400e;">seção &#8220;Vale esperar?&#8221;</a>.""",
"""A Apple <strong>confirmou evento para 9 de setembro/2026</strong> (data oficial no site da Apple), e a imprensa especializada aponta uma nova Apple TV 4K como aposta forte da keynote (chip A17 Pro e Wi-Fi 7 — <em>rumor, não confirmado</em>). Se não há urgência, esperar a semana do evento é racional — leva 5 dias. Detalhes na <a href="#esperar" style="color:#92400e;">seção &#8220;Comprar agora ou esperar?&#8221;</a>.""")

rep("🛒 Onde comprar a Apple TV 4K 64GB: os 3 preços reais de hoje", "🛒 Onde comprar a Apple TV 4K 64GB: o mapa real de estoque hoje")

rep("""Preços capturados pelo editor em <strong>10/08/2026</strong> na página oficial Apple, Amazon e Mercado Livre. Apenas a versão <strong>64GB (A2737)</strong> está disponível no varejo hoje — a 128GB está esgotada nos dois marketplaces (detalhes na seção 8).""",
"""Preços capturados em <strong>04/09/2026</strong> na página oficial Apple, Amazon e Mercado Livre. O cenário mudou desde agosto: <strong>a Amazon esgotou o modelo 64GB</strong> (sem previsão de reabastecimento), o catálogo nacional do Mercado Livre ficou <strong>indisponível</strong> e a 128GB segue esgotada. Hoje restam duas rotas reais: a <strong>Apple Store oficial</strong> e uma <strong>oferta internacional no ML</strong> — leia a ressalva de impostos antes. Detalhes na seção 8.""")

# ── PARTE 3: cards de compra (reordenados) ───────────────────────────────
start = c.find('  <!-- Card 1 — Menor preço (ML internacional) -->')
assert start > -1
_h2ficha = c.find('<h2 class="wp-block-heading">📋 Ficha técnica oficial', start)
assert _h2ficha > start
end = c.rfind("<!-- wp:heading", start, _h2ficha)   # corta antes do comentario do heading
assert end > start
assert c[start:end].count('<!-- Card') == 3

new_block = '''  <!-- Card 1 — Apple Store (recomendado) -->
  <div style="background: white; border: 2px solid #1d1d1f; border-radius: 14px; padding: 20px; margin-bottom: 18px;">
    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
      <span style="background: linear-gradient(135deg, #1d1d1f 0%, #000000 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 800; white-space: nowrap;">⭐ Recomendado — única compra segura nacional</span><br>
      <span style="font-weight: bold; color: #1a1f36; font-size: 17px;">Apple Store oficial <span style="font-weight: 400; color: #888; font-size: 14px;">R$ 2.499 | + 3 meses de Apple TV grátis</span></span>
    </div>
    <p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Com a Amazon esgotada e o catálogo nacional do ML fora do ar, a <strong>Apple Brasil é hoje a única loja que vende a 64GB nova com garantia nacional de forma garantida</strong>: <strong>R$ 2.499 em até 12x de R$ 208,25 sem juros</strong>, frete grátis, nota fiscal Apple e — diferencial que ninguém mais oferece — <strong>3 meses de assinatura do Apple TV grátis</strong> (o streaming custa R$ 29,90/mês; resgate em até 90 dias após a compra). Confirmado na página oficial em 04/09/2026. <em>Link direto, sem comissão para nós.</em></p>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
      <a style="background: linear-gradient(135deg, #1d1d1f 0%, #000000 100%); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,0.3);" href="https://www.apple.com/br/shop/buy-tv/apple-tv-4k" target="_blank" rel="noopener">🍎 Ver na Apple Store — R$ 2.499 (12x)</a>
    </div>
  </div>

  <!-- Card 2 — ML internacional com ressalva de impostos -->
  <div style="background: white; border: 2px solid #f59e0b; border-radius: 14px; padding: 20px; margin-bottom: 18px;">
    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
      <span style="background: linear-gradient(135deg, #16a34a 0%, #166534 100%); color: white; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 800; white-space: nowrap;">💰 Menor preço — oferta internacional</span><br>
      <span style="font-weight: bold; color: #1a1f36; font-size: 17px;">Mercado Livre (vendedor dos EUA) <span style="font-weight: 400; color: #888; font-size: 14px;">R$ 1.764,99 no Pix | 4,9★</span></span>
    </div>
    <p style="font-size: 14px; color: #666; margin: 0 0 10px 0;">Única oferta nova com estoque no ML hoje: <strong>R$ 1.764,99 no Pix</strong> (ou R$ 1.774,99 em até 12x), vendida por VYSEGLOBAL-BR, enviada dos EUA com frete grátis e garantia de envio pelo Mercado Livre (Full). Entrega estimada em 13/set. Restam <strong>3 unidades</strong>.</p>
    <div style="background: #fff7ed; border: 1px solid #fed7aa; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #9a3412; margin-bottom: 14px; line-height: 1.55;">
      <strong>⚠️ Leia antes (transparência Curadoria):</strong> o preço anunciado <strong>não inclui os impostos de importação</strong> — a própria página avisa que o produto &#8220;estará sujeito à declaração de importação e a impostos federais e estaduais&#8221;. No regime de importação atual, o total pode passar dos <strong>R$ 3.000</strong> — ou seja, <strong>ficar mais caro que a Apple Store</strong>. Só vale se você aceitar o risco do cálculo final, o prazo maior e a assistência variável. É a mesma Apple TV 4K 3ª geração (A2737), mas não a tratamos como compra segura.
    </div>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
      <a style="background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,0.3);" href="https://meli.la/2RUDQ1f" target="_blank" rel="sponsored noopener noreferrer nofollow">🛍️ Ver no Mercado Livre — R$ 1.764,99 no Pix*</a>
    </div>
    <p style="font-size: 11.5px; color: #9a3412; margin: 8px 0 0 0;">*Preço sem impostos de importação — leia a ressalva acima.</p>
  </div>

  <!-- Card 3 — Amazon esgotada -->
  <div style="background: white; border: 2px solid #e9ecef; border-radius: 14px; padding: 20px;">
    <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
      <span style="background: #fef2f2; color: #991b1b; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 800; white-space: nowrap;">❌ Esgotada — sem data de volta</span><br>
      <span style="font-weight: bold; color: #1a1f36; font-size: 17px;">Amazon Brasil <span style="font-weight: 400; color: #888; font-size: 14px;">&#8220;Não disponível&#8221; (04/09/2026)</span></span>
    </div>
    <p style="font-size: 14px; color: #666; margin: 0;">Em agosto, a Amazon era a segunda rota nacional (R$ 2.299). Hoje o anúncio oficial da 64GB (A2737) está marcado como <strong>&#8220;Não disponível. Não temos previsão de quando este produto estará disponível novamente&#8221;</strong> — e a 128GB segue o mesmo caminho. Não indicamos os anúncios de terceiros com &#8220;mais opções de compra&#8221; porque vendedor, procedência e garantia variam a cada oferta. Se você prefere a Amazon por pontos ou frete Prime, acompanhe o reabastecimento — mas não pague acima da loja oficial por ansiedade de estoque.</p>
  </div>

</div>
<!-- /wp:html -->

'''
c = c[:start] + new_block + c[end:]
n_subs += 1

# ── PARTE 4: secao esperar, comparativo, pros/contras, para quem ────────
rep("⏳ Comprar agora ou esperar a nova Apple TV 4K? (agosto/2026)", "⏳ Comprar agora ou esperar a nova Apple TV 4K? (setembro/2026)")

rep("""Aqui entra o fator que muda a resposta em 2026. <strong>Fato:</strong> a Apple não anunciou nenhuma nova geração até 10/08/2026 — a 3ª geração (out/2022) segue como o modelo atual à venda. <strong>Rumor <em>(não confirmado pela Apple)</em>:</strong> segundo a Bloomberg (Mark Gurman, março/2026), um sucessor com chip <strong>A17 Pro</strong>, novo chip próprio de rede com <strong>Wi-Fi 7, Bluetooth 6 e Thread</strong>, e recursos da nova Siri; a janela mais citada por veículos como MacRumors é <strong>a partir de setembro de 2026</strong>. O preço especulado diverge: de US$ 99–129 (análise de Ming-Chi Kuo) a ~US$ 199–229 (canais de vazamento).""",
"""Aqui entra o fator que muda a resposta nesta semana. <strong>Fato 1:</strong> a Apple <strong>confirmou evento para 9 de setembro de 2026</strong> (10h PT / 14h Brasília, com transmissão no site e no app Apple TV) — o convite oficial está na página de eventos da Apple. <strong>Fato 2:</strong> até 04/09/2026 a Apple não anunciou a nova geração — a 3ª geração (out/2022) segue como modelo atual, e o preço oficial brasileiro não mudou desde o reajuste: R$ 2.499 na loja. <strong>Rumor <em>(não confirmado pela Apple)</em>:</strong> segundo a Bloomberg (Mark Gurman), o sucessor está &#8220;pronto para lançar&#8221;, com chip <strong>A17 Pro</strong>, chip de rede próprio com <strong>Wi-Fi 7, Bluetooth 6 e Thread</strong>, e a nova Siri com Apple Intelligence; veículos como 9to5Mac e MacRumors apontam o evento de 9/9 ou outubro como janelas mais prováveis. O preço especulado nos EUA diverge (US$ 129–199), e a tendência é de manutenção dos US$ 199 após o reajuste de junho.""")

rep("""<strong>Nossa recomendação prática:</strong> precisou agora e achou perto de R$ 1.500 (como a oferta internacional de hoje)? Pode comprar — o aparelho é excelente e seguirá atualizado por anos; se a nova geração sair, o desconto do modelo atual dificilmente cobre meses de espera. Já tem um streamer funcionando e quer o máximo de futuro (Wi-Fi 7, games mais exigentes, Siri inteligente)? Esperar até outubro vale a decisão. O que não recomendamos é pagar <strong>acima de R$ 2.700 no marketplace</strong> faltando semanas para a possível troca de geração — pela mesma razão, a <strong>Apple Store a R$ 2.499</strong> é hoje o teto racional.""",
"""<strong>Nossa recomendação prática, com o evento a 5 dias:</strong> se você <em>pode</em> esperar, espere até 9/9 — não faz sentido comprar às vésperas de a Apple definir o futuro do produto, ainda mais com o estoque nacional apertado (Amazon esgotada, catálogo ML fora do ar). Se a nova geração vier, a 3ª tende a aparecer com desconto em out/nov (Black Friday logo depois); se não vier, você perdeu 5 dias e o aparelho continua excelente. <strong>Precisa agora?</strong> Vá de <strong>Apple Store a R$ 2.499</strong> — é a única rota nacional segura hoje, e o pacote com 3 meses de Apple TV grátis reduz o custo efetivo. <strong>O que não recomendamos:</strong> a oferta internacional &#8220;barata&#8221; de R$ 1.764,99 — sem impostos inclusos, o total real pode superar os R$ 3.000, e você ainda espera até 13/set por um aparelho que pode ser anunciado como &#8220;geração anterior&#8221; na próxima semana.""")

rep("Preço médio (10/08/2026)", "Preço médio (04/09/2026)")
rep("""<tr><td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7; font-weight: 600;">Apple TV 4K 64GB</td><td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7;"><strong>R$ 1.505–2.499</strong> (intl. / Apple Store)</td>""",
"""<tr><td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7; font-weight: 600;">Apple TV 4K 64GB</td><td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7;"><strong>R$ 2.499</strong> (Apple Store; Amazon e catálogo ML esgotados)</td>""")
rep("Faixas de preço de varejo oficial do dia 10/08/2026 (sujeitas a oscilar).", "Faixas de preço de varejo oficial do dia 04/09/2026 (sujeitas a oscilar).")

rep("<li>128GB <strong>esgotada</strong> no varejo nacional nesta data</li>",
    "<li><strong>Estoque nacional apertado</strong>: 64GB esgotada na Amazon e no catálogo ML; 128GB idem</li>")
rep("<li>Nova geração apontada <strong>a partir de set/2026</strong> (rumor) pode rebaixar este modelo</li>",
    "<li>Nova geração pode ser anunciada <strong>já no evento de 9/9</strong> (rumor) e rebaixar este modelo</li>")
rep("<li>Menor preço do varejo hoje é de <strong>oferta importada</strong> (prazo/garantia variam)</li>",
    "<li>Menor preço &#8220;de vitrine&#8221; hoje é <strong>importado sem impostos</strong> — o total real pode superar R$ 3.000</li>")
rep("<li>você pode esperar até <strong>outubro/2026</strong> pela possível nova geração (rumor).</li>",
    "<li>você pode esperar até o <strong>evento de 9/9</strong> — 5 dias — pela possível nova geração (rumor forte).</li>")

# ── PARTE 5: FAQ, escolha rapida, transparencia, fontes ──────────────────
rep("""Sim, para quem está no ecossistema Apple ou quer a experiência mais fluida e limpa de streaming — especialmente encontrando a 64GB perto de R$ 1.500–2.000. Para uso básico, um stick de ~R$ 350 entrega os mesmos apps; e quem pode esperar algumas semanas por uma possível nova geração (rumor de set/2026) deve avaliar aguardar.""",
"""Sim, para quem está no ecossistema Apple ou quer a experiência mais fluida e limpa de streaming. O preço nacional hoje é um só: R$ 2.499 na Apple Store (Amazon e catálogo ML esgotados). Para uso básico, um stick de ~R$ 350 entrega os mesmos apps; e com o evento Apple confirmado para 9/9 — onde uma nova geração é aposta forte (rumor) — quem não tem pressa deve esperar os 5 dias antes de decidir.""", count=2)

rep("""Menor preço absoluto → oferta internacional no ML (com as ressalvas) · Compra segura com brinde → Apple Store · Só precisa dos apps → rival de ~R$ 350 na nossa tabela comparativa.""",
"""Compra segura nacional → Apple Store (única rota hoje) · Arriscar o importado → ML internacional (sem impostos no preço) · Sem pressa → espere o evento de 9/9 antes de decidir.""")

rep("""href="https://meli.la/2RUDQ1f" target="_blank" rel="sponsored noopener noreferrer nofollow">💰 ML — R$ 1.465,85 no Pix</a>""",
"""href="https://meli.la/2RUDQ1f" target="_blank" rel="sponsored noopener noreferrer nofollow">💰 ML intl — R$ 1.764,99 no Pix*</a>""")

rep("""Na Amazon (Loja Apple) hoje: <a style="color:#ffb340; text-decoration: underline;" href="https://link.amazon/B05GgPy4D" target="_blank" rel="sponsored noopener noreferrer nofollow">R$ 2.299,00 em 12x</a> — acima da loja oficial nesta data.""",
"""*Sem impostos de importação. Amazon e catálogo nacional do ML: esgotados em 04/09/2026.""")

rep("Preços verificados em 10/08/2026 e sujeitos a alteração a qualquer momento.",
    "Preços verificados em 04/09/2026 e sujeitos a alteração a qualquer momento.")
rep("<strong>Oficiais Apple</strong> (todas acessadas em 10/08/2026):",
    "<strong>Oficiais Apple</strong> (todas acessadas em 04/09/2026):")
rep("""newsroom BR</a>.</p>""",
"""newsroom BR</a> · <a href="https://www.apple.com/apple-events/" rel="noopener" target="_blank">página oficial de eventos Apple (evento 9/9 confirmado)</a>.</p>""")
rep("""consolidado (jul/2026)</a>""",
"""consolidado (jul/2026)</a> · <a href="https://9to5mac.com/2026-08-27/new-apple-tv-4k-is-coming-four-features-launching-soon/" rel="noopener nofollow" target="_blank">9to5Mac — 4 recursos esperados (ago/2026)</a>""")

i = c.find('<strong>Varejo</strong>')
j = c.find('</p>', i) + 4
old_varejo = c[i:j]
assert '10/08/2026' in old_varejo and 'B0BJN57F96' in old_varejo, old_varejo[:100]
new_varejo = ('<strong>Varejo</strong> (preços/estoque verificados em 04/09/2026): '
  '<a href="https://www.amazon.com.br/dp/B0BJN57F96" rel="sponsored nofollow noopener noreferrer" target="_blank">Amazon — Apple TV 4K 64GB (3ª geração) — esgotada</a> · '
  '<a href="https://www.mercadolivre.com.br/media-player-apple-tv-4k-wi-fi-3rd-gen-64gb-w-siri-remote/p/MLB2045502307" rel="sponsored nofollow noopener noreferrer" target="_blank">Mercado Livre — oferta internacional (impostos não inclusos)</a>.</p>')
rep(old_varejo, new_varejo)

# ── PARTE 6: JSON-LD + scorecard ─────────────────────────────────────────
rep('"description": "Apple TV 4K vale a pena em 2026? Review com preço real de hoje (R$ 1.505 a R$ 2.804), specs oficiais, comparativo e o alerta da nova geração.",',
    '"description": "Apple TV 4K: comprar agora ou esperar a nova geração? Evento Apple em 9/9, preço oficial, estoque e veredito com dados de 04/09/2026.",')
rep('"headline": "Apple TV 4K Vale a Pena em 2026? Review Completo",',
    '"headline": "Apple TV 4K: Comprar Agora ou Esperar a Nova Geração? (2026)",')
rep('{ "@type": "ListItem", "position": 3, "name": "Apple TV 4K Vale a Pena em 2026?" }',
    '{ "@type": "ListItem", "position": 3, "name": "Apple TV 4K: Comprar Agora ou Esperar a Nova Geração?" }')
rep('"datePublished": "2026-08-10T08:00:00-03:00",\n      "dateModified": "2026-08-10T08:00:00-03:00",',
    '"datePublished": "2026-08-10T08:00:00-03:00",\n      "dateModified": "2026-09-25T08:00:00-03:00",')
rep("""          { "@type": "Offer", "priceCurrency": "BRL", "price": "2499.00", "availability": "https://schema.org/InStock", "url": "https://www.apple.com/br/shop/buy-tv/apple-tv-4k", "seller": { "@type": "Organization", "name": "Apple Store Brasil" } },
          { "@type": "Offer", "priceCurrency": "BRL", "price": "2299.00", "availability": "https://schema.org/InStock", "url": "https://www.amazon.com.br/dp/B0BJN57F96", "seller": { "@type": "Organization", "name": "Amazon.com.br" } }""",
"""          { "@type": "Offer", "priceCurrency": "BRL", "price": "2499.00", "availability": "https://schema.org/InStock", "url": "https://www.apple.com/br/shop/buy-tv/apple-tv-4k", "seller": { "@type": "Organization", "name": "Apple Store Brasil" } }""")
rep('"reviewBody": "A melhor experiência de streaming do mercado — fluida, sem anúncios e com o ecossistema Apple completo. Vale a pena para quem tem iPhone/AirPods ou home theater 4K; para uso básico, um stick de R$ 350 resolve. Compre perto de R$ 1.500 ou na Apple Store por R$ 2.499.",',
    '"reviewBody": "A melhor experiência de streaming do mercado — fluida, sem anúncios e com o ecossistema Apple completo. Vale a pena para quem tem iPhone/AirPods ou home theater 4K; para uso básico, um stick de R$ 350 resolve. Com evento Apple confirmado para 9/9 e nova geração apontada como rumor forte, quem não tem pressa deve esperar a keynote; quem precisa agora tem na Apple Store (R$ 2.499) a única compra segura nacional.",')
rep("""<div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Preço alto + geração desconhecida</div>""",
"""<div style="font-size: 12.5px; color: #475569; line-height: 1.5;">R$ 2.499 nacional + evento de 9/9 no radar</div>""")
rep("Régua Curadoria Prime v2.0 (agosto/2026) —", "Régua Curadoria Prime v2.0 —")

# ── PARTE 6b: imagens do re-angle (thumb 5132 / hero 5133) ──────────────
rep('src="https://curadoriaprime.com/wp-content/uploads/2026/07/apple-tv-4k-hero-tv-interface-newsroom.jpg" width="1960" height="1306" fetchpriority="high" alt="Apple TV 4K 3ª geração ligada à TV com a interface tvOS na tela, ao lado do Siri Remote — review vale a pena"',
    'src="https://curadoriaprime.com/wp-content/uploads/2026/09/apple-tv-4k-agora-ou-esperar-hero.jpg" width="970" height="546" fetchpriority="high" alt="Apple TV 4K preta ao lado do Siri Remote prateado — comprar agora ou esperar a nova geração?"')
rep("A Apple TV 4K transforma qualquer TV com HDMI em uma central de streaming 4K — mas ela vale a pena pelo preço? Veja o veredito completo",
    "Apple TV 4K + Siri Remote: comprar agora ou esperar a nova geração que pode sair no evento de 9/9? Veja o veredito completo")
rep('"image": "https://curadoriaprime.com/wp-content/uploads/2026/07/destaque-review-apple-tv-4k-vale-a-pena-2026.jpg",',
    '"image": "https://curadoriaprime.com/wp-content/uploads/2026/09/apple-tv-4k-agora-ou-esperar-destaque.jpg",')

# ── PARTE 6c: funil reforçado para os rivais baratos (edicao do editor 04/09) ──
FIRE = "https://curadoriaprime.com/fire-tv-stick-4k-wifi-6/"

# linha do Fire na tabela comparacao -> link para o review
rep('<td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7; font-weight: 600;">Fire TV Stick 4K / 4K Max</td>',
    f'<td style="padding: 12px 14px; border-bottom: 1px solid #edf2f7; font-weight: 600;"><a href="{FIRE}" rel="noopener" style="color:#1d4ed8;">Fire TV Stick 4K / 4K Max</a></td>')

# "quem NAO e" -> stick linkado
rep("<li>seu uso é <strong>Netflix/YouTube básico</strong> — um stick de ~R$ 350 resolve;</li>",
    f'<li>seu uso é <strong>Netflix/YouTube básico</strong> — um <a href="{FIRE}" rel="noopener" style="color:#1d4ed8;">stick 4K de ~R$ 350</a> resolve (temos review completo);</li>')

# paragrafo apos a tabela -> frase de funil
rep("""a Apple TV é investimento em experiência, não em especificação.""",
    f"""a Apple TV é investimento em experiência, não em especificação. Em nosso <a href="{FIRE}" rel="noopener">review do Fire TV Stick 4K com Wi-Fi 6</a> mostramos por que ele entrega os mesmos apps por um sétimo do preço.""")

# escolha rapida dark -> terceiro botao (editorial, sem sponsored)
rep("""🍎 Apple Store — R$ 2.499 + 3 meses grátis</a>
</div>""",
f"""🍎 Apple Store — R$ 2.499 + 3 meses grátis</a>
<a style="background: transparent; border: 1px solid #5a5a60; color: #fff; text-decoration: none; padding: 13px 22px; border-radius: 8px; font-weight: 800; font-size: 15px;" href="{FIRE}" rel="noopener">🎯 Só quer os apps? Fire Stick 4K →</a>
</div>""")

# FAQ card resposta 1 -> link do rival (so a versao visivel; JSON-LD fica texto puro)
rep("""quem não tem pressa deve esperar os 5 dias antes de decidir.</p>""",
    f"""quem não tem pressa deve esperar os 5 dias antes de decidir. Para uso básico, veja nosso <a href="{FIRE}" rel="noopener">review do Fire TV Stick 4K</a>.</p>""")

# aplicando hoje: dateModified = 04/09
rep('"dateModified": "2026-09-25T08:00:00-03:00",',
    '"dateModified": "2026-09-04T08:00:00-03:00",')

# ── PARTE 7: reordenacao estrutural vs golden ───────────────────────────
# 7a. Mover bloco "Prós e contras" para logo apos o bloco "Onde comprar"
#     (corte comment-aware: inclui o <!-- wp:heading --> de abertura e para
#      antes do comentario do proximo heading)
def block_bounds(c, h2_text):
    i_h2 = c.find(h2_text)
    assert i_h2 > -1, h2_text[:40]
    i_open = c.rfind("<!-- wp:heading", 0, i_h2)
    assert i_open > -1 and i_h2 - i_open < 200
    return i_open, i_h2

i_pros_open, i_pros_h2 = block_bounds(c, '<h2 class="wp-block-heading">✅ Prós e contras da Apple TV 4K</h2>')
i_next_h2 = c.find('<h2 class="wp-block-heading">🎯 Para quem a Apple TV 4K', i_pros_h2)
assert i_next_h2 > i_pros_h2
i_pros_end = c.rfind("<!-- wp:heading", i_pros_h2, i_next_h2)
assert i_pros_end > i_pros_h2
pros_block = c[i_pros_open:i_pros_end]
c = c[:i_pros_open] + c[i_pros_end:]
i_ficha_open, _ = block_bounds(c, '<h2 class="wp-block-heading">📋 Ficha técnica oficial')
c = c[:i_ficha_open] + pros_block.rstrip() + "\n\n" + c[i_ficha_open:]

# 7b. Mover bloco do autor (byline) para depois de "Fontes consultadas"
i_aut = c.find('<div style="display: flex; gap: 16px; align-items: center; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px 20px; margin-bottom: 28px;">')
assert i_aut > -1, "byline nao achado"
i_aut_open = c.rfind("<!-- wp:html", 0, i_aut)
i_fontes_h2 = c.find('<h2 class="wp-block-heading">📚 Fontes consultadas</h2>')
assert i_fontes_h2 > i_aut
byline = c[i_aut_open:i_fontes_h2]
c = c[:i_aut_open] + c[i_fontes_h2:]
# inserir depois do bloco de fontes (div que fecha apos o paragrafo Varejo)
i_fontes_div_end = c.find('</div>', c.find('Mercado Livre — oferta internacional (impostos não inclusos)</a>.</p>'))
assert i_fontes_div_end > -1
i_fontes_close = c.find("<!-- /wp:html -->", i_fontes_div_end)
assert i_fontes_close > -1
i_fontes_close += len("<!-- /wp:html -->")
c = c[:i_fontes_close] + "\n\n" + byline.rstrip() + c[i_fontes_close:]

# ── PARTE 8: anchors do indice (lambda — NUNCA '\\1' em str.replace) ─────
mapping = {
 "resposta-rapida": "⚡ Apple TV 4K vale a pena? Resposta rápida",
 "onde-comprar": "🛒 Onde comprar a Apple TV 4K 64GB",
 "especificacoes": "📋 Ficha técnica oficial",
 "design": "📦 Design e Siri Remote",
 "interface": "📺 Interface e tvOS 26",
 "imagem-som": "🎬 Imagem e som",
 "ecossistema": "🔗 Ecossistema",
 "casa-inteligente": "🧩 64GB ou 128GB",
 "comparativo": "⚖️ Apple TV 4K vs Fire TV Stick",
 "esperar": "⏳ Comprar agora ou esperar",
 "faq": "❓ Perguntas frequentes",
 "veredito": "✅ Veredito final",
}
for anchor, key in mapping.items():
    pat = re.compile(r'<h2 class="wp-block-heading">(' + re.escape(key) + ')')
    hits = pat.findall(c)
    assert len(hits) == 1, f"{key}: {len(hits)} hits"
    c = pat.sub(lambda m, a=anchor: f'<h2 id="{a}" class="wp-block-heading">' + m.group(1), c, count=1)

open(OUT, "w", encoding="utf-8").write(c)

# ── VALIDACAO ────────────────────────────────────────────────────────────
m = re.search(r'<script type="application/ld\+json">(.*?)</script>', c, re.S)
json.loads(m.group(1))
anchors = set(re.findall(r'href="#([^"]+)"', c))
ids = set(re.findall(r'id="([^"]+)"', c))
assert not (anchors - ids), f"anchors quebradas: {anchors - ids}"
assert "\\1" not in c, "residuo de backreference!"
for tag in ["div","table","ul","li","a","p","h2","h3","span"]:
    o = len(re.findall(rf"<{tag}\b", c)); cl = len(re.findall(rf"</{tag}>", c))
    assert o == cl, f"tag {tag} desbalanceada: {o} vs {cl}"
print(f"OK — {n_subs} substituicoes + 12 anchors | {len(c)} chars | JSON-LD valido | tags balanceadas | anchors ok")
