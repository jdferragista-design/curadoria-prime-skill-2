Markdown

# Template REVIEW — Curadoria Prime v2.0

Status: LOCKED
Formato: Gutenberg + HTML inline
Referência visual: Apple TV 4K
Régua: Curadoria Prime v2.0

Este arquivo é a implementação canônica de REVIEW de um produto.

Não é inspiração.

O Agent deve copiar a anatomia e os estilos definidos aqui e preencher
somente os slots variáveis.

---

# REGRAS DE RENDERIZAÇÃO

O Agent DEVE:

- preservar a ordem;
- preservar comentários Gutenberg;
- preservar CSS inline;
- preservar padding, radius, gap, cores funcionais e hierarquia;
- preencher slots somente com dados confirmados;
- remover blocos condicionais quando seu gatilho não existir;
- reconstruir o índice após remover blocos condicionais;
- usar `CP-IMAGE` enquanto a URL do WordPress não existir.

O Agent NÃO pode:

- entregar Markdown como artigo;
- criar `.cp-*`;
- criar `<style>`;
- converter inline CSS para classes;
- modernizar componentes;
- mudar a anatomia;
- copiar dados de exemplos/golden references;
- inventar informação para preencher slot;
- deixar `{{SLOT}}` na entrega pública;
- usar `[IMAGEM AQUI]`;
- inventar URL.

---

# DADOS DE EXEMPLO

Este template NÃO contém dados factuais de produtos.

Qualquer slot precisa ser preenchido com dados provenientes da execução
atual.

Slots vazios não autorizam inferência.

Sem evidência:

- remover componente condicional; ou
- deixar a informação fora do ARTIGO e registrar a pendência na entrega.

---

# ORDEM CANÔNICA

1. META SEO
2. HERO TEXTUAL
3. HERO-01
4. TIPO DE ANÁLISE
5. LEAD / RECORTE
6. METODOLOGIA
7. PROVA SOCIAL
8. ÍNDICE
9. INTRODUÇÃO
10. AFILIADO
11. RESPOSTA RÁPIDA
12. ONDE COMPRAR — TOPO
13. PRÓS E CONTRAS
14. FICHA TÉCNICA
15. SEÇÕES DE DECISÃO
16. TABELA COMPARATIVA
17. COMPRAR OU ESPERAR — condicional
18. PARA QUEM É / NÃO É
19. RÉGUA v2.0
20. FAQ
21. VEREDITO
22. ESCOLHA RÁPIDA
23. CTA FINAL — condicional
24. FONTES
25. UPDATE BOX — condicional
26. BYLINE — condicional
27. AVISO AFILIADO FINAL

THUMB-01 é Featured Image do WordPress.

THUMB-01 NÃO entra no HTML.

---

# 1. META SEO

```html
<!--
META SEO
Título: {{SEO_TITLE}}
Descrição: {{META_DESCRIPTION}}
URL: {{URL}}
Canonical: {{CANONICAL}}
Atualizado: {{UPDATED_DATE}}
-->
Não colocar preço, rating ou informação temporal não confirmada na meta.

2. HERO TEXTUAL — LOCKED
Este é o Hero canônico Apple TV.

Somente estes tokens visuais podem variar:

{{BRAND_PRIMARY}}
{{BRAND_SECONDARY}}
{{BRAND_ACCENT}}
Todo o restante é LOCKED.

HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg,{{BRAND_PRIMARY}} 0%,{{BRAND_SECONDARY}} 100%); color: #fff; padding: 28px 30px; border-radius: 14px; margin-bottom: 30px; font-size: 15.5px; line-height: 1.75;">

<div style="display: inline-block; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); font-size: 11px; font-weight: bold; letter-spacing: .1em; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;">📌 Review Completo — {{YEAR}}</div>

<p style="margin: 0 0 16px; font-size: 18px; font-weight: 600; color: #fff;">{{HERO_LEAD_HTML}}</p>

<div style="display: flex; flex-wrap: wrap; gap: 10px;">
{{HERO_BADGE_AMAZON}}
{{HERO_BADGE_ML}}
{{HERO_BADGE_PRICE}}
<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">🕒 Atualizado: {{UPDATED_DATE}}</span>
</div>

</div>
<!-- /wp:html -->
HERO_LEAD_HTML
O lead pode usar {{BRAND_ACCENT}} apenas nas âncoras principais de
decisão.

Exemplo estrutural, não factual:

HTML

Afinal, o <strong style="color:{{BRAND_ACCENT}};">{{PRODUCT_NAME}}</strong>
vale a pena? Cruzamos {{HERO_EVIDENCE_SUMMARY}} para entender
{{HERO_DECISION_QUESTION}}.
Não usar “testamos a fundo” sem teste físico documentado.

3. BADGES DO HERO
Badge somente quando o dado estiver CONFIRMADO.

Amazon
HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ Amazon: {{AMAZON_RATING}}/5 em {{AMAZON_COUNT}} avaliações</span>
Mercado Livre
HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ Mercado Livre: {{ML_RATING}}/5 em {{ML_COUNT}} opiniões</span>
Preço
HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">💰 {{PRICE_RANGE}} ({{PRICE_DATE_SHORT}})</span>
Sem confirmação:

remover o badge inteiro.

Amazon e ML permanecem separados.

4. HERO-01
Enquanto o editor ainda não enviou a imagem ao WordPress:

HTML

<!-- CP-IMAGE:HERO-01 -->
Depois de APLICAR_IMAGENS:

HTML

<!-- wp:html -->
<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{{HERO_URL}}" alt="{{HERO_ALT}}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; display: block; margin: 0 auto; box-shadow: 0 4px 16px rgba(0,0,0,.14);" fetchpriority="high">
<figcaption style="font-size: 12px; color: #7c7c9a; text-align: center; margin-top: 8px;">{{HERO_CAPTION}}</figcaption>
</figure>
<!-- /wp:html -->
HERO-01 é a única imagem principal inicial do corpo.

Não criar segunda Featured Image dentro do artigo.

5. TIPO DE ANÁLISE
Sem teste físico:

HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13.5px; color: #78350f; line-height: 1.7;">
<strong>📋 Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou esta unidade fisicamente.
</div>
<!-- /wp:html -->
Somente substituir pelo componente de teste próprio quando o
TEST_GATE estiver documentalmente aprovado.

6. LEAD / RECORTE
HTML

<!-- wp:paragraph -->
<p>{{LEAD_PARAGRAPH}}</p>
<!-- /wp:paragraph -->
O lead deve sintetizar:

o que é;
variante;
fatos centrais;
tensão de compra;
preço somente quando confirmado.
Não repetir o Hero palavra por palavra.

7. METODOLOGIA
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13.5px; color: #78350f; line-height: 1.7;">
<strong>📋 Metodologia:</strong> {{METHODOLOGY_SUMMARY}}
<a href="https://curadoriaprime.com/como-avaliamos/" rel="noopener" style="color: {{BRAND_PRIMARY}}; text-decoration: underline; font-weight: 600;">Veja como avaliamos e calculamos as notas →</a>
</div>
<!-- /wp:html -->
Não afirmar que milhares de avaliações foram analisadas apenas porque a
plataforma exibe milhares de ratings.

8. PROVA SOCIAL — CONDICIONAL
Renderizar somente com evidência.

Padrão preferencial:

2 Amazon + 2 Mercado Livre.

Não é quota.

HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">

<p style="margin: 0 0 14px; font-size: 16px; font-weight: 700; color: #1e293b;">🗣️ O que dizem os compradores <span style="font-size: 12px; font-weight: 400; color: #64748b;">(consulta em {{SOCIAL_DATE}})</span></p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
{{SOCIAL_CARDS}}
</div>

</div>
<!-- /wp:html -->
Card Amazon
HTML

<div style="background: #fff; border: 1px solid #ffd499; border-left: 4px solid #FF9900; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #FF9900;">Amazon — {{MARKETPLACE_VARIANT}}</strong><br>
⭐ <strong>{{MARKETPLACE_RATING}}/5</strong> · <strong>{{MARKETPLACE_COUNT}} avaliações</strong><br>
{{MARKETPLACE_REVIEW_BODY}}
</div>
Card Mercado Livre
HTML

<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #3485DB;">Mercado Livre — {{MARKETPLACE_VARIANT}}</strong><br>
⭐ <strong>{{MARKETPLACE_RATING}}/5</strong> · <strong>{{MARKETPLACE_COUNT}} opiniões</strong><br>
{{MARKETPLACE_REVIEW_BODY}}
</div>
Citação:

somente literal/verificável.

Paráfrase:

usar síntese editorial sem aspas.

Relato LOGÍSTICA/VENDEDOR não sustenta qualidade do produto.

9. ÍNDICE
Montar somente depois de decidir quais blocos condicionais serão
renderizados.

HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 30px;">
<p style="font-size: 15px; font-weight: 800; color: #1a1a2e; margin: 0 0 14px;">📑 Índice de Conteúdo</p>
<ol style="margin: 0; padding-left: 22px; line-height: 1.8;">
{{INDEX_ITEMS}}
</ol>
</div>
<!-- /wp:html -->
Nunca apontar para âncora inexistente.

10. INTRODUÇÃO
HTML

<!-- wp:heading {"anchor":"intro"} -->
<h2 id="intro" class="wp-block-heading">{{INTRO_HEADING}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{INTRO_PARAGRAPH_1}}</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>{{INTRO_PARAGRAPH_2}}</p>
<!-- /wp:paragraph -->
Responder à decisão rapidamente.

Sem introdução genérica para aumentar comprimento.

11. AVISO DE AFILIADO
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
<strong>⚠️ Transparência:</strong> este artigo contém links de afiliado. Se você comprar por meio deles, a Curadoria Prime pode receber uma comissão, sem custo adicional para você. Isso não altera nossos critérios editoriais. Preços e estoque podem mudar; confirme na loja.
</div>
<!-- /wp:html -->
12. RESPOSTA RÁPIDA — LOCKED
HTML

<!-- wp:heading {"anchor":"resposta-rapida"} -->
<h2 id="resposta-rapida" class="wp-block-heading">⚡ Resposta rápida</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.6;">
<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#166534;">✅ Vale se...</p>
<p style="margin:0;">{{QUICK_YES}}</p>
</div>

<div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.6;">
<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#1e40af;">🤔 Depende se...</p>
<p style="margin:0;">{{QUICK_DEPENDS}}</p>
</div>

<div style="background: #fffbeb; border: 2px solid #f59e0b; border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.6;">
<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#92400e;">⏳ Pode esperar se...</p>
<p style="margin:0;">{{QUICK_WAIT}}</p>
</div>

</div>
<!-- /wp:html -->
Decisão → condição → detalhe.

Não usar preço gigante aqui.

13. ONDE COMPRAR — TOPO — CONDICIONAL
Somente depois de MARKET_GATE.

HTML

<!-- wp:heading {"anchor":"onde-comprar"} -->
<h2 id="onde-comprar" class="wp-block-heading">🛒 Onde comprar</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: white; border: 1px solid #e9ecef; border-radius: 20px; padding: 35px 25px; margin-top: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">

<h3 style="text-align: center; color: #2d3277; font-size: 22px; margin: 0 0 30px 0;">🛒 Onde comprar: preços verificados em {{MARKET_DATE}}</h3>

{{BUY_CARDS}}

</div>
<!-- /wp:html -->
Cards são empilhados.

Não criar três colunas.

14. CARD DE COMPRA — ESTRUTURA
HTML

<div style="background: white; border: 2px solid {{BUY_CARD_BORDER}}; border-radius: 14px; padding: 20px; margin-bottom: 18px;">

<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 8px;">
<span style="{{BUY_CARD_PILL_STYLE}}">{{BUY_CARD_PILL}}</span>
<span style="font-weight: bold; color: #1a1f36; font-size: 17px;">{{BUY_CARD_TITLE}} <span style="font-weight: 400; color: #888; font-size: 14px;">{{BUY_CARD_META}}</span></span>
</div>

{{BUY_CARD_IMAGE}}

<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">{{BUY_CARD_ARGUMENT}}</p>

{{BUY_CARD_ALERT}}

<div style="display: flex; gap: 10px; flex-wrap: wrap;">
{{BUY_CARD_CTAS}}
</div>

</div>
Foto somente quando prevista.

Para produtos grandes, seguir limites definidos em layout-apple-tv.md.

15. CTA AMAZON — LOCKED
HTML

<a style="background: linear-gradient(135deg, #ff9900, #ff8500); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(255,150,0,.3);" href="{{AMAZON_AFFILIATE_URL}}" target="_blank" rel="sponsored nofollow noopener noreferrer">Ver na Amazon{{AMAZON_PRICE_LABEL}}</a>
Sem URL confirmada:

não renderizar.

16. CTA MERCADO LIVRE — LOCKED
HTML

<a style="background: linear-gradient(135deg, #2d3277, #1a1f5c); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,.3);" href="{{ML_AFFILIATE_URL}}" target="_blank" rel="sponsored nofollow noopener noreferrer">Ver no Mercado Livre{{ML_PRICE_LABEL}}</a>
17. CTA OFICIAL GENÉRICO
HTML

<a style="background: linear-gradient(135deg, #111827, #030712); color: #fff; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(0,0,0,.25);" href="{{OFFICIAL_URL}}" target="_blank" rel="noopener noreferrer">Ver na loja oficial{{OFFICIAL_PRICE_LABEL}}</a>
Não marcar sponsored quando não houver relação patrocinada.

18. PRÓS E CONTRAS — LOCKED
HTML

<!-- wp:heading {"anchor":"pros-contras"} -->
<h2 id="pros-contras" class="wp-block-heading">✅ Prós e contras</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 24px;">
<h3 style="margin: 0 0 16px 0; font-size: 18px; color: #166534; display: flex; align-items: center; gap: 8px;"><span style="font-size: 24px;">✅</span> Pontos Positivos</h3>
<ul style="list-style: none; padding: 0; margin: 0;">
{{POSITIVE_ITEMS}}
</ul>
</div>

<div style="background: #fef2f2; border: 2px solid #ef4444; border-radius: 12px; padding: 24px;">
<h3 style="margin: 0 0 16px 0; font-size: 18px; color: #991b1b; display: flex; align-items: center; gap: 8px;"><span style="font-size: 24px;">❌</span> Pontos Negativos</h3>
<ul style="list-style: none; padding: 0; margin: 0;">
{{NEGATIVE_ITEMS}}
</ul>
</div>

</div>
<!-- /wp:html -->
Item positivo intermediário:

HTML

<li style="padding: 10px 0; border-bottom: 1px solid #bbf7d0; font-size: 14.5px; line-height: 1.6;">{{ITEM}}</li>
Último positivo:

HTML

<li style="padding: 10px 0; font-size: 14.5px; line-height: 1.6;">{{ITEM}}</li>
Item negativo intermediário:

HTML

<li style="padding: 10px 0; border-bottom: 1px solid #fecaca; font-size: 14.5px; line-height: 1.6;">{{ITEM}}</li>
Último negativo:

HTML

<li style="padding: 10px 0; font-size: 14.5px; line-height: 1.6;">{{ITEM}}</li>
Não há quota de itens.

19. FICHA TÉCNICA
HTML

<!-- wp:heading {"anchor":"especificacoes"} -->
<h2 id="especificacoes" class="wp-block-heading">📋 Especificações técnicas</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="overflow-x: auto; margin-bottom: 28px;">

<table style="width: 100%; border-collapse: collapse; font-size: 13.5px; min-width: 640px;">

<thead>
<tr style="background: {{TABLE_HEADER}}; color: #fff;">
<th style="padding: 12px 14px; text-align: left;">Especificação</th>
<th style="padding: 12px 14px; text-align: left;">Detalhe</th>
<th style="padding: 12px 14px; text-align: left;">Fonte</th>
</tr>
</thead>

<tbody>
{{SPEC_ROWS}}
</tbody>

</table>
</div>
<!-- /wp:html -->
Somente dados confirmados.

20. LINHAS DA FICHA
Alternar zebra.

HTML

<tr style="background: #f8fafc;">
<td style="padding: 11px 14px;"><strong>{{SPEC_NAME}}</strong></td>
<td style="padding: 11px 14px;">{{SPEC_VALUE}}</td>
<td style="padding: 11px 14px;">{{SPEC_SOURCE}}</td>
</tr>
e:

HTML

<tr style="background: #fff;">
<td style="padding: 11px 14px;"><strong>{{SPEC_NAME}}</strong></td>
<td style="padding: 11px 14px;">{{SPEC_VALUE}}</td>
<td style="padding: 11px 14px;">{{SPEC_SOURCE}}</td>
</tr>
21. SEÇÕES DE DECISÃO
Para cada eixo:

HTML

<!-- wp:heading {"anchor":"{{AXIS_ID}}"} -->
<h2 id="{{AXIS_ID}}" class="wp-block-heading">{{AXIS_TITLE}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{AXIS_PARAGRAPH_1}}</p>
<!-- /wp:paragraph -->

<!-- CP-IMAGE:{{OPTIONAL_IMAGE_ID}} -->

<!-- wp:paragraph -->
<p>{{AXIS_PARAGRAPH_2}}</p>
<!-- /wp:paragraph -->
A imagem intermediária é opcional.

Se não houver imagem:

remover marcador.

Não criar espaço vazio.

22. TABELA COMPARATIVA — LOCKED
Usar comparação lado a lado por critério.

HTML

<!-- wp:heading {"anchor":"comparativo"} -->
<h2 id="comparativo" class="wp-block-heading">📊 Tabela comparativa: {{COMPARISON_TITLE}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Dados verificados em {{COMPARISON_DATE}} — preços e estoque sujeitos a alteração. Sempre confira antes de comprar.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="overflow-x: auto; margin-bottom: 28px;">

<table style="width: 100%; border-collapse: collapse; font-size: 13.5px; min-width: 640px;">

<thead>
<tr style="background: {{TABLE_HEADER}}; color: #fff;">
<th style="padding: 12px 14px; text-align: left; border-radius: 8px 0 0 0;">Critério</th>
{{COMPARISON_HEADERS}}
</tr>
</thead>

<tbody>
{{COMPARISON_ROWS}}
</tbody>

</table>
</div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Fonte:</strong> {{COMPARISON_SOURCE_SUMMARY}}</p>
<!-- /wp:paragraph -->
23. HEADER DE PRODUTO NA COMPARAÇÃO
HTML

<th style="padding: 12px 14px; text-align: center;">{{PRODUCT_SHORT}}</th>
Último header pode receber:

HTML

<th style="padding: 12px 14px; text-align: center; border-radius: 0 8px 0 0;">{{PRODUCT_SHORT}}</th>
24. LINHAS DA COMPARAÇÃO
Zebra A:

HTML

<tr style="background: #f8fafc;">
{{COMPARISON_CELLS}}
</tr>
Zebra B:

HTML

<tr style="background: #fff;">
{{COMPARISON_CELLS}}
</tr>
Primeira célula:

HTML

<td style="padding: 11px 14px;"><strong>{{CRITERION}}</strong></td>
Produto:

HTML

<td style="padding: 11px 14px; text-align: center;">{{VALUE}}</td>
Vantagem comprovada:

HTML

<td style="padding: 11px 14px; text-align: center;"><strong>{{VALUE}} ✅</strong></td>
✅ somente com vantagem factual defensável.

25. COMPRAR AGORA OU ESPERAR — CONDICIONAL
Somente quando houver:

nova geração;
rumor relevante;
sucessor;
transição de mercado.
HTML

<!-- wp:heading {"anchor":"esperar"} -->
<h2 id="esperar" class="wp-block-heading">⏳ Comprar agora ou esperar?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{BUY_OR_WAIT_TEXT}}</p>
<!-- /wp:paragraph -->
Rumor precisa de:

palavra rumor;
veículo;
data.
26. PARA QUEM É / NÃO É
HTML

<!-- wp:heading {"anchor":"para-quem"} -->
<h2 id="para-quem" class="wp-block-heading">🎯 Para quem é — e para quem não é</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #166534;">✅ Pode ser uma boa escolha se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7; color: #475569;">
{{WHO_YES_ITEMS}}
</ul>
</div>

<div style="background: #fef2f2; border: 2px solid #ef4444; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #991b1b;">❌ Pode não ser a melhor escolha se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7; color: #475569;">
{{WHO_NO_ITEMS}}
</ul>
</div>

</div>
<!-- /wp:html -->
27. RÉGUA v2.0 — CONDICIONAL
Renderizar somente quando RATING_GATE passa.

Os critérios são sempre:

Custo-benefício — 30%
Satisfação verificada — 25%
Ficha técnica — 20%
Recursos e usabilidade — 10%
Consenso técnico — 10%
Confiança e suporte — 5%
HTML

<!-- wp:heading {"anchor":"notas"} -->
<h2 id="notas" class="wp-block-heading">📊 Notas por categoria</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-bottom: 16px;">
{{RATING_CARDS}}
</div>

<div style="background: linear-gradient(135deg,{{BRAND_PRIMARY}} 0%,{{BRAND_SECONDARY}} 100%); border-radius: 10px; padding: 16px 20px; margin-top: 16px; text-align: center;">
<p style="font-size: 13px; color: rgba(255,255,255,.8); margin: 0 0 4px; text-transform: uppercase; letter-spacing: .08em; font-weight: bold;">Nota Geral</p>
<p style="font-size: 36px; font-weight: 800; color: #fff; margin: 0;">{{FINAL_RATING}}<span style="font-size: 18px; color: rgba(255,255,255,.6);">/10</span></p>
<p style="font-size: 14px; color: #fff; margin: 6px 0 0;">{{RATING_SEAL}}</p>
</div>

<p style="text-align: center; font-size: 13px; margin-top: 12px;">
Pontuação calculada pela <strong>Régua Curadoria Prime v2.0</strong>.
<a href="https://curadoriaprime.com/como-avaliamos/" rel="noopener" style="color: {{BRAND_PRIMARY}}; font-weight: 600;">Veja a metodologia e os pesos →</a>
</p>
<!-- /wp:html -->
Em telas pequenas, se o tema não reflowar adequadamente esse grid,
o template poderá usar auto-fit após aprovação explícita do editor.
Não alterar durante geração comum.

28. CARD DA RÉGUA
HTML

<div style="background: #f5f5fb; border-radius: 10px; padding: 14px 16px; text-align: center;">

<p style="font-size: 12px; color: #7c7c9a; margin: 0 0 6px; font-weight: bold; text-transform: uppercase; letter-spacing: .06em;">{{CRITERION}} · {{WEIGHT}}</p>

<p style="font-size: 22px; font-weight: 800; color: {{RATING_COLOR}}; margin: 0 0 6px;">{{RATING}}<span style="font-size: 14px; color: #7c7c9a;">/10</span></p>

<p style="font-size: 12.5px; color: #64748b; line-height: 1.5; margin: 0;">{{REASON}}</p>

</div>
Nota somente em múltiplos de 0,5.

29. FAQ — LOCKED
Não usar <details>.

HTML

<!-- wp:heading {"anchor":"faq"} -->
<h2 id="faq" class="wp-block-heading">❓ Perguntas frequentes</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="margin-bottom: 28px;">
{{FAQ_CARDS}}
</div>
<!-- /wp:html -->
Card:

HTML

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px;">
<p style="margin: 0 0 8px; font-weight: 700; font-size: 14.5px;">{{NUMBER}}. {{QUESTION}}</p>
<p style="margin: 0; font-size: 14px; line-height: 1.65;">{{ANSWER}}</p>
</div>
Quantidade:

6–10 quando houver perguntas úteis suficientes.

30. VEREDITO
HTML

<!-- wp:heading {"anchor":"veredito"} -->
<h2 id="veredito" class="wp-block-heading">✅ Veredito final: {{VERDICT_HEADING}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{VERDICT_TEXT}}</p>
<!-- /wp:paragraph -->
Precisa responder:

para quem;
principal força;
principal limitação;
faixa de preço;
rival relevante.
31. ESCOLHA RÁPIDA
HTML

<!-- wp:heading {"anchor":"escolha-rapida"} -->
<h2 id="escolha-rapida" class="wp-block-heading">⚡ Escolha rápida: 3 cenários</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">
{{QUICK_CHOICE_CARDS}}
</div>
<!-- /wp:html -->
Cada card deve representar cenário diferente.

32. CARD ESCOLHA RÁPIDA
Verde:

HTML

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px; text-align: center;">
<p style="font-size: 28px; margin: 0 0 8px;">{{ICON}}</p>
<p style="font-weight: 700; color: #166534; font-size: 16px; margin: 0 0 8px;">{{TITLE}}</p>
<p style="font-size: 14px; color: #475569; margin: 0;">{{TEXT}}</p>
</div>
Azul:

usar #eff6ff / #3b82f6 / #1e40af.

Âmbar:

usar #fffbeb / #f59e0b / #92400e.

33. CTA FINAL — CONDICIONAL
Somente quando MARKET_GATE passou.

Reutilizar:

cards de compra;
CTAs Amazon;
CTAs ML;
CTA oficial.
Não criar componente novo no final.

34. FONTES — LOCKED
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin: 24px 0; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📚 Fontes consultadas nesta análise:</strong><br>
{{SOURCE_LINKS}}
</div>
<!-- /wp:html -->
Agrupar conceitualmente:

oficiais;
independentes;
varejo;
rumores.
Toda URL deve ser real.

35. UPDATE BOX — CONDICIONAL
Somente atualização real/substancial quando aplicável.

HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📌 Última atualização:</strong> {{UPDATED_DATE}} |
<strong>Produto em análise:</strong> {{PRODUCT_MODEL_SKU}}<br>
<strong>⚠️ Aviso:</strong> {{TEMPORAL_NOTICE}}
</div>
<!-- /wp:html -->
36. BYLINE — CONDICIONAL
Renderizar somente quando:

AUTHOR_APPROVED = SIM

A IA não escreve bio nova.

O conteúdo do byline deve vir de fragmento canônico previamente aprovado.

Estrutura visual:

HTML

<!-- wp:html -->
<div style="display: flex; gap: 16px; align-items: center; flex-wrap: wrap; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px 20px; margin-bottom: 28px;">
{{APPROVED_AUTHOR_FRAGMENT}}
</div>
<!-- /wp:html -->
Sem AUTHOR_APPROVED:

remover bloco.

37. AVISO AFILIADO FINAL
HTML

<!-- wp:html -->
<div style="background: #f8fafc; border-top: 3px solid {{BRAND_PRIMARY}}; border-radius: 0 0 10px 10px; padding: 14px 18px; font-size: 12.5px; color: #64748b; line-height: 1.6;">
<strong>Aviso de afiliado:</strong> o Curadoria Prime participa de programas de afiliados. Compras feitas por links desta página podem gerar comissão ao site, sem custo adicional para você. Isso não altera nossos critérios editoriais. Preços e disponibilidade podem mudar.
</div>
<!-- /wp:html -->
38. RELATÓRIO DE IMAGENS
Este relatório fica FORA do ARTIGO HTML.

No mínimo:

THUMB-01
HERO-01

Adicionar IMG-01 etc. quando necessário.

Formato:

ID:
USO:
ENTRA NO HTML:
TIPO:
POSIÇÃO EXATA:
MARCADOR HTML:
OBJETIVO:
PRODUTO:
MODELO/SKU:
O QUE BUSCAR/COMPOR:
FONTE PREFERENCIAL:
ORIENTAÇÃO:
ALT:
LEGENDA:
OBRIGATÓRIA:
OBSERVAÇÕES:

39. THUMB-01
Uso:

Featured Image do WordPress.

Não inserir no HTML.

40. BLOQUEIO FINAL
Antes de entregar ARTIGO HTML, confirmar:

nenhum {{SLOT}} não resolvido;
nenhum [IMAGEM AQUI];
nenhuma URL placeholder;
nenhum preço sem Market Gate;
nenhuma nota sem Rating Gate;
nenhum comprador inventado;
nenhuma citação inventada;
nenhum dado copiado de exemplo;
nenhum Markdown no artigo;
nenhuma classe visual inventada;
nenhuma segunda imagem principal;
nenhuma alteração da estrutura LOCKED.
Exceção:

<!-- CP-IMAGE:ID -->

pode permanecer enquanto a imagem aguarda upload no WordPress.

O artigo entregue nesse estado é:

PRONTO PARA REVISÃO HUMANA

e não:

PRONTO PARA PUBLICAÇÃO.

text


Esse é o conteúdo que deve estar em `assets/template-review.md`.

O `template-guia.md` não deve receber isso. Ele deve ficar deprecated/ponte, ou ser removido depois que você confirmar que nenhuma referência ativa ainda aponta para ele.

Há também um ajuste que recomendo no `SKILL.md`: onde ele diz “templates”, deixe somente:

```text
REVIEW → assets/template-review.md
VS → assets/template-vs.md
LISTA/GUIA → assets/template-lista.md
