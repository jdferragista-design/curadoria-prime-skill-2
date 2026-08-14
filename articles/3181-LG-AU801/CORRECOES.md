# Post 3181 · LG AU801 50" — pacote completo de correções

`/lg-au801-50-review` · auditado sobre o HTML publicado em 13/08/2026

Ordem sugerida: **1 → 8**. Os itens 1, 2 e 3 são os de risco real (alegação
enganosa e dados errados); do 4 em diante é higiene técnica.

---

## ✅ O que já está certo (não mexer)

- **8 links de afiliado**, todos com `rel="sponsored noopener noreferrer nofollow"`.
- **Bloco de divulgação** presente, com "sem custo adicional".
- Seção de **contras** e **FAQ** existem.

---

## 🔴 1. Urgência fabricada — REMOVER

**Localize:**

```html
<p style="font-size: 12px; color: #e11d48; font-weight: bold; margin: 10px 0 0;">⏰ Preço verificado há 2 horas | Estoque limitado</p>
```

**Substitua por:**

```html
<p style="font-size: 12px; color: #64748b; margin: 10px 0 0;">Faixa de preço observada em <strong>13/08/2026</strong>: <strong>R$ 1.973 a R$ 2.088</strong>. Marketplaces mudam preço sem aviso — confira o valor na loja antes de comprar.</p>
```

**Por quê:** "há 2 horas" é falso por construção (nada revalida o preço de hora
em hora) e fica **congelado** — daqui a seis meses ainda dirá "há 2 horas".
"Estoque limitado" é escassez inventada: você não enxerga o estoque de Amazon
nem de Mercado Livre. CDC art. 37, §1º.

Repare que o vermelho `#e11d48` reforça a urgência. Trocado por cinza neutro.

---

## 🔴 2. Preço errado em 6 lugares

Você coletou hoje: **Amazon R$ 2.088,10** · **Mercado Livre R$ 1.973 (Pix)**.
O artigo afirma **R$ 1.941** — valor pelo qual ninguém consegue comprar.

| # | Onde | Trocar |
|---|---|---|
| 1 | Introdução | "O preço está em torno de R$ 1.941" → **"O preço fica entre R$ 1.973 e R$ 2.088 (agosto/2026)"** |
| 2 | Abertura da análise | "A LG AU801 50″ custa R$ 1.941" → **"custa a partir de R$ 1.973"** |
| 3 | Box de CTA | "Preço de referência: ~R$ 1.941" → usar o bloco do item 1 |
| 4 | Tabela de specs | "Preço médio ~R$ 1.941" → **"R$ 1.973 – R$ 2.088"** |
| 5 | Tabela comparativa | "Preço R$ 1.941" → **"R$ 1.973"** |
| 6 | Box final | "~R$ 1.941" → **"a partir de R$ 1.973"** |

### ⚠️ Efeito dominó na conclusão

O texto diz: *"A Philips 7019 vence em preço (**R$ 47 mais barata**)"*.
Esse R$ 47 vem de `1.941 − 1.894`. Com o preço real, a diferença é **R$ 79**.

E confira se R$ 1.894 (Philips) e R$ 2.154 (Samsung) ainda valem — se saíram da
mesma coleta do R$ 1.941, a tabela comparativa inteira está defasada.

**Localize também:**

```html
<p style="font-size: 12px; color: rgba(255,255,255,.5); margin: 14px 0 0;">Preços verificados em Julho/2026 — sujeitos a alteração.</p>
```

Atualize para **Agosto/2026**. (Este aqui está no formato certo: data fixa.)

---

## 🔴 3. Alegação de teste físico

**Localize:**

```html
<p class="wp-block-paragraph">Para este review, analisamos as <strong>especificações técnicas oficiais</strong>, cruzamos com os <strong>relatos reais de mais de 815 compradores verificados</strong> e testamos os pontos mais críticos — especialmente o upscaling, que é onde a LG AU801 realmente se destaca. Muitos leitores nos perguntam: <strong>LG AU801 vale a pena</strong> o investimento? Vamos aos dados.</p>
```

**Substitua por:**

```html
<p class="wp-block-paragraph">Para este review, analisamos as <strong>especificações técnicas oficiais</strong>, cruzamos os <strong>relatos de compradores verificados</strong> nos principais varejistas e comparamos os resultados com as medições publicadas por laboratórios independentes — com foco no upscaling, que é onde a LG AU801 se destaca. Muitos leitores nos perguntam: <strong>LG AU801 vale a pena</strong> o investimento? Vamos aos dados.</p>
```

**Por quê:** "testamos os pontos mais críticos" afirma teste físico que não
houve. A versão nova descreve a metodologia real — análise documental + agregação
de relatos + laboratórios de terceiros — que é legítima e ainda atende o "Como"
do framework E-E-A-T do Google. Note que ela também remove o "815" (ver item 4).

---

## 🔴 4. O número 815 é falso — o print da Amazon prova

O anúncio que você colou mostra:

```
4,6 de 5 estrelas   (50)
```

O post afirma **815 avaliações**. A **nota bate** (4,6), a **contagem está
inflada em 16×**. Guarde esse print: é a prova de que os `reviewCount` do site
foram inventados, e valida a remoção do `aggregateRating` nos 48 posts.

**Localize:**

```html
<p class="wp-block-paragraph">Nos principais sites (Mercado Livre, Amazon BR, Magazine Luiza), a <strong>LG AU801</strong> acumula cerca de 815 avaliações com média 4.6.</p>
```

**Substitua por:**

```html
<p class="wp-block-paragraph">Na Amazon BR, a <strong>LG AU801</strong> registra média <strong>4,6 de 5</strong> em 50 avaliações (consulta em 13/08/2026). O volume ainda é baixo, então trate a nota como indicativa, não como consenso consolidado.</p>
```

Admitir amostra pequena constrói mais confiança do que inflar o número — e é
verificável por qualquer leitor.

**Há mais um:** na tabela comparativa, a linha `Reviews 815 / 194 / 9.091`.
Corrija o 815 para 50, e confira os outros dois — provavelmente vieram da mesma
fonte inventada. Se não conseguir confirmar, **remova a linha inteira**.

---

## 🔴 5. Dois JSON-LD quebrados pela aspa de `50"`

Além do bloco que já sabíamos, descobri que **o schema do Rank Math também está
quebrado** — e pelo mesmo motivo:

```
"name": "LG AU801 50" Vale a Pena? Review 2026"
                    ↑ a aspa das polegadas fecha a string
```

| Bloco | Origem | Estado |
|---|---|---|
| `[0]` | Rank Math | 🔴 quebrado — `50"` no `name` do WebPage |
| `[1]` | manual (`TechArticle`) | 🔴 quebrado — `50"` no `headline` |
| `[2]` | manual (`Product`) | ⚠️ wpautop (`<br />`) — corrigido em `3181-COLAR-NO-WP.html` |
| `[3]` | manual (`FAQPage`) | ⚠️ wpautop (`<br />`) |

**Resultado: o post não tem NENHUM dado estruturado válido hoje.** Nem Product,
nem FAQ, nem breadcrumb, nem Article.

**Correção do título (resolve os blocos 0 e 1 de uma vez):**
no Rank Math, troque o título SEO de

```
LG AU801 50" Vale a Pena? Review 2026
```

para

```
LG AU801 50 polegadas Vale a Pena? Review 2026
```

Use `50 polegadas` ou `50″` (aspa tipográfica U+2033) — **nunca** `"` reto. O
`<h1>` do post já usa `50″` corretamente; o problema está só no título SEO/og.

---

## 🔴 6. Schema: `aggregateRating` e preços dos concorrentes

O `Product` declarava:

```json
"aggregateRating": { "ratingValue": "4.6", "reviewCount": "815" },
"offers": { "lowPrice": "1894", "highPrice": "2154" }
```

Dois erros: o rating inventado (item 4) e — mais sutil — **R$ 1.894 é a Philips
e R$ 2.154 é a Samsung**. Alguém copiou a faixa da tabela comparativa para
dentro da oferta deste produto. Declarar preço de concorrente como oferta
própria é erro de dados estruturados e pode gerar aviso no Search Console.

**Já corrigido** em `3181-COLAR-NO-WP.html`:

```json
"offers": { "lowPrice": "1973", "highPrice": "2088", "offerCount": "2" }
```

Sem `aggregateRating`. O `review` 8.4/10 (sua nota editorial) foi preservado.

---

## ⚠️ 7. `author` no schema

O bloco `TechArticle` traz `"name": "Cristiano"`. O canônico do projeto é
**`Cristiano Martins`**. Como o bloco está quebrado (item 5), o script não
consegue corrigir sozinho — ajuste junto com o título.

O `meta twitter:data1` também diz `Cristiano`; isso vem do perfil do WordPress.
Vale padronizar o nome de exibição do usuário para consertar em todo o site.

---

## ⚠️ 8. `datePublished` com fuso errado

```json
"datePublished": "2026-01-27T08:00:00+03:00"
```

`+03:00` é Moscou. O Brasil é **`-03:00`**. Erro de sinal — provavelmente na
geração do bloco. Corrija junto com o item 5.

---

## Checklist de aplicação

- [ ] 1. Remover "verificado há 2 horas | Estoque limitado"
- [ ] 2. Corrigir R$ 1.941 → faixa real (6 lugares) + recalcular o "R$ 47"
- [ ] 3. Reescrever o parágrafo do "testamos"
- [ ] 4. Corrigir 815 → 50 avaliações (2 lugares: texto + tabela)
- [ ] 5. Trocar `50"` por `50 polegadas` no título SEO (Rank Math)
- [ ] 6. Colar `3181-COLAR-NO-WP.html` no lugar do bloco Product
- [ ] 7. Corrigir `Cristiano` → `Cristiano Martins`
- [ ] 8. Corrigir `+03:00` → `-03:00`

### Validar depois

```bash
curl -s https://curadoriaprime.com/lg-au801-50-review/ | grep -c "1.941\|verificado há\|Estoque limitado\|aggregateRating"
```

Esperado: **0**.

E em <https://search.google.com/test/rich-results>: `Product` sem estrela
agregada, com `review`; `FAQPage` detectado **pela primeira vez**.
