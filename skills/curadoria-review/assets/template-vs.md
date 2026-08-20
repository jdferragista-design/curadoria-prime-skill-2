# Template VS — Curadoria Prime v2.0

Status: LOCKED
Formato: Gutenberg + HTML inline
Uso: Comparação direta de 2 ou 3 produtos lado a lado

Este template espelha o modelo-vs-golden.html (Lenovo vs Acer).

Não converter para Markdown.
Não criar novo design.
Não copiar dados de golden reference.
Preencher slots com dados verificados na execução.

---

# ORDEM OBRIGATÓRIA DE BLOCOS

1. Meta SEO (comentário HTML)
2. Hero Section (gradiente da marca do produto âncora)
3. HERO-01 (imagem principal)
4. Tipo de análise (somente se não houver teste físico)
5. Metodologia
6. Transparência (afiliados)
7. Prova Social (grid 2×2 — 2 Amazon + 2 ML)
8. Índice
9. Introdução
10. Aviso de afiliado
11. Botões de Compra Topo
12. Resposta Rápida (2 cards lado a lado)
13. Tabela Comparativa
14. Produto A (foto + prós/contras + fonte)
15. Produto B (foto + prós/contras + fonte)
16. Produto C (se houver — mesma estrutura)
17. Para Quem É / Não É (2 cards lado a lado)
18. Notas por Categoria — Régua v2.0 (grid 3×2)
19. Box "Como chegamos às notas"
20. Escolha Rápida (3 cards lado a lado)
21. FAQ
22. Veredito Final (2 cards comparando notas)
23. Onde Comprar (cards empilhados sem imagem)
24. Fontes Consultadas
25. Última Atualização + Rodapé
26. Byline (somente quando aprovado)
27. Aviso de Afiliado Final
28. Schema JSON-LD (Article + ItemList + FAQPage + BreadcrumbList)

---

## 1. META SEO

```html
<!--
META SEO
Título: {{PRODUTO_A}} ou {{PRODUTO_B}}: Qual Comprar em 2026?
Descrição: Comparamos {{PRODUTO_A}} vs {{PRODUTO_B}}. Especificações, preços e veredito.
URL: /{{slug-a}}-ou-{{slug-b}}/
Atualizado: {{DATA}}
-->
2. HERO SECTION (GRADIENTE DA MARCA)
HTML

<!-- wp:html -->
<div style="background: linear-gradient(135deg, {{BRAND_PRIMARY}} 0%, {{BRAND_SECONDARY}} 100%); color: #fff; padding: 28px 30px; border-radius: 14px; margin-bottom: 30px; font-size: 15.5px; line-height: 1.75;">
<div style="display: inline-block; background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); font-size: 11px; font-weight: bold; letter-spacing: .1em; text-transform: uppercase; padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;">📊 Comparativo {{VS_COUNT}} — {{CATEGORIA}} {{ANO}}</div>
<p style="margin: 0 0 16px; font-size: 18px; font-weight: 600; color: #fff;">{{PRODUTO_A}} ou {{PRODUTO_B}}: <strong style="color: {{BRAND_ACCENT}};">qual {{produto}} comprar em {{ANO}}?</strong></p>
<p style="margin: 0 0 16px; font-size: 15px; color: rgba(255,255,255,0.85);">Comparamos os dois {{produtos}} mais procurados: <strong style="color: {{BRAND_ACCENT}};">{{PRODUTO_A}}</strong> ({{SPEC_A}}, nota {{NOTA_A}}, R$ {{PREÇO_A}}) vs <strong style="color: {{BRAND_ACCENT}};">{{PRODUTO_B}}</strong> ({{SPEC_B}}, nota {{NOTA_B}}, R$ {{PREÇO_B}}). Especificações oficiais, avaliações e análise do custo-benefício.</p>
<div style="display: flex; flex-wrap: wrap; gap: 10px;">
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">⭐ {{RATING_A}}★ {{PRODUTO_A}} · {{RATING_B}}★ {{PRODUTO_B}}</span>
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">💰 R$ {{MIN}} a R$ {{MAX}}</span>
<span style="background: rgba(255,255,255,.2); border: 1px solid rgba(255,255,255,.3); padding: 6px 14px; border-radius: 100px; font-size: 13px;">🕒 Atualizado: {{DATA}}</span>
</div>
</div>
<!-- /wp:html -->
3. HERO-01
HTML

<!-- CP-IMAGE:HERO-01 -->
4. TIPO DE ANÁLISE
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
<strong>📋 Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou estas unidades fisicamente.
</div>
<!-- /wp:html -->
5. METODOLOGIA
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13.5px; color: #78350f; line-height: 1.7;">
<strong>📋 Metodologia deste comparativo:</strong> análise construída com base nas <strong>especificações técnicas oficiais {{FABRICANTE_A}} e {{FABRICANTE_B}}</strong>, <strong>reviews completos publicados no site</strong> (p={{ID_A}}, publicado {{DATA_A}}; p={{ID_B}}, publicado {{DATA_B}}) e <strong>avaliações reais de compradores</strong> na Amazon e Mercado Livre. <strong>Não testamos estas unidades fisicamente.</strong> <a href="https://curadoriaprime.com/sobre-a-curadoria-prime/" style="color: #1428A0; text-decoration: underline; font-weight: 600;">Entenda nossa metodologia</a>.
</div>
<!-- /wp:html -->
6. TRANSPARÊNCIA (AFILIADOS)
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
<strong>⚠️ Transparência:</strong> este artigo contém links de afiliados (Amazon e Mercado Livre). Se você comprar por eles, recebemos uma comissão <strong>sem custo adicional</strong> para você. Os preços mencionados são referentes à <strong>data de verificação {{DATA}}</strong> e estão sujeitos a alteração.
</div>
<!-- /wp:html -->
7. PROVA SOCIAL (2×2)
HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">
<p style="margin: 0 0 14px; font-size: 16px; font-weight: 700; color: #1e293b;">🗣️ O que dizem os compradores <span style="font-size: 12px; font-weight: 400; color: #64748b;">(dados de {{MÊS/ANO}})</span></p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
{{SOCIAL_CARDS}}
</div>
</div>
<!-- /wp:html -->
Card Amazon:
HTML

<div style="background: #fff; border: 1px solid #ffd499; border-left: 4px solid #FF9900; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #FF9900;">Amazon — {{PRODUTO}}</strong><br>
⭐ <strong>{{RATING}}/5</strong> · <strong>{{COUNT}} avaliações</strong> · {{DISTRIBUIÇÃO}}% 5★<br>
<em>"{{TRANSCRIÇÃO}}"</em> <span style="color:#64748b;">— {{NOME}}, comprador relata, {{DATA}}</span>
</div>
Card ML:
HTML

<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">
<strong style="color: #3485DB;">Mercado Livre — {{PRODUTO}}</strong><br>
⭐ <strong>{{RATING}}/5</strong> · <strong>{{COUNT}} opiniões</strong> · {{DISTRIBUIÇÃO}}% 5★<br>
<em>"{{TRANSCRIÇÃO}}"</em> <span style="color:#64748b;">— {{NOME}}, comprador relata, {{DATA}}</span>
</div>
8. ÍNDICE
HTML

<!-- wp:html -->
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">
<p style="margin: 0 0 14px; font-size: 15px; font-weight: 700; color: #1e293b;">📑 Índice do comparativo</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 8px 18px; font-size: 13.5px;">
{{INDEX_ITEMS}}
</div>
</div>
<!-- /wp:html -->
9. INTRODUÇÃO
HTML

<!-- wp:paragraph -->
<p>{{INTRO_PARAGRAPH}}</p>
<!-- /wp:paragraph -->
10. AVISO DE AFILIADO
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
<strong>⚠️ Transparência:</strong> este artigo contém links de afiliados (Amazon e Mercado Livre). Se você comprar por eles, recebemos uma comissão <strong>sem custo adicional</strong> para você. Os preços mencionados são referentes à <strong>data de verificação {{DATA}}</strong> e estão sujeitos a alteração.
</div>
<!-- /wp:html -->
11. BOTÕES DE COMPRA TOPO
HTML

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 28px;">
{{BUY_TOP_CARDS}}
</div>
<!-- /wp:html -->
12. RESPOSTA RÁPIDA
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">⚡ Resposta rápida: qual escolher?</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 28px;">
<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.6;">
<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#166534;">🥇 Melhor custo-benefício</p>
<p>{{QUICK_A}}</p>
</div>
<div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.6;">
<p style="margin:0 0 8px; font-size:15px; font-weight:700; color:#1e40af;">🏆 Melhor desempenho</p>
<p>{{QUICK_B}}</p>
</div>
</div>
<!-- /wp:html -->
13. TABELA COMPARATIVA
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">📊 Tabela comparativa: {{PRODUTO_A}} vs {{PRODUTO_B}}</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Dados verificados em {{DATA}}</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="overflow-x: auto; margin-bottom: 28px;">
<table style="width: 100%; border-collapse: collapse; font-size: 13.5px; min-width: 640px;">
<thead>
<tr style="background: {{TABLE_HEADER}}; color: #fff;">
<th style="padding: 12px 14px; text-align: left;">Critério</th>
<th style="padding: 12px 14px; text-align: center;">{{PRODUTO_A}}</th>
<th style="padding: 12px 14px; text-align: center;">{{PRODUTO_B}}</th>
</tr>
</thead>
<tbody>
{{TABLE_ROWS}}
</tbody>
</table>
</div>
<!-- /wp:html -->
14. PRODUTO A
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">💻 {{PRODUTO_A}} — nota {{NOTA_A}}/10</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>{{DESCRIPTION_A}}</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<figure style="margin: 20px 0; text-align: center;">
<img src="{{IMG_A}}" alt="{{ALT_A}}" style="width: 100%; max-width: 600px; height: auto; border-radius: 12px; display: block; margin: 0 auto;">
<figcaption style="font-size: 12.5px; color: #888; text-align: center; margin-top: 8px;">{{CAPTION_A}}</figcaption>
</figure>
<!-- /wp:html -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 25px 0;">
<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 24px;">
<h3 style="margin: 0 0 16px 0; font-size: 18px; color: #166534;">✅ Pontos Positivos</h3>
<ul style="list-style: none; padding: 0; margin: 0;">
{{PROS_A}}
</ul>
</div>
<div style="background: #fef2f2; border: 2px solid #ef4444; border-radius: 12px; padding: 24px;">
<h3 style="margin: 0 0 16px 0; font-size: 18px; color: #991b1b;">❌ Pontos Negativos</h3>
<ul style="list-style: none; padding: 0; margin: 0;">
{{CONS_A}}
</ul>
</div>
</div>
<!-- /wp:html -->

<!-- wp:paragraph -->
<p><strong>Fonte oficial:</strong> {{SOURCE_A}}</p>
<!-- /wp:paragraph -->
15. PRODUTO B
Mesma estrutura do Produto A.

16. PARA QUEM É / NÃO É
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">🎯 Compre o {{PRODUTO_A}} se... / Compre o {{PRODUTO_B}} se...</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; margin-bottom: 28px;">
<div style="background: #f0fdf4; border: 2px solid #22c55e; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #166534;">🎯 Compre o {{PRODUTO_A}} se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7;">
{{WHO_A}}
</ul>
</div>
<div style="background: #eff6ff; border: 2px solid #3b82f6; border-radius: 12px; padding: 18px;">
<h3 style="margin: 0 0 12px 0; font-size: 16px; color: #1e40af;">🎯 Compre o {{PRODUTO_B}} se...</h3>
<ul style="margin: 0; padding-left: 18px; font-size: 14px; line-height: 1.7;">
{{WHO_B}}
</ul>
</div>
</div>
<!-- /wp:html -->
17. NOTAS POR CATEGORIA — RÉGUA v2.0
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">📊 Notas por categoria — Régua v2.0</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div id="avaliacao-{{SLUG}}" style="margin: 32px 0; padding: 28px; background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%); border: 1px solid #e2e8f0; border-radius: 16px; box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);">

<div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 2px solid #e2e8f0;">
<div>
<div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">📊 {{PRODUTO_A}} vs {{PRODUTO_B}}</div>
<div style="font-size: 13px; color: #64748b;">Avaliação baseada em 6 critérios técnicos</div>
</div>
<div style="display: flex; align-items: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 14px 22px; border-radius: 12px;">
<div style="text-align: center;">
<div style="font-size: 30px; font-weight: 800; color: #fff; line-height: 1;">{{NOTA_A}}</div>
<div style="font-size: 10px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase;">{{PRODUTO_A}}</div>
</div>
<div style="height: 44px; width: 1px; background: rgba(255,255,255,0.3);"></div>
<div style="text-align: center;">
<div style="font-size: 30px; font-weight: 800; color: #fff; line-height: 1;">{{NOTA_B}}</div>
<div style="font-size: 10px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase;">{{PRODUTO_B}}</div>
</div>
<div style="height: 44px; width: 1px; background: rgba(255,255,255,0.3);"></div>
<div style="font-size: 12px; font-weight: 700; color: #fff; line-height: 1.3;">🏆<br>{{VENCEDOR}}</div>
</div>
</div>

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
{{RATING_CARDS}}
</div>

</div>
<!-- /wp:html -->
18. ESCOLHA RÁPIDA (3 CENÁRIOS)
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">⚡ Escolha rápida: 3 cenários de compra</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-bottom: 28px;">
{{QUICK_CHOICE_CARDS}}
</div>
<!-- /wp:html -->
19. FAQ
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">❓ Perguntas frequentes</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="margin-bottom: 28px;">
{{FAQ_CARDS}}
</div>
<!-- /wp:html -->
20. VEREDITO FINAL
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">✅ Veredito final: qual dos dois comprar?</h2>
<!-- /wp:heading -->

<!-- wp:html -->
<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; margin-bottom: 20px;">
{{VERDICT_CARDS}}
</div>
<!-- /wp:html -->
21. ONDE COMPRAR
HTML

<!-- wp:heading -->
<h2 class="wp-block-heading">🛒 Onde comprar: melhores preços verificados ({{DATA}})</h2>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>⚠️ <strong>Aviso:</strong> preços e estoque verificados em {{DATA}}</p>
<!-- /wp:paragraph -->

<!-- wp:html -->
<div style="background: white; border: 1px solid #e9ecef; border-radius: 20px; padding: 35px 25px; margin-top: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.05);">
{{BUY_CARDS}}
</div>
<!-- /wp:html -->
22. FONTES CONSULTADAS
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin: 24px 0; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📚 Fontes consultadas nesta análise:</strong><br>
{{SOURCE_LINKS}}
</div>
<!-- /wp:html -->
23. RODAPÉ + BYLINE
HTML

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13px; color: #78350f; line-height: 1.7;">
<strong>📌 Última atualização:</strong> {{DATA}} | <strong>Produtos em análise:</strong> {{PRODUTO_A}} · {{PRODUTO_B}}<br>
<strong>⚠️ Aviso:</strong> Os preços mencionados foram verificados em {{DATA}}.
</div>
<!-- /wp:html -->

<!-- wp:html -->
<div style="display: flex; gap: 16px; align-items: center; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px 20px; margin-bottom: 28px;">
<img src="{{AUTHOR_IMG}}" width="72" height="72" style="width: 72px; height: 72px; border-radius: 50%; object-fit: cover; flex-shrink: 0;">
<div style="font-size: 13.5px; line-height: 1.6; color: #334155;">
<strong style="font-size: 14.5px;">{{AUTHOR_NAME}}</strong> — {{AUTHOR_ROLE}}<br>
<span style="color: #64748b;">{{AUTHOR_BIO}}</span>
</div>
</div>
<!-- /wp:html -->
24. AVISO AFILIADO FINAL
HTML

<!-- wp:html -->
<div style="background: #f8fafc; border-top: 3px solid {{BRAND_PRIMARY}}; border-radius: 0 0 10px 10px; padding: 14px 18px; font-size: 12.5px; color: #64748b; line-height: 1.6;">
<strong>Aviso de afiliado:</strong> o Curadoria Prime participa dos programas de afiliados da Amazon e do Mercado Livre. Preços verificados em {{DATA}}.
</div>
<!-- /wp:html -->
25. SCHEMA JSON-LD
HTML

<!-- wp:html -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "{{PRODUTO_A}} ou {{PRODUTO_B}}: Qual Comprar em {{ANO}}?",
      "image": "{{HERO_IMG}}",
      "datePublished": "{{PUBLISHED_DATE}}",
      "dateModified": "{{MODIFIED_DATE}}",
      "inLanguage": "pt-BR",
      "author": { "@type": "Person", "name": "Cristiano Martins" },
      "publisher": { "@type": "Organization", "name": "Curadoria Prime" },
      "mainEntityOfPage": "{{URL}}",
      "description": "{{META_DESCRIPTION}}"
    },
    {
      "@type": "ItemList",
      "name": "{{PRODUTO_A}} vs {{PRODUTO_B}}",
      "numberOfItems": 2,
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "item": { "@type": "Product", "name": "{{PRODUTO_A}}", "brand": { "@type": "Brand", "name": "{{FABRICANTE_A}}" } } },
        { "@type": "ListItem", "position": 2, "item": { "@type": "Product", "name": "{{PRODUTO_B}}", "brand": { "@type": "Brand", "name": "{{FABRICANTE_B}}" } } }
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
        { "@type": "ListItem", "position": 2, "name": "{{CATEGORIA}}", "item": "{{CATEGORIA_URL}}" },
        { "@type": "ListItem", "position": 3, "name": "{{PRODUTO_A}} vs {{PRODUTO_B}}" }
      ]
    }
  ]
}
</script>
<!-- /wp:html -->
BLOQUEIO FINAL
nenhum {{SLOT}};
nenhum [IMAGEM AQUI];
nenhuma URL placeholder;
nenhum dado de exemplo;
nenhuma estrutura Markdown;
links afiliados com rel="sponsored nofollow noopener noreferrer";
preços com data;
"comprador relata" (sem "compra verificada" sem selo);
produtos com 3+ pontos de atenção;
sem aggregateRating externo;
sem priceValidUntil inventado.
