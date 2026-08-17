# ESTADO — 3548 (Redmi Buds 6 Play · `redmi-buds-6-play-review-2026-vale-a-pena`)

**Status:** ✅ REESCRITO em 17/08/2026 · checker 14/14, 0 erros · 4.261 palavras · nota 8,2/10
**Arquivo:** `articles/redmi-buds-6-play-review-2026-vale-a-pena.html`

## 🔴 Achados críticos no publicado

### 1. URGÊNCIA VENCIDA NO AR
O card de compra dizia: *"chega grátis entre terça e quinta — **a tempo do Dia dos Pais (09/08)**"*.
Hoje é **17/08**: a data passou há mais de uma semana. É o mesmo erro já corrigido no guia 3336 em
14/08 ("chega antes do Dia dos Pais"), que reapareceu aqui. **Removido.**

### 2. "207 mil+ avaliações reais" — número inflado
Hero e corpo citavam **207.851 avaliações**. É o total do **catálogo** do Mercado Livre, que agrega
dezenas de variações e produtos correlatos — não são avaliações do anúncio analisado. Substituído
por descrição qualitativa (selo de mais vendido, nota alta consistente) sem número não verificável.

### 3. Três depoimentos com selo "compra verificada"
Mesma violação da regra 4.2 já corrigida no 3523: citações entre aspas com selo. → **síntese
editorial**, sem aspas e sem selo. Também saiu "compradores verificados" (2×) do bloco de metodologia.

### 4. Preços de 01/08 desatualizados — dois com erro de direção
| Produto | publicado (01/08) | **real (17/08)** | impacto |
|---|---|---|---|
| Redmi Buds 6 Play | R$ 79,90 Pix | **R$ 78,99** | menor |
| QCY T13 ANC | R$ 143,55 | **R$ 186,10 / R$ 199** | 🔴 grave |
| Galaxy Buds Core | R$ 242,19 | **R$ 219,31 / R$ 268,20** | corrigido |

O caso do QCY era o pior: o texto mandava o leitor ao QCY "por um pouco mais" citando R$ 143,55.
Hoje o QCY custa **2,5× o Redmi** — a recomendação mudava de sentido. Reescrita com o alerta.
Removido também o nome do vendedor ("GSOTECNO"), que muda a cada consulta.

### 5. "Problemas Comuns" com rótulo de frequência sem base
Os 4 itens traziam "Frequência: alta / moderada / baixa" **sem dump de avaliações**. Pela regra
§18.3 e pela lição §15.2, a seção foi renomeada para **"Limitações conhecidas"** e abre com um aviso
declarando que a lista é **dedutiva** (derivada da ficha técnica), não contagem. Nenhum item tem
rótulo de frequência.

## ➕ Adicionado
- **Faixa de preço dos últimos 6 meses** (regra §18): Redmi R$ 78 / R$ 79–120 / **R$ 78,99 no piso
  histórico** · QCY · Buds Core, com leitura por produto.
- Bloco **"Prós e contras"** (não existia): 8 prós + 7 Pontos de Atenção.
- Seção **"não é para quem"** com 5 perfis.
- JSON-LD `@graph` completo: Article + Review + FAQPage (5 perguntas espelhando a visível) +
  BreadcrumbList. Sem `offers`, sem `aggregateRating`, sem `priceValidUntil`.

## Preços verificados (17/08/2026)
`meli.la/1J2VMuY` → **MLB55462947**, R$ 78,99, azul celeste, selo mais vendido.
Cor preta R$ 98 · outra variação R$ 90,55 — **diferença de até R$ 20 pela cor**, avisado no card.

## Faixa histórica (mar–ago/2026)
Piso R$ 77,89 (KaBuM) · R$ 104,90 em 27/03 (Amazon) · R$ 113,99 em 01/12 (Magalu) · hoje R$ 78,99.
**Está no piso — não há motivo para esperar queda.**

## 🔴 Pendência
Subir **dump de avaliações do Redmi** (Amazon + ML) para converter "Limitações conhecidas" em
frequência real, como foi feito em 3523/3527/3545. Enquanto não houver, a seção permanece declarada
como dedutiva.

## Validação
JSON-LD válido (4 tipos) · 0 offers/aggregateRating/priceValidUntil · 8 afiliados, 100% com `rel`
completo · tags balanceadas · 0 base64 · 0 "compra verificada" · 0 menção a Dia dos Pais.
