# ESTADO — 3139 (Samsung S90F QD-OLED review)

**Status:** ✅ REWRITE CONCLUÍDO e validado (aguardando colagem no WP pelo cliente)

- URL: https://curadoriaprime.com/samsung-s90f-qd-oled-review/
- Título: Samsung S90F Vale a Pena em 2026? Review QD-OLED 4K 144Hz
- Entregável: `articles/samsung-s90f-qd-oled-review.html`
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **Links de afiliado** com `rel="sponsored noopener noreferrer nofollow"` (4 links: 2 Samsung + 2 LG). Os botões "Comparar Preços: LG C5" do publicado estavam SEM href (quebrados) — corrigidos.
- **"dados de compradores verificados" / "47 avaliações verificadas"** → "avaliações publicadas por compradores".
- **Alegação de uso removida**: "É frustrante voltar para controle comum depois de usar Magic Remote" e "navega 3-5x/5x mais rápido" → suavizadas (sem medição inventada).
- **Citações sem fonte verificável removidas** (5 blockquotes: "Usuário verificado", "Comunidade gamer Reddit (9,5/10)", "Review técnico em fórum", "fóruns especializados") → **"Síntese editorial dos relatos"** sem aspas/nome.
- **Placeholders vazados removidos**: "[INSERIR FOTO 3]", "[INSERIR FOTO 6]", "Nome do arquivo:", "Alt text:", "Legenda:" (eram TODO do rascunho publicado).
- **Texto duplicado/truncado corrigido** ("ente melhores que na LG C5.", "as HDMI 2.1... Empate técnico.") e typos "WOOLD" → "WOLED" (3×).
- **Superlativos suavizados**: "imbatível", "vence", "vencedor", "mágica tecnológica", "impossíveis", "Para 80% das pessoas".
- **Box de metodologia** com "não testamos esta unidade fisicamente".
- **Preços atualizados (16/08/2026)**: Samsung S90F ~R$ 6.478 (ML); LG C5 ~R$ 5.851–6.595. A diferença hoje é ~R$ 600 (não R$ 1.000 como no publicado).
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + Product (S90F, reviewRating 9,3/10 com worstRating) + FAQPage + BreadcrumbList (`tv-e-home-theater`); autor "Cristiano Martins"; sem aggregateRating/offers.
- **Bloco de autor canônico** + "Fontes consultadas" (Samsung, LG, Rtings.com) + "Veja também" (3153, 3226).

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 4/4 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.273 palavras · valor-agregado completo · imparcialidade 6 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 32/32 · ul 2/2 · ol 2/2 · p 57/57 · h2 11/11 · li 16/16 · a 21/21.
Zero base64. Zero citação inventada.
```

## Dados de mercado coletados (16/08/2026)

| TV | Preço hoje | Amazon | Mercado Livre |
|---|---|---|---|
| Samsung S90F 55" QD-OLED | R$ 6.478 (ML, Fast Shop) | ASIN **B0FNT5H95K** (`amazon.com.br/dp/B0FNT5H95K`) | **MLB54140106** (`…/p/MLB54140106`) |
| LG OLED C5 55" | R$ 5.851 a R$ 6.595 | ASIN **B0F5X3WY5N** (`amazon.com.br/dp/B0F5X3WY5N`) | **MLB53613524** (`…/p/MLB53613524`) |

- Samsung Amazon BR: 4,8/5 em ~38 avaliações (16/08/2026) — atualizado no artigo (o "4,9/5 · 47" do publicado estava defasado/não batia).
- **Artigo atualizado** com 4 botões (Amazon + ML para cada TV), todos com rel="sponsored". Links diretos canônicos usados como fallback até o cliente gerar os shortlinks.

## Pendências FORA do arquivo (painel / cliente)

1. **Colar no WP** substituindo o conteúdo atual (Editor de Código).
2. ⚠️ **Shortlink LG C5 (`mercadolivre.com/sec/1rZFCkW`) resolve para uma LISTA VAZIA** — o artigo agora usa o link direto `/p/MLB53613524` como fallback. **O cliente deve gerar novo shortlink** (mercado livre afiliados) e me passar para trocar.
3. Shortlink Samsung S90F (`2fDo1zK`) OK → MLB54140106. Amazon: precisa de shortlink (`amzn.to`/`link.amazon`) ou confirmar a tag do programa Amazon (memória cita `martins73-20`, não confirmada no repo).
4. ~~Contagem "47 avaliações / 4,9/5"~~ ✅ resolvida: Amazon BR hoje = 4,8/5 em ~38 avaliações.
5. Título SEO: manter "144Hz" e conferir "QD-OLED" no H1 (mesmo padrão dos outros posts).
