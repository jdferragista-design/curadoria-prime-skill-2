Template LISTA/GUIA — Curadoria Prime v2.0
Status: LOCKED
Formato: Gutenberg + HTML inline
Uso: N produtos selecionados por categoria, perfil, preço ou ocasião.

Este template espelha a estrutura do modelo-lista-golden.html.

Não converter para Markdown.
Não criar novo design.
Não copiar dados de golden reference.
Preencher slots com dados verificados na execução.

ORDEM OBRIGATÓRIA DE BLOCOS
Meta SEO (comentário HTML)
Hero Section (gradiente neutro/multi-marca)
Metodologia (Régua v2.0)
Transparência (afiliados)
Resposta rápida (veredito em 15s)
Critérios de avaliação
Produto #1 (posição + ficha + prós/contras + veredito + CTA)
Produto #2
Produto #3
Produto #4
Produto #5
Tabela comparativa
FAQ
Conclusão / Veredito do guia
Escolha rápida (bloco escuro)
Análises completas do cluster (links)
Fontes consultadas
Revisão editorial + rodapé
Byline
Schema JSON-LD (Article + ItemList + FAQPage + BreadcrumbList)
1. META SEO
HTML

<!--
META SEO
Título: {{SEO_TITLE}}
Descrição: {{META_DESCRIPTION}}
URL: {{URL}}
Atualizado: {{UPDATED_DATE}}
-->
2. HERO SECTION (MULTI-MARCA)
HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg,#1a1a2e 0%,#16213e 100%); color: #fff; padding: 28px 30px; border-radius: 14px; margin-bottom: 30px; font-size: 15.5px; line-height: 1.75;">
<div style="display: inline-block; background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); font-size: 11px; font-weight: bold; letter-spacing: .1em; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;">{{KICKER_LABEL}}</div>
<p style="margin: 0 0 16px; font-size: 20px; font-weight: 700; color: #fff;">{{TITLE}}</p>
<p style="margin: 0 0 16px; color: #e2e2f0; font-size: 15px; line-height: 1.7;">{{DESCRIPTION}}</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
{{HERO_BADGES}}
</div>
</div>
<!-- /wp:html -->
Badges Hero
HTML

<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold;">{{BADGE_1}}</span>
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold;">{{BADGE_2}}</span>
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold;">{{BADGE_3}}</span>
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold;">{{BADGE_4}}</span>
3. METODOLOGIA (RÉGUA v2.0)
HTML

<!-- wp:html -->
<div style="background: #fff; border: 1px solid #e2e2f0; border-left: 4px solid #5a4fcf; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px; box-shadow: 0 2px 8px rgba(90,79,207,.07);">
<p style="font-size: 14px; font-weight: bold; color: #1a1a2e; margin: 0 0 12px; text-transform: uppercase; letter-spacing: .06em;">📋 Metodologia deste guia</p>
<p style="margin: 0 0 12px; color: #4a4a68; font-size: 14.5px; line-height: 1.7;">Cada modelo da lista passou pela <strong style="color: #1a1a2e;">Régua Curadoria Prime v2.0</strong>:</p>
<p style="margin: 0 0 8px; padding: 8px 0 8px 28px; position: relative; color: #4a4a68; border-bottom: 1px solid #f0f0f8; font-size: 15px;"><span style="position: absolute; left: 0; color: #5a4fcf; font-weight: 800;">✓</span><strong style="color: #1a1a2e;">Especificações oficiais</strong> dos fabricantes</p>
<p style="margin: 0 0 8px; padding: 8px 0 8px 28px; position: relative; color: #4a4a68; border-bottom: 1px solid #f0f0f8; font-size: 15px;"><span style="position: absolute; left: 0; color: #5a4fcf; font-weight: 800;">✓</span><strong style="color: #1a1a2e;">Testes publicados por canais especializados</strong></p>
<p style="margin: 0 0 8px; padding: 8px 0 8px 28px; position: relative; color: #4a4a68; border-bottom: 1px solid #f0f0f8; font-size: 15px;"><span style="position: absolute; left: 0; color: #5a4fcf; font-weight: 800;">✓</span><strong style="color: #1a1a2e;">Leitura das avaliações publicadas por compradores</strong> na Amazon Brasil e no Mercado Livre</p>
<p style="margin: 0 0 8px; padding: 8px 0 8px 28px; position: relative; color: #4a4a68; font-size: 15px;"><span style="position: absolute; left: 0; color: #5a4fcf; font-weight: 800;">✓</span><strong style="color: #1a1a2e;">Comparativo de mercado</strong> e síntese independente</p>
<p style="margin: 12px 0 0; color: #7c7c9a; font-size: 13.5px; line-height: 1.7;">🔍 <strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou estas unidades fisicamente. <a href="https://curadoriaprime.com/sobre-a-curadoria-prime/" style="color: #5a4fcf; text-decoration: underline; font-weight: 600;">Entenda nossa metodologia →</a></p>
</div>
<!-- /wp:html -->
4. TRANSPARÊNCIA (AFILIADOS)
HTML

<!-- wp:html -->
<div style="background: #f8f8ff; border: 1px solid #e2e2f0; border-radius: 10px; padding: 14px 20px; margin-bottom: 28px; font-size: 13.5px; color: #7c7c9a; line-height: 1.65;">⚠️ <strong style="color: #1a1a2e;">Transparência:</strong> este guia contém links de afiliados (Amazon e Mercado Livre). Se você comprar por eles, recebemos uma comissão sem custo adicional para você. O ranking é editorial — baseado em especificação oficial, testes de especialistas e relatos publicados por compradores — e não é influenciado pelas lojas. <a href="https://curadoriaprime.com/transparencia-curadoria-prime/" style="color: #5a4fcf; text-decoration: underline; font-weight: 600;">Saiba mais →</a></div>
<!-- /wp:html -->
5. RESPOSTA RÁPIDA
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">1. Resposta Rápida: qual {{CATEGORY}} comprar para cada perfil</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">
<p style="font-size: 14px; font-weight: bold; color: #1a1a2e; margin: 0 0 12px; text-transform: uppercase; letter-spacing: .06em;">✅ O veredito em 15 segundos (preços de {{DATA}}):</p>
<ul style="margin: 0; padding-left: 20px; line-height: 2;">
{{QUICK_VERDICT_ITEMS}}
</ul>
</div>
<!-- /wp:html -->
Itens
HTML

<li><strong>{{LABEL}}:</strong> {{PRODUCT}} — {{PRICE}}</li>
6. CRITÉRIOS DE AVALIAÇÃO
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">2. Critérios de avaliação</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">
<p style="margin: 0 0 12px; color: #4a4a68; font-size: 15px;">Para entrar neste Top {{N}}, cada modelo foi avaliado nos mesmos seis critérios da Régua v2.0:</p>
<ul style="margin: 0; padding-left: 20px; line-height: 2;">
<li><strong>💰 Custo-benefício (30%):</strong> o que o produto entrega pelo preço praticado hoje</li>
<li><strong>⭐ Satisfação verificada (25%):</strong> volume e teor das avaliações na Amazon e ML</li>
<li><strong>📋 Ficha técnica (20%):</strong> especificações oficiais comparadas aos rivais da faixa</li>
<li><strong>⚙️ Recursos e usabilidade (10%):</strong> recursos extras relevantes</li>
<li><strong>📚 Consenso técnico (10%):</strong> convergência entre reviews de especialistas</li>
<li><strong>🤝 Confiança e suporte (5%):</strong> garantia, assistência e histórico da marca</li>
</ul>
</div>
<!-- /wp:html -->
7. PRODUTO #1 (e repetir para demais)
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">3. 🥇 {{PRODUTO_1_NOME}} — {{PRODUTO_1_RÓTULO}}</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 16px;"><span style="background: #f5f5fb; border: 1px solid #e2e2f0; padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold; color: #1a1a2e;">🥇 1º lugar · {{LABEL_1}}</span>
<span style="background: #f5f5fb; border: 1px solid #e2e2f0; padding: 6px 14px; border-radius: 100px; font-size: 13px; font-weight: bold; color: #1a1a2e;">💸 {{PRICE_1}} · verificado {{DATA}}</span></div>
<!-- /wp:html -->

<!-- wp:html -->
<div style="margin-bottom: 20px;">
<img src="{{IMG_1}}" style="width: 100%; max-width: 500px; height: auto; border-radius: 12px; display: block; margin: 0 auto; box-shadow: 0 4px 16px rgba(90,79,207,.12);" alt="{{ALT_1}}" loading="lazy" decoding="async" width="758" height="505"><p></p>
<p style="text-align: center; font-size: 12px; color: #7c7c9a; margin: 8px 0 0;">{{CAPTION_1}}</p>
</div>
<!-- /wp:html -->

<!-- wp:paragraph {"className":"wp-block-paragraph"} -->
<p class="wp-block-paragraph">{{DESCRIPTION_1}}</p>
<!-- /wp:paragraph -->

<!-- wp:heading {"level":3,"className":"wp-block-heading"} -->
<h3 class="wp-block-heading">📋 Ficha técnica</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 6px 24px rgba(90,79,207,.12); margin-bottom: 20px;">
<table style="width: 100%; border-collapse: collapse; font-size: 14.5px; min-width: 500px;">
<thead><tr style="background: linear-gradient(135deg,#5a4fcf,#764ba2); color: #fff;"><th style="padding: 12px 16px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .06em; width: 40%;">Especificação</th><th style="padding: 12px 16px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">Detalhe</th></tr></thead>
<tbody>
{{SPEC_ROWS_1}}
</tbody>
</table>
</div>
<!-- /wp:html -->

<!-- wp:heading {"level":3,"className":"wp-block-heading"} -->
<h3 class="wp-block-heading">✨ O que ele faz de melhor</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 20px;">
{{HIGHLIGHTS_1}}
</div>
<!-- /wp:html -->

<!-- wp:html -->
<div style="background: #fff1f2; border: 1px solid #fecdd3; border-left: 4px solid #e11d48; border-radius: 8px; padding: 16px 20px; margin-bottom: 20px;">
<h3 class="wp-block-heading" style="font-size: 16px; color: #9f1239; margin: 0 0 12px;">Pontos de Atenção</h3>
<ul style="margin: 0; padding-left: 20px; line-height: 1.8; color: #9f1239; font-size: 14.5px;">
{{ATTENTION_1}}
</ul>
</div>
<!-- /wp:html -->

<!-- wp:html -->
<div style="background: #f0fdf4; border-left: 4px solid #22c55e; border-radius: 8px; padding: 16px 20px; margin-bottom: 20px;">
<p style="font-size: 15px; font-weight: bold; color: #14532d; margin: 0 0 8px;">💡 Veredito:</p>
<p style="color: #166534; font-size: 14.5px; margin: 0; line-height: 1.7;">{{VERDICT_1}}</p>
</div>
<!-- /wp:html -->

<!-- wp:paragraph {"className":"wp-block-paragraph"} -->
<p class="wp-block-paragraph">Leia a <a href="{{REVIEW_URL_1}}"><strong>análise completa do {{PRODUTO_1_NOME}}</strong></a>.</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="background: #f5f5fb; border-radius: 12px; padding: 20px 22px; margin-bottom: 36px; text-align: center;">
<p style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: .08em; color: #7c7c9a; margin: 0 0 14px;">🛒 {{PRODUTO_1_NOME}}</p>
<p style="font-size: 14px; color: #4a4a68; margin: 0 0 12px;">{{BUY_INFO_1}}</p>
<div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">{{BUY_BUTTONS_1}}</div>
<p style="font-size: 12px; color: #9c9cb8; margin: 10px 0 0;">Marketplaces alteram preços sem aviso — confirme o valor na loja.</p>
</div>
<!-- /wp:html -->
8. TABELA COMPARATIVA
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">8. Tabela comparativa lado a lado</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="overflow-x: auto; border-radius: 12px; box-shadow: 0 6px 24px rgba(90,79,207,.12); margin-bottom: 12px;">
<table style="width: 100%; border-collapse: collapse; font-size: 14px; min-width: 640px;">
<thead><tr style="background: linear-gradient(135deg,#5a4fcf,#764ba2); color: #fff;"><th style="padding: 12px 14px; text-align: left; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_1}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_2}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_3}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_4}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_5}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_6}}</th><th style="padding: 12px 14px; text-align: center; font-size: 12px; text-transform: uppercase; letter-spacing: .06em;">{{COLUMN_7}}</th></tr></thead>
<tbody>
{{TABLE_ROWS}}
</tbody>
</table>
<p style="margin: 8px 0 0; font-size: 12.5px; color: #7c7c9a;">{{TABLE_FOOTNOTE}}</p>
</div>
<!-- /wp:html -->
9. FAQ
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">9. Perguntas frequentes</h2>
<!-- /wp:heading -->

<!-- wp:html -->
{{FAQ_CARDS}}
<!-- /wp:html -->
Card FAQ
HTML

<div style="background: #fff; border-radius: 12px; margin-bottom: 10px; border: 1px solid #e2e2f0; overflow: hidden; box-shadow: 0 2px 8px rgba(90,79,207,.07);">
<p style="padding: 16px 20px; font-size: 15px; font-weight: bold; color: #5a4fcf; margin: 0; border-bottom: 1px solid #e2e2f0;">{{N}}. {{PERGUNTA}}</p>
<p style="padding: 14px 20px; color: #4a4a68; font-size: 15px; margin: 0; line-height: 1.7;">{{RESPOSTA}}</p>
</div>
10. CONCLUSÃO / VEREDITO DO GUIA
HTML

<!-- wp:heading {"className":"wp-block-heading"} -->
<h2 class="wp-block-heading">10. Conclusão: qual {{CATEGORY}} escolher?</h2>
<!-- /wp:heading -->

<!-- wp:paragraph {"className":"wp-block-paragraph"} -->
<p class="wp-block-paragraph">{{CONCLUSION_PARAGRAPH}}</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">
<ul style="margin: 0; padding-left: 20px; line-height: 2;">
{{CONCLUSION_ITEMS}}
</ul>
</div>
<!-- /wp:html -->
11. ESCOLHA RÁPIDA (BLOCO ESCURO)
HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg,#5a4fcf 0%,#764ba2 100%); border-radius: 14px; padding: 28px 30px; margin-bottom: 30px; text-align: center;">
<p style="font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: .08em; color: rgba(255,255,255,.8); margin: 0 0 12px;">⚡ Escolha rápida</p>
<p style="font-size: 16px; color: #fff; margin: 0 0 8px;">{{QUICK_CHOICE_TEXT}}</p>
<p style="font-size: 12px; color: rgba(255,255,255,.5); margin: 0 0 16px;">Preços verificados em {{DATA}} — sujeitos a alteração.</p>
<div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 12px;">{{QUICK_CHOICE_BUTTONS}}</div>
</div>
<!-- /wp:html -->
12. ANÁLISES COMPLETAS DO CLUSTER (LINKS)
HTML

<!-- wp:heading {"level":3,"className":"wp-block-heading"} -->
<h3 class="wp-block-heading">🎧 Análises completas do cluster de {{CATEGORIA}}</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: #fff; border-left: 4px solid #5a4fcf; border-radius: 10px; padding: 18px 22px; margin: 28px 0; box-shadow: 0 2px 8px rgba(90,79,207,.08);">
<ul style="margin: 0; padding-left: 20px; line-height: 2;">
{{CLUSTER_LINKS}}
</ul>
</div>
<!-- /wp:html -->
13. FONTES CONSULTADAS
HTML

<!-- wp:heading {"level":3,"className":"wp-block-heading"} -->
<h3 class="wp-block-heading">📚 Fontes consultadas</h3>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="background: #f8f9fa; border-left: 4px solid #5a4fcf; padding: 16px 20px; margin: 24px 0; border-radius: 6px;">
<ul style="margin: 0; padding-left: 20px; line-height: 1.9; font-size: 14px; color: #4a4a68;">
{{SOURCE_LINKS}}
</ul>
</div>
<!-- /wp:html -->
14. REVISÃO EDITORIAL + RODAPÉ
HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg,#5a4fcf 0%,#764ba2 100%); color: rgba(255,255,255,.9); padding: 18px 24px; border-radius: 12px;">
<p style="margin: 0; font-size: 13.5px; line-height: 1.75;">{{REVISION_FOOTER}}</p>
</div>
<!-- /wp:html -->
15. BYLINE
HTML

<!-- wp:html -->
<div style="display: flex; gap: 16px; align-items: center; background: #f5f5fb; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 20px; margin: 28px 0 20px;"><img src="{{AUTHOR_IMG}}" alt="{{AUTHOR_ALT}}" width="72" height="72" loading="lazy" decoding="async" style="width: 72px; height: 72px; border-radius: 50%; object-fit: cover; flex-shrink: 0;"><p></p>
<div style="font-size: 13.5px; line-height: 1.6; color: #4a4a68;"><strong style="font-size: 14.5px; color: #1a1a2e;">{{AUTHOR_NAME}}</strong> — {{AUTHOR_ROLE}}<br>
<span style="color: #7c7c9a;">{{AUTHOR_BIO}}</span> <a href="{{AUTHOR_SOCIAL}}" rel="noopener" target="_blank" style="color: #1d4ed8; font-weight: 600; text-decoration: none;">Seguir no X →</a></div>
</div>
<!-- /wp:html -->
16. SCHEMA JSON-LD
HTML

<!-- wp:html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "{{SEO_TITLE}}",
      "image": "{{HERO_IMG}}",
      "datePublished": "{{PUBLISHED_DATE}}",
      "dateModified": "{{MODIFIED_DATE}}",
      "inLanguage": "pt-BR",
      "author": { "@type": "Person", "name": "Cristiano Martins", "url": "https://curadoriaprime.com/sobre-a-curadoria-prime/" },
      "publisher": { "@type": "Organization", "name": "Curadoria Prime", "url": "https://curadoriaprime.com/", "logo": { "@type": "ImageObject", "url": "{{LOGO_URL}}" } },
      "mainEntityOfPage": "{{URL}}",
      "description": "{{META_DESCRIPTION}}"
    },
    {
      "@type": "ItemList",
      "name": "{{ITEM_LIST_NAME}}",
      "numberOfItems": {{COUNT}},
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "itemListElement": [
        {{ITEM_LIST_ELEMENTS}}
      ]
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {{FAQ_SCHEMA_ITEMS}}
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Início", "item": "https://curadoriaprime.com/" },
        { "@type": "ListItem", "position": 2, "name": "{{CATEGORY}}", "item": "{{CATEGORY_URL}}" },
        { "@type": "ListItem", "position": 3, "name": "{{TITLE}}" }
      ]
    }
  ]
}
</script>
<!-- /wp:html -->
BLOQUEIO FINAL
Antes da entrega:

nenhum {{SLOT}};
nenhum [IMAGEM AQUI];
nenhuma URL placeholder;
nenhum dado de exemplo;
nenhuma estrutura Markdown;
nenhuma classe visual inventada;
links afiliados com rel="sponsored nofollow noopener noreferrer";
preços com data de verificação;
testemunhos com "comprador relata" (sem "compra verificada" sem selo);
produtos com 3+ pontos de atenção;
sem aggregateRating externo;
sem priceValidUntil inventado.
