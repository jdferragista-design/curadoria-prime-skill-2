Markdown

# Template REVIEW — Curadoria Prime v2.0

Status: LOCKED
Formato: Gutenberg + HTML inline
Referência visual: Apple TV 4K
Régua: v2.0

Este template é implementação, não inspiração.

O Agent:

- preserva estrutura;
- preserva inline CSS;
- preenche slots;
- remove componentes condicionais sem evidência.

O Agent NÃO:

- converte para Markdown;
- cria `.cp-*`;
- cria stylesheet;
- muda radius/padding/gap;
- inventa dado para preencher slot.

Nenhum `{{SLOT}}` pode aparecer na entrega pública.

---

## 1. META SEO INTERNA

```html
<!--
META SEO
Título: {{SEO_TITLE}}
Descrição: {{META_DESCRIPTION}}
URL: {{URL}}
Atualizado: {{UPDATED_DATE}}
-->
Dados não confirmados não entram na meta.

2. HERO TEXTUAL — LOCKED
HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg,{{BRAND_PRIMARY}} 0%,{{BRAND_SECONDARY}} 100%); color: #fff; padding: 28px 30px; border-radius: 14px; margin-bottom: 30px; font-size: 15.5px; line-height: 1.75;">

<div style="display: inline-block; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); font-size: 11px; font-weight: bold; letter-spacing: .1em; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;">📌 Review Completo — {{YEAR}}</div>

<p style="margin: 0 0 16px; font-size: 18px; font-weight: 600; color: #fff;">
{{HERO_LEAD_HTML}}
</p>

<div style="display: flex; flex-wrap: wrap; gap: 10px;">

{{HERO_BADGE_AMAZON}}

{{HERO_BADGE_ML}}

{{HERO_BADGE_PRICE}}

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">🕒 Atualizado: {{UPDATED_DATE}}</span>

</div>
</div>
<!-- /wp:html -->
Badge Amazon
Somente se confirmado:

HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ Amazon: {{AMAZON_RATING}}/5 em {{AMAZON_COUNT}} avaliações</span>
Badge ML
HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ Mercado Livre: {{ML_RATING}}/5 em {{ML_COUNT}} opiniões</span>
Badge preço
HTML

<span style="background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); padding: 6px 14px; border-radius: 100px; font-size: 13px;">💰 {{PRICE_RANGE}} ({{PRICE_DATE_SHORT}})</span>
Sem dado confirmado:

remover o badge inteiro.

3. HERO-01
Enquanto aguarda WordPress:

HTML

<!-- CP-IMAGE:HERO-01 -->
Quando aplicado, usar o componente de imagem aprovado:

HTML

<!-- wp:html -->
<figure style="margin: 0 0 25px 0; text-align: center;">
<img src="{{HERO_URL}}" alt="{{HERO_ALT}}" style="width: 100%; max-width: 1000px; height: auto; border-radius: 12px; display: block; margin: 0 auto; box-shadow: 0 4px 16px rgba(0,0,0,.14);" fetchpriority="high">
<figcaption style="font-size: 12px; color: #7c7c9a; text-align: center; margin-top: 8px;">{{HERO_CAPTION}}</figcaption>
</figure>
<!-- /wp:html -->
THUMB-01 nunca entra aqui.

4. TIPO DE ANÁLISE
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13.5px; color: #78350f; line-height: 1.7;">
<strong>📋 Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou esta unidade fisicamente.
</div>
<!-- /wp:html -->
Somente substituir por versão de teste próprio se houver documentação
válida.

5. METODOLOGIA
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13.5px; color: #78350f; line-height: 1.7;">
<strong>📋 Metodologia:</strong> {{METHODOLOGY_SUMMARY}}
<a href="https://curadoriaprime.com/como-avaliamos/" rel="noopener" style="color: {{BRAND_PRIMARY}}; text-decoration: underline; font-weight: 600;">Veja como avaliamos e calculamos as notas →</a>
</div>
<!-- /wp:html -->
6. PROVA SOCIAL
Somente com evidência.

HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">

<p style="margin: 0 0 14px; font-size: 16px; font-weight: 700; color: #1e293b;">
🗣️ O que dizem os compradores
<span style="font-size: 12px; font-weight: 400; color: #64748b;">(consulta em {{SOCIAL_DATE}})</span>
</p>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">

{{SOCIAL_CARD_1}}
{{SOCIAL_CARD_2}}
{{SOCIAL_CARD_3}}
{{SOCIAL_CARD_4}}

</div>
</div>
<!-- /wp:html -->
Amazon:

HTML

<div style="background: #fff; border: 1px solid #ffd499; border-left: 4px solid #FF9900; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #FF9900;">Amazon — {{VARIANT}}</strong><br>
⭐ <strong>{{RATING}}/5</strong> · <strong>{{COUNT}} avaliações</strong><br>
{{REVIEW_OR_SYNTHESIS}}
</div>
ML:

HTML

<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #3485DB;">Mercado Livre — {{VARIANT}}</strong><br>
⭐ <strong>{{RATING}}/5</strong> · <strong>{{COUNT}} opiniões</strong><br>
{{REVIEW_OR_SYNTHESIS}}
</div>
Nunca preencher card sem evidência.

7. ÍNDICE
Usar somente âncoras de seções realmente renderizadas.

HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 30px;">
<p style="font-size: 15px; font-weight: 800; color: #1a1a2e; margin: 0 0 14px;">📑 Índice de Conteúdo</p>
<ol style="margin: 0; padding-left: 22px; line-height: 1.8;">
{{INDEX_ITEMS}}
</ol>
</div>
<!-- /wp:html -->
8. INTRODUÇÃO
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
Sem repetição artificial.

9. AFILIADO
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
<strong>⚠️ Transparência:</strong> este artigo contém links de afiliado. Se você comprar por meio deles, a Curadoria Prime pode receber uma comissão, sem custo adicional para você. Isso não altera nossos critérios editoriais. Preços e estoque podem mudar; confirme na loja.
</div>
<!-- /wp:html -->
10. RESPOSTA RÁPIDA
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
11. ONDE COMPRAR — TOPO
Renderizar somente após MARKET_GATE.

Cards empilhados.

HTML

<!-- wp:html -->
<div style="background: white; border: 1px solid #e9ecef; border-radius: 20px; padding: 35px 25px; margin-top: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">

<h3 style="text-align: center; color: #2d3277; font-size: 22px; margin: 0 0 30px 0;">🛒 Onde comprar</h3>

{{BUY_CARD_1}}
{{BUY_CARD_2}}
{{BUY_CARD_3}}

</div>
<!-- /wp:html -->
Cada card segue o componente canônico definido no modelo.

CTA Amazon:

HTML

<a style="background: linear-gradient(135deg, #ff9900, #ff8500); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(255,150,0,.3);" href="{{AMAZON_AFFILIATE_URL}}" target="_blank" rel="sponsored nofollow noopener noreferrer">Ver na Amazon{{OPTIONAL_PRICE}}</a>
CTA ML:

HTML

<a style="background: linear-gradient(135deg, #2d3277, #1a1f5c); color: #ffe600; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,.3);" href="{{ML_AFFILIATE_URL}}" target="_blank" rel="sponsored nofollow noopener noreferrer">Ver no Mercado Livre{{OPTIONAL_PRICE}}</a>
12. PRÓS E CONTRAS — LOCKED
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
Negativo:

HTML

<li style="padding: 10px 0; border-bottom: 1px solid #fecaca; font-size: 14.5px; line-height: 1.6;">{{ITEM}}</li>
Último item remove border-bottom.

13. FICHA TÉCNICA
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
14. SEÇÕES DE DECISÃO
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
Não criar imagem quando não acrescentar informação.

15. TABELA COMPARATIVA — LOCKED
HTML

<!-- wp:heading {"anchor":"comparativo"} -->
<h2 id="comparativo" class="wp-block-heading">📊 Tabela comparativa: {{COMPARISON_TITLE}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Dados verificados em {{COMPARISON_DATE}}. Preços e estoque podem mudar; confira antes de comprar.</p>
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
Linha zebra A:

HTML

<tr style="background: #f8fafc;">
...
</tr>
Linha B:

HTML

<tr style="background: #fff;">
...
</tr>
Não inventar ✅.

16. COMPRAR OU ESPERAR — CONDITIONAL
Só quando houver questão real de geração/rumor.

HTML

<!-- wp:heading {"anchor":"esperar"} -->
<h2 id="esperar" class="wp-block-heading">⏳ Comprar agora ou esperar?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{BUY_OR_WAIT_TEXT}}</p>
<!-- /wp:paragraph -->
Rumor sempre atribuído.

17. PARA QUEM É / NÃO É
HTML

<!-- wp:heading {"anchor":"para-quem"} -->
<h2 id="para-quem" class="wp-block-heading">🎯 Para quem é — e para quem não é</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">

<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px; font-size: 16px; color: #166534;">✅ Pode ser uma boa escolha se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7; color: #475569;">
{{WHO_YES_ITEMS}}
</ul>
</div>

<div style="background: #fef2f2; border: 2px solid #ef4444; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px; font-size: 16px; color: #991b1b;">❌ Pode não ser a melhor escolha se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7; color: #475569;">
{{WHO_NO_ITEMS}}
</ul>
</div>

</div>
<!-- /wp:html -->
18. RÉGUA v2.0 — GRID 3×2
Somente quando RATING_GATE passa.

HTML

<!-- wp:heading {"anchor":"notas"} -->
<h2 id="notas" class="wp-block-heading">📊 Notas por categoria</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; margin-bottom: 16px;">
{{RATING_CARDS}}
</div>

<div style="background: linear-gradient(135deg,{{BRAND_PRIMARY}} 0%,{{BRAND_SECONDARY}} 100%); border-radius: 10px; padding: 16px 20px; margin-top: 16px; text-align: center;">
<p style="font-size: 13px; color: rgba(255,255,255,.8); margin: 0 0 4px; text-transform: uppercase; letter-spacing: .08em; font-weight: bold;">Nota Geral</p>
<p style="font-size: 36px; font-weight: 800; color: #fff; margin: 0;">{{FINAL_RATING}}<span style="font-size: 18px; color: rgba(255,255,255,.6);">/10</span></p>
<p style="font-size: 14px; color: #fff; margin: 6px 0 0;">{{RATING_SEAL}}</p>
</div>

<p style="text-align:center;font-size:13px;margin-top:12px;">
Pontuação calculada pela <strong>Régua Curadoria Prime v2.0</strong>.
<a href="https://curadoriaprime.com/como-avaliamos/" rel="noopener" style="color:{{BRAND_PRIMARY}};font-weight:600;">Veja a metodologia e os pesos →</a>
</p>
<!-- /wp:html -->
Cada card:

HTML

<div style="background: #f5f5fb; border-radius: 10px; padding: 14px 16px; text-align: center;">
<p style="font-size: 12px; color: #7c7c9a; margin: 0 0 6px; font-weight: bold; text-transform: uppercase; letter-spacing: .06em;">{{CRITERION}} · {{WEIGHT}}</p>
<p style="font-size: 22px; font-weight: 800; color: {{RATING_COLOR}}; margin: 0 0 6px;">{{RATING}}<span style="font-size: 14px; color: #7c7c9a;">/10</span></p>
<p style="font-size: 12.5px; color: #64748b; line-height: 1.5; margin:0;">{{REASON}}</p>
</div>
Critérios sempre:

Custo-benefício 30%
Satisfação verificada 25%
Ficha técnica 20%
Recursos e usabilidade 10%
Consenso técnico 10%
Confiança e suporte 5%
19. FAQ — CARDS LOCKED
HTML

<!-- wp:heading {"anchor":"faq"} -->
<h2 id="faq" class="wp-block-heading">❓ Perguntas frequentes</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="margin-bottom: 28px;">
{{FAQ_CARDS}}
</div>
<!-- /wp:html -->
Cada card:

HTML

<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px;">
<p style="margin: 0 0 8px; font-weight: 700; font-size: 14.5px;">{{NUMBER}}. {{QUESTION}}</p>
<p style="margin: 0; font-size: 14px; line-height: 1.65;">{{ANSWER}}</p>
</div>
Nunca converter para <details>.

20. VEREDITO
HTML

<!-- wp:heading {"anchor":"veredito"} -->
<h2 id="veredito" class="wp-block-heading">✅ Veredito final: {{VERDICT_HEADING}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{VERDICT_TEXT}}</p>
<!-- /wp:paragraph -->
Alinhado à Régua e Resposta Rápida.

21. ESCOLHA RÁPIDA
HTML

<!-- wp:heading {"anchor":"escolha-rapida"} -->
<h2 id="escolha-rapida" class="wp-block-heading">⚡ Escolha rápida: 3 cenários</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin-bottom: 28px;">
{{QUICK_CHOICE_CARDS}}
</div>
<!-- /wp:html -->
22. CTA FINAL
Somente se MARKET_GATE passou.

Usar os mesmos CTAs canônicos da seção de compra.

Não inventar nova cor/componente.

23. FONTES — LOCKED
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin: 24px 0; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📚 Fontes consultadas nesta análise:</strong><br>
{{SOURCE_LINKS}}
</div>
<!-- /wp:html -->
URLs diretas.

24. UPDATE BOX — CONDITIONAL
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📌 Última atualização:</strong> {{UPDATED_DATE}} |
<strong>Produto em análise:</strong> {{PRODUCT_MODEL_SKU}}<br>
<strong>⚠️ Aviso:</strong> {{TEMPORAL_NOTICE}}
</div>
<!-- /wp:html -->
25. BYLINE — CONDITIONAL
Somente:

AUTHOR_APPROVED = SIM

Nunca gerar bio.

Usar fragmento canônico aprovado do autor.

Caso contrário:

omitir integralmente.

26. AVISO AFILIADO FINAL
HTML

<!-- wp:html -->
<div style="background: #f8fafc; border-top: 3px solid {{BRAND_PRIMARY}}; border-radius: 0 0 10px 10px; padding: 14px 18px; font-size: 12.5px; color: #64748b; line-height: 1.6;">
<strong>Aviso de afiliado:</strong> o Curadoria Prime participa de programas de afiliados. Compras feitas por links desta página podem gerar comissão ao site, sem custo adicional para você. Isso não altera nossos critérios editoriais. Preços e disponibilidade podem mudar.
</div>
<!-- /wp:html -->
BLOQUEIO FINAL
Antes da entrega:

nenhum {{SLOT}};
nenhum [IMAGEM AQUI];
nenhuma URL placeholder;
nenhuma nota não sustentada;
nenhum dado de exemplo;
nenhuma estrutura Markdown;
nenhuma classe visual inventada.
CP-IMAGE pode permanecer apenas enquanto aguarda upload.

text


5. `assets/template-vs.md`

Baseado diretamente no padrão Lenovo/Acer que você escolheu, mas sem seus fatos.

```markdown
# Template VS — Curadoria Prime v2.0

Status: LOCKED
Formato: Gutenberg + HTML inline
Uso: comparação direta de 2 ou 3 produtos

O HTML real é fonte de verdade.

Não converter para Markdown.
Não criar novo design.
Não copiar dados de golden references.

---

# ORDEM

1. Meta SEO
2. Hero VS
3. HERO-01
4. Tipo de análise
5. Metodologia
6. Transparência
7. Prova social
8. Índice
9. Introdução
10. Compra topo
11. Resposta rápida
12. Tabela comparativa
13. Produto A
14. Produto B
15. Produto C, quando existir
16. Para quem escolher cada um
17. Escolha rápida
18. Notas v2.0, quando disponíveis
19. FAQ
20. Veredito
21. Onde comprar
22. Fontes
23. Update box
24. Byline aprovado
25. Afiliado final

---

# 1. HERO VS

Mesma geometria do Hero REVIEW.

Kicker:

`📊 Comparativo {{VS_COUNT_LABEL}} — {{CATEGORY}}`

```html
<!-- wp:html -->
<div style="background: linear-gradient(135deg,{{HERO_PRIMARY}} 0%,{{HERO_SECONDARY}} 100%); color: #fff; padding: 28px 30px; border-radius: 14px; margin-bottom: 30px; font-size: 15.5px; line-height: 1.75;">

<div style="display: inline-block; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.28); font-size: 11px; font-weight: bold; letter-spacing: .1em; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;">📊 Comparativo {{VS_COUNT_LABEL}} — {{YEAR}}</div>

<p style="margin: 0 0 16px; font-size: 18px; font-weight: 600; color: #fff;">
{{VS_HERO_LEAD}}
</p>

<div style="display:flex;flex-wrap:wrap;gap:10px;">
{{VS_HERO_BADGES}}
<span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);padding:6px 14px;border-radius:100px;font-size:13px;">🕒 Atualizado: {{UPDATED_DATE}}</span>
</div>

</div>
<!-- /wp:html -->
Para marcas diferentes, Hero normalmente neutro:

#0f172a → #020617

Não vestir VS multi-marca como uma única fabricante.

2. HERO-01
Composição de produtos reais.

HTML

<!-- CP-IMAGE:HERO-01 -->
THUMB-01 fora do HTML.

3. TIPO DE ANÁLISE
HTML

<!-- wp:html -->
<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:16px 20px;margin-bottom:24px;font-size:13.5px;color:#78350f;line-height:1.7;">
<strong>📋 Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou estas unidades fisicamente.
</div>
<!-- /wp:html -->
4. METODOLOGIA
Usar mesmo componente jurídico REVIEW.

Explicar:

fontes de A;
fontes de B/C;
data comum de mercado;
critério de equivalência.
5. PROVA SOCIAL
Usar componente 2×2 canônico quando houver evidência.

No VS, distribuir evidência de forma útil entre produtos.

Não existe obrigação de exatamente um relato de cada produto/plataforma
se os dados não permitem.

Nunca inventar para simetria.

6. INTRODUÇÃO
Explicar:

por que esses produtos são comparáveis;
principal diferença;
decisão que o artigo resolve.
7. COMPRA TOPO
Cards dos produtos comparados.

MARKET_GATE obrigatório.

Mesmo componente de CTA.

8. RESPOSTA RÁPIDA
HTML

<!-- wp:heading {"anchor":"resposta-rapida"} -->
<h2 id="resposta-rapida" class="wp-block-heading">⚡ Resposta rápida: qual escolher?</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;margin-bottom:28px;">
{{VS_QUICK_CARDS}}
</div>
<!-- /wp:html -->
Cada card deve indicar perfil, não vencedor universal.

9. TABELA COMPARATIVA — CRÍTICO
HTML

<!-- wp:heading {"anchor":"tabela"} -->
<h2 id="tabela" class="wp-block-heading">📊 Tabela comparativa: {{PRODUCT_A_SHORT}} vs {{PRODUCT_B_SHORT}}{{OPTIONAL_PRODUCT_C}}</h2>
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
<th style="padding: 12px 14px; text-align: center;">{{PRODUCT_A_SHORT}}</th>
<th style="padding: 12px 14px; text-align: center;">{{PRODUCT_B_SHORT}}</th>
{{PRODUCT_C_HEADER}}
</tr>
</thead>

<tbody>
{{COMPARISON_ROWS}}
</tbody>

</table>
</div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Fonte:</strong> {{COMPARISON_SOURCES}}</p>
<!-- /wp:paragraph -->
Critérios:

categoria-específicos.

Não transformar em tabela "Ganha/Perde".

10. PRODUTO A
HTML

<!-- wp:heading {"anchor":"produto-a"} -->
<h2 id="produto-a" class="wp-block-heading">{{PRODUCT_A_ICON}} {{PRODUCT_A}} — {{PRODUCT_A_RATING_IF_VALID}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{PRODUCT_A_POSITIONING}}</p>
<!-- /wp:paragraph -->

<!-- CP-IMAGE:IMG-A -->

<!-- wp:paragraph -->
<p>{{PRODUCT_A_KEY_DATA}}</p>
<!-- /wp:paragraph -->

{{PRODUCT_A_PROS_CONS}}

<!-- wp:paragraph -->
<p><strong>Fonte oficial:</strong> {{PRODUCT_A_SOURCE_LINKS}}</p>
<!-- /wp:paragraph -->
11. PRODUTO B
Mesma estrutura do Produto A.

Nunca mudar design.

HTML

<!-- CP-IMAGE:IMG-B -->
12. PRODUTO C
Somente VS 3.

Mesma estrutura.

HTML

<!-- CP-IMAGE:IMG-C -->
13. PRÓS/CONTRAS POR PRODUTO
Usar exatamente CP-PROS-CONS do template-review.md.

Não criar variante.

14. PARA QUEM ESCOLHER CADA UM
Cards iguais em peso visual.

Não usar comissão como critério.

15. ESCOLHA RÁPIDA
Normalmente 3 cenários.

Exemplos:

orçamento;
performance;
portabilidade.
Não declarar vencedor universal quando não existe.

16. NOTAS v2.0
Se cada produto possuir nota válida:

mostrar score resumido e/ou os critérios conforme especificação do
template.

Se review vigente v2.0 já existir:

reutilizar com referência.

Se não:

calcular separadamente.

Não inventar nota para preencher comparação.

17. FAQ
Usar CP-FAQ canônico do REVIEW.

Cards, não <details>.

18. VEREDITO
Responder:

A vence para qual perfil;
B vence para qual;
C quando aplicável;
qual diferença de preço muda a decisão.
Não declarar vencedor absoluto sem base.

19. ONDE COMPRAR
Cards empilhados por produto.

MARKET_GATE obrigatório.

20. FONTES
Usar CP-SOURCES canônico.

Incluir fontes específicas de todos os produtos.

21. BYLINE
Somente AUTHOR_APPROVED.

22. IMAGENS
Relatório mínimo:

THUMB-01
HERO-01
IMG-A
IMG-B
IMG-C quando aplicável.

THUMB nunca entra no HTML.

BLOQUEIO
Nenhum:

slot;
URL fake;
preço fake;
nota fake;
review fake;
imagem de modelo parecido;
pode entrar na entrega pública.

text


6. `assets/template-lista.md`

```markdown
# Template LISTA/GUIA — Curadoria Prime v2.0

Status: LOCKED
Formato: Gutenberg + HTML inline
Uso: N produtos selecionados por categoria, perfil, preço ou ocasião.

Não usar para VS direto.

Não usar o antigo template-guia Markdown.

---

# ORDEM

1. Meta SEO
2. Hero neutro/multi-marca
3. HERO-01
4. Tipo de análise
5. Metodologia e critérios do ranking
6. Transparência
7. Índice
8. Resposta rápida
9. Tabela geral
10. Produto 1
11. Produto 2
12. Produto N
13. Faixas/perfis
14. Alertas
15. FAQ
16. Veredito do guia
17. Fontes
18. Update box
19. Byline aprovado
20. Afiliado final

---

# 1. HERO

Para lista multi-marca:

PRIMARY:

`#0f172a`

SECONDARY:

`#020617`

ACCENT:

`#e2e8f0`

Usar mesma geometria REVIEW:

```html
<!-- wp:html -->
<div style="background:linear-gradient(135deg,#0f172a 0%,#020617 100%);color:#fff;padding:28px 30px;border-radius:14px;margin-bottom:30px;font-size:15.5px;line-height:1.75;">

<div style="display:inline-block;background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);font-size:11px;font-weight:bold;letter-spacing:.1em;text-transform:uppercase;padding:4px 12px;border-radius:100px;margin-bottom:12px;">📌 Guia de Compra — {{YEAR}}</div>

<p style="margin:0 0 16px;font-size:18px;font-weight:600;color:#fff;">{{GUIDE_HERO_LEAD}}</p>

<div style="display:flex;flex-wrap:wrap;gap:10px;">
{{GUIDE_BADGES}}
<span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);padding:6px 14px;border-radius:100px;font-size:13px;">🕒 Atualizado: {{UPDATED_DATE}}</span>
</div>

</div>
<!-- /wp:html -->
2. HERO-01
HTML

<!-- CP-IMAGE:HERO-01 -->
Normalmente composição limpa da categoria.

THUMB-01 fora do HTML.

3. TIPO DE ANÁLISE
Usar plural:

HTML

<!-- wp:html -->
<div style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:16px 20px;margin-bottom:24px;font-size:13.5px;color:#78350f;line-height:1.7;">
<strong>📋 Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou estas unidades fisicamente.
</div>
<!-- /wp:html -->
4. METODOLOGIA DO GUIA
Explicar antes do ranking:

recorte;
critérios de entrada;
mercado;
perfis;
como ranking foi formado.
Não dizer "melhores do Brasil" sem base.

5. MERCADO
Cada SKU comercial precisa passar curadoria-mercado.

Produto FORA:

não recebe card como recomendado.

Pode aparecer em:

Ficou de fora

com motivo factual.

6. RESPOSTA RÁPIDA
Cards por perfil.

Exemplo conceitual:

Melhor para perfil A;
Melhor para perfil B;
Melhor para orçamento C.
Não usar nota/comissão como único critério.

7. TABELA GERAL
Usar padrão comparativo canônico:

HTML

<!-- wp:html -->
<div style="overflow-x:auto;margin-bottom:28px;">
<table style="width:100%;border-collapse:collapse;font-size:13.5px;min-width:640px;">
<thead>
<tr style="background:#0f172a;color:#fff;">
{{GUIDE_TABLE_HEADERS}}
</tr>
</thead>
<tbody>
{{GUIDE_TABLE_ROWS}}
</tbody>
</table>
</div>
<!-- /wp:html -->
Zebra:

#f8fafc
#fff

8. COMPONENTE DE PRODUTO
Cada produto usa a MESMA estrutura.

HTML

<!-- wp:heading {"anchor":"produto-{{POSITION}}"} -->
<h2 id="produto-{{POSITION}}" class="wp-block-heading">{{POSITION_LABEL}} {{PRODUCT_NAME}} — {{PROFILE_LABEL}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{PRODUCT_POSITIONING}}</p>
<!-- /wp:paragraph -->

<!-- CP-IMAGE:IMG-P{{POSITION}} -->

<!-- wp:paragraph -->
<p>{{PRODUCT_KEY_FACTS}}</p>
<!-- /wp:paragraph -->

{{PRODUCT_PROS_CONS}}

{{PRODUCT_BUY_CARD}}

<!-- wp:paragraph -->
<p><strong>Fonte oficial:</strong> {{PRODUCT_SOURCE_LINKS}}</p>
<!-- /wp:paragraph -->
Não variar design entre posições.

9. PRÓS E CONTRAS
Usar exatamente CP-PROS-CONS do REVIEW.

Não inventar três negativos.

10. CARD DE COMPRA
Somente depois de MARKET_GATE.

Usar CTAs canônicos Amazon/ML/oficial.

Preço datado.

11. NOTA DE PRODUTO
Só mostrar se:

review v2.0 existente; ou
Régua v2.0 foi aplicada com evidência suficiente.
Não gerar notas rápidas apenas para ordenar lista.

Ranking != nota.

12. FAIXA DE PREÇO
Explicar quando:

produto vale;
perde sentido;
rival fica mais adequado.
Basear nos dados atuais.

Não criar limites arbitrários.

13. ALERTAS
Podem incluir:

importação;
versão CN;
geração;
garantia;
acessório ausente;
incompatibilidade;
estoque.
Somente com evidência.

14. FAQ
Usar cards canônicos.

Perguntas sobre a decisão da categoria.

15. VEREDITO DO GUIA
Reafirmar:

melhor escolha por perfil;
trade-offs;
faixa de orçamento.
Não declarar vencedor universal se o guia é segmentado por perfil.

16. FONTES
Usar CP-SOURCES.

Incluir fonte oficial de cada item relevante.

Não listar somente marketplaces.

17. IMAGENS
Relatório mínimo:

THUMB-01
HERO-01
IMG-P01
IMG-P02
...
IMG-PN

Uma imagem identificável por produto quando disponível.

18. GUIA REGULATÓRIO
Este template não ativa automaticamente o visual ciano Power Bank.

Se intenção for regulatória:

classificar explicitamente como subtipo regulatório conforme
layout-apple-tv.md.

Não usar ciano apenas por ser power bank.

BLOQUEIO
Lista não pode existir apenas como:

nome
→ preço
→ afiliado.

Cada selecionado precisa de razão editorial verificável.

text


7. Golden references em `assets/modelos/`

Como já existe essa pasta, eu faria três arquivos adicionais/normalizados:

`assets/modelos/README.md`

```markdown
# Golden References

Arquivos desta pasta demonstram resultados visuais aprovados.

Eles são referência de:

- estrutura;
- geometria;
- CSS inline;
- Gutenberg;
- ordem visual.

Eles NÃO são fonte factual para novos artigos.

É proibido copiar de golden reference:

- preço;
- rating;
- count;
- comentário;
- comprador;
- URL comercial;
- SKU;
- nota;
- data;
- especificação.

Todo dado factual precisa ser novamente pesquisado.

Correspondência:

REVIEW → modelo-review-golden.html
VS → modelo-vs-golden.html
LISTA → modelo-lista-golden.html

Em conflito visual:

template vigente prevalece sobre golden antigo.
Eu usaria seu Apple TV corrigido como modelo-review-golden.html, Lenovo vs Acer corrigido/metodologicamente migrado como modelo-vs-golden.html, e sua melhor lista corrigida como modelo-lista-golden.html.

Não recomendo eu inventar esses três HTMLs sem ver os arquivos que já existem em assets/modelos/, porque aí poderíamos novamente criar um visual paralelo ao seu site.

Com essas alterações, a arquitetura fica finalmente consistente:

