# ESTADO — 4541 (5 Presentes Tech Premium · `presentes-dia-dos-pais-2026-tech-premium`)

**Status:** ✅ CORRIGIDO E VALIDADO (reposicionado de sazonal → permanente)

- URL: https://curadoriaprime.com/presentes-dia-dos-pais-2026-tech-premium/
- Título (novo H1/schema): "5 Presentes Tech Premium em 2026: Guia Completo"
- Título (campo WP) ANTIGO: "Dia dos Pais 2026: 5 Presentes Tech Premium (Guia Completo)" — pendente no painel.
- Entregável: `articles/presentes-dia-dos-pais-2026-tech-premium-artigo-completo.html`
- Data da reescrita: 16/08/2026

## Decisões aplicadas (do editor, 16/08)

1. **SEM teste físico real** — "testado por nós"/"testamos na bancada" NÃO se aplicam.
   As 3 frases viraram "Analisamos em detalhe". O selo "Testado por nós" só aparece
   no disclaimer padrão (contexto aprovado).
2. **SEM "Dia dos Pais 2026"** — reposicionado para guia permanente (filosofia do 4397).
3. **Contras §2.7** — 5 blocos "Pontos de Atenção" (h4 + `<ul>` ≥3).
4. **Faixas de preço de 6 meses** (fev–ago/2026), sem valor fixo.

## Faixas aplicadas (6 meses)

| Produto | Faixa |
|---|---|
| Apple Pencil Pro | R$ 1.100 – R$ 1.500 |
| Galaxy Watch7 44mm BT | R$ 1.050 – R$ 1.590 |
| Anker 737 PowerCore 24K | R$ 600 – R$ 800 |
| Soundcore Liberty 4 NC | R$ 370 – R$ 450 |
| JBL Wave Buds 2 | R$ 220 – R$ 290 |

## Links de afiliado (12, extraídos do artigo ao vivo — 100% sponsored)

| Produto | Amazon | ML |
|---|---|---|
| Apple Pencil Pro | `link.amazon/B00DEwd4w` | — (sem nacional confiável) |
| Galaxy Watch7 44mm | `link.amazon/B01x5UxXC` | `meli.la/1LuqqHm` |
| Anker 737 | `link.amazon/B0hWINXCY` (irmão A1695) | `meli.la/2uyvRWS` |
| Liberty 4 NC | `link.amazon/B02Xs9U4O` | `meli.la/2BweosK` |
| JBL Wave Buds 2 | `amzn.to/4xdlwEo` | `meli.la/2JLLpU1` |
| Escolha rápida | Liberty `B02Xs9U4O` | Anker `2uyvRWS` + Watch7 `1LuqqHm` |

## Correções além das decisões

- Bug de link interno corrigido: o rascunho do outro chat usava o slug literal
  `slug-presentes-dia-dos-pais-tech-ate-300` (placeholder) → trocado pelo real
  `presentes-dia-dos-pais-tech-ate-300`.
- Breadcrumb: categoria corrigida de `guias` (inexistente) → `destaques` (real).
- JSON-LD: @graph = Article + ItemList(5) + FAQPage(8) + BreadcrumbList.
  SEM aggregateRating, SEM priceValidUntil, SEM availability. AggregateOffer com
  lowPrice/highPrice (faixas de 6 meses). Autor canônico Cristiano Martins
  (url /sobre-a-curadoria-prime/, sameAs x.com/CuradoriaPrime). Fuso -03:00.
- Deslazyficadas: 6 imagens + 3 iframes (src direto, sem data-lazyloaded/litespeed).
- Metodologia: "compradores verificados" → "avaliações publicadas por compradores".

## Validação (checar_conformidade.py)

✅ APROVADO: 0 erros, 0 alertas. 12 links sponsored 100%. div 91×91. zero base64.
"testamos"/"testado por nós" restantes são NEGAÇÕES + selo do disclaimer (checker: 0 alegações).

## Pendências (painel, fora do arquivo)

1. **Campo Título do post + Rank Math SEO:** remover "Dia dos Pais 2026" →
   "5 Presentes Tech Premium em 2026: Guia Completo".
2. **Perfil WP:** nome de exibição "Cristiano Martins".
3. **Fuso horário:** São Paulo (se ainda não aplicado).
4. **Slug** ainda contém "dia-dos-pais" — avaliar 301 futuro (não feito, §9.4).
5. **Imagens** com nome "dia-dos-pais-2026" na biblioteca (hero premium / pencil-ipad):
   URLs mantidas (existem no WP); só o alt foi atualizado. Se renomear no WP, avisar p/ atualizar o src.
