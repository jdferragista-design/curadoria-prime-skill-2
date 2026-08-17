# ESTADO — CLUSTER ÁUDIO (3523 · 3545 · 3527)

**Status:** 🔧 EM EXECUÇÃO (17/08/2026) — 3527 ✅ ENTREGUE · 3545 ⏸️ aguarda confirmação · 3523 ⏳ na fila
**Modo de trabalho:** 3 por vez (mudança de cadência pedida pelo cliente em 17/08)

| # | Slug | Produto principal | Risco CSV | Alegações | Links sem sponsored |
|---|---|---|---|---|---|
| 3523 | `qcy-t13-anc-review-2026-vale-a-pena` | QCY T13 ANC | 21 (o pior da fila) | 7 | 0/6 |
| 3545 | `samsung-galaxy-buds-core-vale-a-pena` | Samsung Galaxy Buds Core | 13 | 2 | 1/7 |
| 3527 | `edifier-w820nb-review-2026-vale-a-pena` | Edifier W820NB | 3 | 1 | 0/4 |

---

## 0. Por que estes três juntos

Os três são **o mesmo cluster de áudio** e se citam mutuamente. Cada um usa os
outros dois como "alternativa" no bloco de compra:

- **3523 (QCY)** → card alternativa **Galaxy Buds Core**
- **3545 (Buds Core)** → cards alternativa **QCY T13 ANC** + **Edifier W820NB**
- **3527 (Edifier)** → cita **Galaxy Buds Core** e **QCY T13 ANC** no resumo

Os três apontam para o guia-mãe `melhor-fone-bluetooth-ate-500-reais-2026` (3336,
já corrigido em 14/08) e para os mesmos 2 posts irmãos (Redmi Buds 6 Play `3548`,
JBL Wave Buds 2 `3550`).

**Consequência prática:** uma captura de preço serve aos 3; uma decisão sobre nota
e sobre citação de compradores serve aos 3; e **um preço errado num deles
contamina os outros dois**. Corrigir isoladamente geraria divergência entre posts.

---

## 1. 🔴 ACHADO CRÍTICO — o preço do Edifier W820NB está errado nos 3 posts

Este é o problema mais grave do lote e o motivo mais forte para tratá-los juntos.

| Onde | Preço publicado | Preço real (17/08/2026) |
|---|---|---|
| 3527 (review do Edifier) | "~R$ 399" (hero, resumo, specs, schema) | **Amazon: "Não disponível" (esgotado)** · **ML: R$ 708,39, "último disponível"** |
| 3545 (card alternativa) | "Edifier W820NB ~R$ 399" | idem |
| 3336 (guia-mãe, já corrigido) | "R$ 355,49 (KaBuM) / R$ 422,90 (Amazon branco)" | idem |
| 3523 (menção no texto) | "Edifier W820NB (38dB, over-ear, **R$ 399**)" ×2 | idem |

O produto **saiu de linha ou está em ruptura**: a Edifier lançou o **W820NB Plus V25**
(Bluetooth 6.1, R$ 499 Amazon / R$ 499 ML) como sucessor. O anúncio ML de R$ 708,39
é revenda de estoque residual — quase **78% acima** do preço publicado.

Isso é **gatilho de nível 1 da §17.2** (produto esgotado + variação >20% + sucessor
lançado) → revisão obrigatória em 7 dias e **bloco de compra suspenso** (§17.1 VERMELHO).

**Decisão necessária do cliente** (ver §6, item 1).

---

## 2. Problemas por artigo

### 2.1. 3523 — QCY T13 ANC (o pior da fila)

**Alegações de teste:** o CSV registra 7 ("testamos", "unboxing", "usamos o fone por").
✅ **Boa notícia: já foram corrigidas.** O post foi reescrito em 15/08 e hoje traz
box de metodologia honesto ("não tivemos o produto em mãos"), seção renomeada para
"O Que Vem na Caixa" e a ressalva explícita *"O que depende de ter o produto no
ouvido […] nós não verificamos"*. **O CSV está desatualizado para este item.**

**O que AINDA está errado:**

1. 🔴 **4 depoimentos com aspas + "compra verificada"** no bloco "O que dizem os
   compradores" (2 Amazon, 2 ML, com datas mai/2026, fev/2024, set/2024, mai/2024).
   Fere §4.2 (transformar paráfrase em citação; "compradores verificados" sem selo).
   O termo "avaliações **verificadas**" aparece ainda **6×** no corpo.
2. 🔴 **JSON-LD com `priceValidUntil: "2026-12-31"`** — data futura inventada (§2.5).
3. 🔴 **`availability: InStock`** em 3 lugares (AggregateOffer + 2 Offers) — não verificado.
4. 🟡 `AggregateOffer` com `lowPrice 169.00` / `highPrice 186.10` — a estrutura está
   correta (o outro chat recomendou AggregateOffer para faixa), mas os valores são de
   15/08 e o ML hoje está **R$ 199** (subiu 18%). Precisa recaptura.
5. 🟡 **FAQ do schema ≠ FAQ visível**: o schema tem "Qual a diferença do T13 ANC para
   o T13 ANC 2?" que **não existe** na página; a página tem "O ANC é eficiente no
   transporte público?" que não está no schema. Google penaliza FAQ que não corresponde.
6. 🟡 Preço no texto ("R$ 169–186", "R$ 169-186" ×4) desatualizado.
7. 🟢 Links: os 4 de afiliado **já têm** `rel="sponsored nofollow noopener"` — o CSV
   dizia 0/6. Falta só o padrão completo `noreferrer`.

**Já OK:** autor canônico, "Fontes consultadas", box de metodologia, "não indica para
quem", nota 8,5/10, BreadcrumbList `audio-e-som`.

### 2.2. 3545 — Samsung Galaxy Buds Core (o mais grave em veracidade)

1. 🔴 **ALEGAÇÃO DE TESTE FÍSICO EXPLÍCITA E DETALHADA** — o pior caso do lote:
   > *"Para responder com precisão, **testamos o Galaxy Buds Core durante duas semanas
   > em três cenários reais**: Ecossistema Samsung completo: **Galaxy S25**… Android de
   > outra marca: **Xiaomi 14T**, para medir… **iPhone 15**…"*

   E ainda: *"**Testamos** em quatro cenários reais de chamada durante duas semanas"*
   (com tabela de 4 cenários e estrelas), *"Durante os **testes de conforto**… em
   sessões de até 3 horas contínuas"*, *"Em treinos na academia com corrida e
   agachamento, o fone se manteve firme… algo que **não aconteceu com o QCY T13 ANC
   no mesmo teste**"*, *"**Nos nossos testes** com português–inglês e português–espanhol"*.
   → Narra teste comparativo de 2 unidades que não existiu. **CDC art. 37.**
2. 🔴 **"unidade adquirida pelo autor"** no rodapé — declaração de posse do produto
   que contradiz a política padrão (§2.1) e não tem as 8 evidências da §2.2.
3. 🔴 **Tabela de chamadas inteira é ficção**: 4 cenários (home office, café lotado,
   ônibus, rua com vento) com nota em estrelas e "feedback dos participantes" entre
   aspas — *"Parece presença física — melhor fone de reunião que já ouvi nessa faixa"*,
   *"Não ouço nada do café — você está em silêncio. Impressionante"*. Sem fonte.
4. 🔴 **7+ citações de compradores entre aspas** sem link/data verificável, incluindo
   *"corri 1hr de esteira e não saiu"*, *"Carreguei a caixinha dia 24/12… dia 31/12
   ainda está em 74%"*, *"a conexão e qualidade do som do Core é superior"*.
5. 🔴 **"dados de compradores verificados"** no box de transparência + *"Todas as
   citações são de compras verificadas"* na nota de IA.
6. 🔴 **Box "avaliações analisadas com IA"** afirma *"Os dados complementam — mas não
   substituem — os **testes práticos realizados pela nossa equipe editorial**"* →
   afirma equipe de testes que não existe.
7. 🟡 **`<br />` injetado dentro dos cards de compra** (`</span><br />\n<a style=…`) —
   o wpautop já corrompeu o HTML; é o problema documentado na MEMÓRIA §10.3.
8. 🟡 Nota dupla (9,0/10 Samsung · 7,8/10 outros) — padrão da sessão é nota única.
9. 🟡 "Última atualização: **Março de 2026**" — mas o post foi modificado depois.
10. 🟡 Preço "R$ 229–270" desatualizado (hoje **R$ 219,31 Pix / R$ 243,68** Amazon).
11. 🟢 Links: 6 dos 7 já com `rel="sponsored nofollow noopener"`.
12. ❌ **Sem bloco de autor canônico** (o 3523 e o 3527 têm).
13. ❌ **Sem "Fontes consultadas"**.
14. ❌ **Sem box "Tipo de análise"**.

### 2.3. 3527 — Edifier W820NB

1. 🔴 **Preço/estoque completamente defasado** (ver §1) — o mais urgente.
2. 🔴 **`priceValidUntil: "2026-08-31"`** no schema — vence em 14 dias e o produto
   nem está disponível (§2.5).
3. 🔴 **`availability: InStock`** + `price: "399.00"` fixo apontando para `amzn.to/3MYWbfZ`,
   que hoje resolve para uma página **"Não disponível"**.
4. 🔴 **`author.url` = `/author/cristian/`** — slug antigo, o mesmo bug já registrado no
   4537 (MEMÓRIA §11).
5. 🔴 **`@id` e `mainEntityOfPage` apontam para `/edifier-w820nb-review-2026/`** — URL
   que **não é** a do post (o slug real é `edifier-w820nb-review-2026-vale-a-pena`).
6. 🟡 **"dados agregados de compradores verificados"** no box de tipo de análise +
   "avaliações de compradores verificados" ×3 no corpo.
7. 🟡 Seção "📦 Unboxing: o que vem na caixa" — o conteúdo é honesto (lista da
   embalagem oficial), mas o **título "Unboxing"** dispara a regra §2.1 e é o que o
   CSV pegou. Renomear para "O que vem na caixa".
8. 🟡 `logo.url` = `/wp-content/uploads/logo-curadoria-prime.png` — caminho sem ano,
   provavelmente 404 (os outros posts usam `/2026/03/cropped-logo-…webp`).
9. 🟡 Bluetooth 5.0 na descrição do schema vs "Bluetooth 5.4" do sucessor — conferir
   se a ficha ainda bate com o que é vendido.
10. 🟢 Já tem: autor canônico, "Fontes consultadas" com links diretos (Tecnoblog,
    Prime Audio, Oficina da Net), box "não testamos esta unidade fisicamente",
    "Para quem é (ou não)", `reviewRating` 8,8/10 com `worstRating`.

---

## 3. Problema TRANSVERSAL aos três: links internos inconsistentes

Os três usam **slugs curtos** que redirecionam (301) em vez do slug canônico:

| Slug usado nos links | Slug canônico real |
|---|---|
| `/qcy-t13-anc-review/` | `qcy-t13-anc-review-2026-vale-a-pena` |
| `/edifier-w820nb-review/` | `edifier-w820nb-review-2026-vale-a-pena` |
| `/redmi-buds-6-play-review/` | `redmi-buds-6-play-review-2026-vale-a-pena` |
| `/jbl-wave-buds-2-review/` | `jbl-wave-buds-2-review-2026-vale-a-pena` |

Não são 404 (resolvem por redirect), mas cada salto custa crawl budget e dilui
sinal interno. Padronizar para o slug canônico nos três posts.

---

## 4. Capturas de mercado — 17/08/2026

| Produto | Amazon BR | Mercado Livre | Δ vs publicado |
|---|---|---|---|
| **QCY T13 ANC** | `B0BWRBKMCK` — **R$ 186,10** (4,7/5 · 4.423 aval. no ASIN irmão B0BX9G9C78) | **MLB34102640** (oficial QCY) — **R$ 199** (de R$ 269,90, 26% OFF) · 12× R$ 19,70 | ML **+18%** (era R$ 169) |
| **Galaxy Buds Core** | `B0FP8KDP36` — **R$ 219,31 Pix/NuPay** · R$ 243,68 normal · em estoque, entrega grátis | **MLB57492226** (branco) — **R$ 243,68** (de R$ 399, 38% OFF) · preto MLB52845211 R$ 279,37 Pix | dentro da faixa, mas **mais barato** que o publicado |
| **Edifier W820NB** | `B09MDC77QX` — ⛔ **"Não disponível. Não temos previsão"** | **MLB19052273** — **R$ 708,39** · "último disponível" | 🔴 **+78%** e sem estoque |
| *Sucessor* **W820NB Plus V25** | `B0G534R9BZ` — R$ 499 (4,8/5 · 26 aval.) | **MLB63419175** — R$ 499 | novo |

**Alternativas de mesma faixa vistas hoje (para a seção do Edifier, se o cliente quiser):**
Edifier W800BT Pro R$ 284,05 Pix (ML) / R$ 299 (Amazon) · Edifier WH700NB Pro R$ 349 ·
JBL Tune 780NC R$ 397 (ML) · Soundcore P30i R$ 210 (ML).

---

## 5. Plano de correção do lote (após aprovação)

**Ordem:** 3527 (Edifier) → 3545 (Buds Core) → 3523 (QCY). O Edifier primeiro porque
a decisão sobre ele muda o texto dos outros dois.

**Comum aos três:**
1. Preços em faixa com data 17/08/2026; remover todo `priceValidUntil` e `availability`.
2. `rel="sponsored noopener noreferrer nofollow"` em 100% dos links.
3. "compradores verificados"/"avaliações verificadas" → "avaliações publicadas por compradores".
4. Citações entre aspas sem fonte → "Síntese editorial dos relatos".
5. Links internos → slug canônico.
6. JSON-LD parseado → mutado → redumpado, em `<!-- wp:html -->` sem `<br/>`.
7. Nota única /10; "Pontos de Atenção" (h4 + ul ≥3); "para quem NÃO é".
8. Validar cada arquivo: `python3 tools/checar_conformidade.py articles/<arquivo>.html`.

**Específico 3527:** decidir destino do produto (ver §6.1); corrigir `author.url`,
`@id`/`mainEntityOfPage`, `logo.url`; "Unboxing" → "O que vem na caixa".

**Específico 3545:** remover TODA a narrativa de teste de 2 semanas (3 cenários +
tabela de 4 chamadas + testes de conforto + teste do Intérprete); remover "unidade
adquirida pelo autor"; adicionar box "Tipo de análise", autor canônico e "Fontes
consultadas"; refazer os cards corrompidos por `<br/>`; nota única.

**Específico 3523:** remover os 4 depoimentos com aspas; alinhar FAQ do schema com a
FAQ visível; recapturar preço; trocar `availability`/`priceValidUntil`.

---

## 6. Pendências do CLIENTE (bloqueiam a entrega)

1. 🔴 **Edifier W820NB — decidir o destino do post 3527.** O produto está esgotado na
   Amazon e a R$ 708 no ML (era R$ 399), com sucessor W820NB Plus V25 a R$ 499.
   Três caminhos possíveis:
   - **(a)** manter o review com **bloco de compra suspenso** ("consultar preço atual")
     + aviso de fim de linha + apontar o Plus V25 como opção — igual ao que fizemos na
     Philips 50PUG7019 → 7300;
   - **(b)** manter e **trocar o produto principal** para o W820NB Plus V25 (exige
     pesquisa nova de ficha técnica e shortlinks novos);
   - **(c)** manter só como conteúdo histórico, sem CTA.
   👉 Minha recomendação: **(a)** — preserva o SEO da URL e repete um padrão que já
   funcionou no site.
2. 🔴 **Shortlinks de afiliado para o W820NB Plus V25** (Amazon `B0G534R9BZ` + ML
   `MLB63419175`), caso escolha (a) ou (b).
3. 🔴 **3545 — confirmar que NÃO houve teste físico.** O post afirma "unidade adquirida
   pelo autor" e descreve 2 semanas de testes com Galaxy S25, Xiaomi 14T e iPhone 15.
   Se isso **realmente aconteceu**, preciso das 8 evidências da §2.2 (nome, datas,
   origem da unidade, variante, protocolo, medições, fotos originais, limitações) para
   manter o texto com o selo "Testado por nós". **Sem essas evidências, removo tudo.**
4. 🟡 **Notas duplas** (3545: 9,0/7,8 · 2888: 7,5/6,0) — unificar em nota única?
5. 🟡 **Redmi Buds 6 Play (3548) e JBL Wave Buds 2 (3550)** completam este cluster e
   têm os mesmos vícios. Entram no próximo lote de 3?


---

## 7. ✅ 3527 (Edifier W820NB) — ENTREGUE em 17/08/2026

**Arquivo:** `articles/edifier-w820nb-review-2026-vale-a-pena.html`
**Decisão do cliente:** caminho **(a)** — mesmo padrão da Philips 50PUG7019 → 50PUG7300.

### O que foi feito

| # | Correção |
|---|---|
| 1 | **Bloco de compra SUSPENSO** (§17.1, estado VERMELHO). Aviso de fim de linha no topo, com os números da verificação: Amazon "Não disponível", ML R$ 708,39 "último disponível", faixa histórica R$ 355–423 e o cálculo do desvio (~78%). |
| 2 | **Sucessora W820NB Plus V25 como OPÇÃO** (R$ 499 nas duas lojas) + gancho "Em breve: review dedicado" — igual ao 3183. |
| 3 | Seção "O que comprar hoje" com 3 cards: Plus V25 (sucessora), W800BT Pro (over-ear mais barato, R$ 284–299) e Galaxy Buds Core (TWS, R$ 219–244). |
| 4 | Todos os "~R$ 399" fixos removidos do corpo → faixa histórica com data. |
| 5 | "Unboxing" → **"O que vem na caixa"**. |
| 6 | "compradores verificados" / "avaliações verificadas" → "avaliações publicadas por compradores" (0 no corpo). |
| 7 | "Pontos negativos" → **"Pontos de Atenção"** (h4 + ul, 8 itens, com o fim de linha em primeiro). |
| 8 | 6 links de afiliado + 2 de fonte com `rel="sponsored noopener noreferrer nofollow"`; fontes editoriais com `noopener noreferrer`. |
| 9 | Links internos nos **slugs canônicos** (eram 4 slugs curtos com 301). |
| 10 | Nota **8,8/10 mantida, mas explicitamente atribuída ao produto no preço histórico** + novo card "Disponibilidade 3,0/10" no painel do veredito. |
| 11 | **JSON-LD reconstruído** (parse → mutação → redump), em `wp:html` sem `<br/>`. Corrigidos: `author.url` (era `/author/cristian/`), `@id` e `mainEntityOfPage` (apontavam para `/edifier-w820nb-review-2026/`, slug inexistente), `logo.url` (caminho sem ano, 404). Removidos `offers`, `price`, `availability` e `priceValidUntil`. |
| 12 | FAQ do schema **alinhada com a FAQ visível** (5 perguntas iguais nos dois), incluindo a nova "Ainda dá para comprar?". |
| 13 | "Fontes consultadas" ampliada com as páginas de produto das duas lojas + data de consulta. |

### Validação

```
python3 tools/checar_conformidade.py articles/edifier-w820nb-review-2026-vale-a-pena.html
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 8/8 · divulgação antes dos links · autoria · metodologia ·
honestidade · fontes (~11 itens) · data · teste-fisico 0 ·
profundidade 4.331 palavras · valor-agregado completo · imparcialidade 7 contras ·
enchimento OK · keyword-stuffing OK · schema válido.
```

Verificação independente: JSON-LD parseia (Article + Review + FAQPage + BreadcrumbList);
zero `aggregateRating`/`ratingCount`/`reviewCount`/`offers`/`priceValidUntil`/`availability`;
zero `<br/>` dentro do `<script>`; zero base64; zero `data-src`; balanço de tags fechado
(div 56/56 · p 96/96 · li 50/50 · a 46/46 · table 5/5 · script 1/1); nenhum slug com 301.

### Pendência do cliente para este post

- **Shortlinks de afiliado da W820NB Plus V25** — o arquivo usa as URLs canônicas
  (`amazon.com.br/dp/B0G534R9BZ` e `mercadolivre.com.br/p/MLB63419175`) como fallback,
  já com `rel` correto. Trocar pelos shortlinks quando gerá-los.
- Mesma coisa para o W800BT Pro (`B0DF5NF475` / `MLB41983700`).
