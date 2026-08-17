# ESTADO — CLUSTER ÁUDIO (3523 · 3545 · 3527)

**Status:** 🔧 EM EXECUÇÃO (17/08/2026) — 3527 ✅ ENTREGUE · 3545 ✅ ENTREGUE · 3523 ⏳ próximo
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


---

## 8. ✅ 3545 (Samsung Galaxy Buds Core) — ENTREGUE em 17/08/2026

**Arquivo:** `articles/samsung-galaxy-buds-core-vale-a-pena.html`
**Decisão do cliente (17/08):** *"se a afirmação não for de reviews de terceiros, não"* —
ou seja, **não houve teste próprio**. Toda narrativa em 1ª pessoa foi removida; o que era
atribuível a terceiros foi mantido com a fonte nomeada.

### Alegações de teste REMOVIDAS (as 14 do diagnóstico)

| Trecho publicado | Tratamento |
|---|---|
| "testamos o Galaxy Buds Core durante **duas semanas em três cenários reais**" + lista Galaxy S25 / Xiaomi 14T / iPhone 15 | **removido**; substituído por "As seções a seguir separam, recurso por recurso, o que é universal e o que é exclusivo — com base na documentação oficial da Samsung e nos relatos publicados nas lojas" |
| "**Testamos** em quatro cenários reais de chamada durante duas semanas" + tabela de 4 cenários com falas de participantes entre aspas | **tabela removida** → "Síntese editorial dos relatos" descrevendo os padrões (silêncio, ambiente movimentado, vento) sem aspas e sem nota em estrelas |
| "Durante os **testes de conforto** … sessões de até 3 horas contínuas" | **removido** → síntese dos relatos sobre encaixe, incluindo o contraponto de orelhas menores |
| "Em treinos na academia … algo que **não aconteceu com o QCY T13 ANC no mesmo teste**" | **removido** — era comparativo físico de 2 unidades |
| "**Nos testes** com português–inglês e português–espanhol, a latência ficou abaixo de 2 segundos" | → "A Samsung indica suporte a português brasileiro como idioma de origem e destino" |
| "**Nos testes**, o Auto Switch funcionou … menos de 3 segundos" | → "Nos relatos publicados por compradores que usam aparelhos Galaxy, é apontado como um dos recursos que mais economizam tempo" |
| "🔋 **Autonomia real medida** (volume 60%)" | → "**Autonomia declarada pelo fabricante**" + nota "Não realizamos medição própria de bateria" |
| "os dados complementam mas não substituem os **testes práticos realizados pela nossa equipe editorial**" | → "São relatos de terceiros publicados nas lojas — não substituem teste próprio, que não foi realizado para este review" |
| rodapé "Produto analisado: … **(unidade adquirida pelo autor)**" | **removido** |

**Verificação:** `duas semanas`, `Galaxy S25`, `Xiaomi 14T`, `iPhone 15`, `testes de conforto`,
`no mesmo teste`, `Nos testes`, `unidade adquirida`, `equipe editorial`, `Autonomia real`,
`medida`, `medir` → **0 ocorrências no corpo**. O único "testamos" é a negação
"não testamos esta unidade fisicamente".

### Demais correções

- **7+ citações entre aspas** sem fonte → "Síntese editorial dos relatos", sem aspas.
  Restam 3 pares de aspas no corpo, todos legítimos: o selo "Testado por nós", o selo
  "Escolha da Amazon" e o acabamento "black piano".
- "dados de compradores verificados" e "Todas as citações são de compras verificadas" →
  "avaliações publicadas por compradores" (**0 ocorrências** dos termos proibidos).
- **Box "Tipo de análise" adicionado** (não existia).
- **Bloco de autor canônico adicionado** (não existia).
- **"Fontes consultadas" adicionada** (não existia): Samsung oficial, documentação do
  Galaxy AI, páginas de produto das duas lojas com data.
- **Seção "Para quem é (e para quem NÃO é)" criada** — o artigo não tinha o "para quem NÃO é".
- "Limitações" → **"Pontos de Atenção"** (h4 + ul, 8 itens; incluído o da asa de tamanho único).
- **Nota dupla 9,0/7,8 → nota única 8,5/10**, com a diferença por perfil explicada no texto.
  ⚠️ **Confirmar com o cliente.**
- Preços em faixa com data: **R$ 219,31 Pix (Amazon) · R$ 243,68 · R$ 279,37 Pix (ML preto)**.
  O publicado dizia "R$ 229–270" e "Última atualização: Março de 2026".
- **Cards de compra refeitos** — o publicado já tinha `<br />` injetado pelo wpautop dentro
  dos `<div>` de botão.
- Links internos → **slugs canônicos** (eram `/qcy-t13-anc-review/` e `/edifier-w820nb-review/`).
- **Card do Edifier convertido em aviso de fim de linha**, apontando para o 3527 corrigido —
  os dois posts do lote agora contam a mesma história sobre o W820NB.
- Removido o link genérico `mercadolivre.com.br` da abertura (era marcado como sponsored
  sem ser link de produto).
- **JSON-LD criado do zero** (o publicado não tinha nenhum): Article + Review (8,5/10 com
  `worstRating`, **sem offers**) + FAQPage + BreadcrumbList, em `wp:html` sem `<br/>`.

### Validação

```
python3 tools/checar_conformidade.py articles/samsung-galaxy-buds-core-vale-a-pena.html
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 7/7 · divulgação antes dos links · autoria · metodologia · honestidade ·
fontes (~21 itens) · data · teste-fisico 0 · profundidade 4.848 palavras ·
valor-agregado completo · imparcialidade 8 contras · enchimento OK · schema válido.
```

Verificação independente: JSON-LD parseia (Article + Review + FAQPage + BreadcrumbList);
zero `aggregateRating`/`offers`/`priceValidUntil`/`availability`; zero `<br/>` no `<script>`;
zero base64; zero `data-src`; balanço de tags fechado (div 58/58 · p 68/68 · li 53/53 ·
a 38/38); nenhum slug com 301.

> Nota sobre os 2 alertas iniciais: a primeira rodada acusou `[enchimento] 'ecossistema' 16×`
> e `[valor-agregado] faltam prós e contras / para quem NÃO é`. Resolvidos variando a
> redação ("linha Galaxy", "aparelhos Galaxy", "integração Samsung") e criando a seção
> "para quem NÃO é" — que de fato faltava no publicado.

### Pendência do cliente para este post

- **Confirmar a nota única 8,5/10** (substitui "9,0/10 Samsung · 7,8/10 outros").
- Conferir o título SEO/Rank Math: verificar se não promete teste próprio.
- O `<style>` inline do topo do post publicado permanece no painel — não foi duplicado
  neste arquivo.


---

## 9. 🔄 REVISÃO do 3527 (17/08, após feedback do cliente) — card de compra MANTIDO

**Instrução do cliente:** *"O card do Edifier mantém, só que com o branco, como fizemos
no Top 5 Melhores Fones até R$ 500 — e aviso para a nova versão."*

### O que a verificação mostrou

O diagnóstico da §1 estava **incompleto**: eu havia checado apenas o ASIN `B09MDC77QX`,
que é a **cor cinza**. Conferindo o link que o Top 5 já usava (`link.amazon/B06vz0YO0`),
ele resolve para outro ASIN — **`B09HR1B9RW`, a cor branca**:

| Cor | ASIN | Situação em 17/08/2026 |
|---|---|---|
| **Branco** | `B09HR1B9RW` | ✅ **R$ 437,57**, em estoque, vendido e entregue pela Amazon, 4,7/5 em ~1.483 avaliações |
| Cinza | `B09MDC77QX` | ⛔ "Não disponível" na Amazon · R$ 708,39 no ML ("último disponível") |
| Plus V25 (nova versão) | `B0G534R9BZ` | R$ 499 nas duas lojas |

Ou seja: **o produto não saiu do mercado — saiu a cor cinza.** A conclusão anterior de
"suspender o bloco de compra" era baseada em amostra incompleta.

### Mudanças aplicadas

- **Bloco de compra restaurado**, apontando só para a **cor branca** via
  `link.amazon/B06vz0YO0` — exatamente o link já validado no guia Top 5.
- **Aviso de cor em 4 pontos** (hero, box do topo, bloco de compra e specs): a branca é a
  recomendada; a cinza saiu de linha e o estoque restante é vendido ~60% acima da faixa.
- **Aviso da nova versão** W820NB Plus V25 (R$ 499, Bluetooth 6.1) como card de opção,
  com o gancho "Em breve: review dedicado" — padrão da Philips 7019 → 7300.
- Faixa histórica corrigida de "R$ 355–423" para **R$ 355–437**.
- Nota geral **8,8/10 mantida**; o card "Disponibilidade" subiu de 3,0 para **6,0/10**
  ("só na cor branca").
- Verificação: **0 ocorrências** de "fim de linha" e "suspenso" no corpo do 3527.

### Espelhamento no 3545

O card do Edifier no Galaxy Buds Core voltou a ser **card de compra** (branco, R$ 437,57,
com botão da Amazon e `rel` correto), mantendo o aviso sobre a cor cinza. Os dois posts
seguem contando a mesma história.

### ⚠️ Nova pendência do cliente

**Shortlink ML do W820NB branco.** O shortlink usado no Top 5 (`meli.la/1pXMdaD`) resolve
para **lista vazia** do perfil de afiliado — mesmo sintoma do LG C5 no post 3139. Por isso
os dois arquivos deste lote trazem **apenas o botão da Amazon** para o W820NB. Regenerar o
link do ML e adicionar o segundo botão.

> Isso também afeta o **guia Top 5 (3336)**, que hoje tem um botão "🛍️ Mercado Livre"
> apontando para esse shortlink quebrado, e ainda exibe "R$ 422,90 (Amazon) / R$ 355,49
> (KaBuM) · 14/08". Recomendo entrar na fila para recaptura.

### Revalidação

```
python3 tools/checar_conformidade.py articles/edifier-w820nb-review-2026-vale-a-pena.html
                                     articles/samsung-galaxy-buds-core-vale-a-pena.html
✅ Aprovado (os dois) — 0 erros, 0 alertas em 2 arquivos.
```
JSON-LD parseia nos dois; zero `aggregateRating`/`offers`/`priceValidUntil`/`availability`;
`rel` correto em 100% dos links; balanço de tags fechado.


---

## 10. 🔒 Decisão final sobre os links do Edifier (17/08/2026)

**Instrução do cliente:** *"Deixar como está — branco só na Amazon, que é onde ele está a
R$ 437,57 e em estoque, com aviso do preço."*

### Como ficou o bloco de compra do 3527

| Card | Amazon | Mercado Livre |
|---|---|---|
| **W820NB branco** (recomendado, R$ 437,57) | ✅ `link.amazon/B06vz0YO0` → ASIN `B09HR1B9RW` | ❌ **sem botão** (decisão do cliente) |
| **W820NB Plus V25** (nova versão, R$ 499) | `amazon.com.br/dp/B0G534R9BZ` (cinza escuro) | ✅ `meli.la/1EapXtQ` → `MLB63185537`, loja oficial Edifier, **marfim**, 9× R$ 55,44 |
| **W800BT Pro** (alternativa, R$ 284–299) | `B0DF5NF475` | `MLB41983700` |
| **Galaxy Buds Core** (alternativa TWS) | `amzn.to/4cDNSkc` | `mercadolivre.com/sec/1pdm5eK` |

### Aviso de preço da cor cinza — agora com link de comprovação

O link `MLB19052273` fornecido pelo cliente **não virou botão de compra** (é a cor esgotada,
a R$ 708,39). Ele foi usado como **prova documental do preço**, em 2 lugares:

1. No aviso acima do bloco de compra, com o valor **R$ 708,39 clicável** — o leitor confere
   sozinho por que não recomendamos essa cor;
2. Na seção **"Fontes consultadas"**, que passou a discriminar as três capturas:
   - Amazon — W820NB **branco** (`B09HR1B9RW`): R$ 437,57, em estoque, 4,7/5 em ~1.483 avaliações;
   - Amazon — W820NB **cinza** (`B09MDC77QX`): "Não disponível, sem previsão";
   - Mercado Livre — W820NB **cinza** (`MLB19052273`): R$ 708,39, "último disponível".

Todos com `rel="sponsored noopener noreferrer nofollow"` e data de consulta.

### Shortlinks descartados (registro para não repetir o teste)

| Shortlink | Resultado em 17/08/2026 |
|---|---|
| `meli.la/1pXMdaD` (usado no guia Top 5) | ⛔ **lista vazia** do perfil de afiliado — mesmo sintoma do LG C5 no post 3139 |
| `meli.la/1d8YAMm` | ⛔ **"Id does not exist"** |
| `MLB19052273` | é a cor **cinza**, R$ 708,39 — não serve para o card do branco |
| `meli.la/1EapXtQ` | ✅ válido, **mas é a Plus V25 marfim** — aplicado no card correto |

> O MLB do W820NB **branco** é o **`MLB19052272`**. Se o cliente gerar o shortlink de
> afiliado para ele, basta adicionar o segundo botão no card do branco.

### Revalidação final do lote

```
python3 tools/checar_conformidade.py articles/edifier-w820nb-review-2026-vale-a-pena.html
                                     articles/samsung-galaxy-buds-core-vale-a-pena.html
✅ Aprovado (os dois) — 0 erros, 0 alertas em 2 arquivos.
Edifier: 11/11 links sponsored · fontes ~12 itens
Buds Core: 8/8 links sponsored · fontes ~21 itens
```

Verificação independente nos dois: JSON-LD parseia (Article + Review + FAQPage +
BreadcrumbList); zero `aggregateRating`/`offers`/`priceValidUntil`/`availability`;
zero `<br/>` no `<script>`; zero base64; zero `data-src`; balanço de tags fechado;
zero alegação de teste físico no corpo.

---

## §11 — Post 3523 · QCY T13 ANC (entregue em 17/08/2026)

**Arquivo:** `articles/qcy-t13-anc-review-2026-vale-a-pena.html`
**Slug:** `qcy-t13-anc-review-2026-vale-a-pena` · **Nota:** 8,5/10 · **5.398 palavras**
**Checker:** 14/14 ✅ — `Total: 0 erro(s)` · 6 links de afiliado, todos com `rel` completo · ~8 fontes.

### Situação encontrada
O post **já havia sido reescrito em 15/08/2026**: as 7 alegações de teste físico da auditoria
original ("testamos", "unboxing", "usamos o fone por") já não estavam no ar, e o artigo já tinha
box de metodologia honesto, bloco "O que isto não é", transparência de afiliados e ressalvas de
não-medição em quase todas as seções. **O CSV `audit/auditoria-48-artigos.csv` está desatualizado
para este item** (como já estava para 3527 e 3545).

### O que restava e foi corrigido nesta rodada

| # | Problema no publicado | Correção |
|---|---|---|
| 1 | H2 e âncora `#unboxing` | → "O que vem na caixa" / `#caixa` |
| 2 | **4 depoimentos entre aspas** com selo "compra verificada" e datas individuais (mai/2026, fev/2024, set/2024, mai/2024) | → bloco "🗣️ Síntese editorial dos relatos", sem aspas, sem selo, sem data individual (regra 4.2) |
| 3 | "avaliações verificadas" / "compradores verificados" (6×) | → "avaliações publicadas por compradores" |
| 4 | JSON-LD com `AggregateOffer`: `lowPrice 169,00`, `highPrice 186,10`, `priceValidUntil "2026-12-31"` (data futura inventada) e 3× `availability: InStock` | **bloco de offers removido inteiro** — padrão do lote |
| 5 | FAQ do schema divergente da visível: tinha "Qual a diferença do T13 ANC para o T13 ANC 2?" (inexistente na página) e faltava "O ANC é eficiente no transporte público?" | as **5 perguntas agora são idênticas** nos dois |
| 6 | Preços de 15/08 (R$ 169–186) | recapturados em 17/08: **Amazon `B0BWRBKMCK` R$ 186,10** · **ML loja oficial QCY R$ 199** (26% OFF de R$ 269,90). Faixa "R$ 186–199" propagada para hero, corpo, 3 tabelas, régua de nota, specs, card de compra e schema |
| 7 | Edifier citado como "38dB, R$ 399" | → R$ 437,57 na cor **branca**, alinhado ao 3527 corrigido |
| 8 | Buds Core citado como "R$ 229–380" | → **R$ 219,31 (Pix, Amazon) / R$ 243,68 (ML)**, alinhado ao 3545 |
| 9 | Bloco "🆕 Novidade" dizia só "construção mais robusta" | → **T13 ANC 2 tem conexão multiponto** (justamente a falta do original), R$ 219,90 na loja oficial ML (de R$ 274, 19% OFF), 4,8/5 em ~1.289 opiniões |
| 10 | Links internos em slugs com 301 (`/edifier-w820nb-review/`, `/jbl-wave-buds-2-review/`) | → slugs canônicos |
| 11 | `rel="sponsored nofollow noopener"` (sem `noreferrer`) | → `rel="sponsored noopener noreferrer nofollow"` em 100% |
| 12 | "Contras" | → **"Pontos de Atenção"** (h4 + `<ul>`, 6 itens) |

### Mantido (já estava correto)
Box de metodologia ("não tivemos o produto em mãos"), a frase condicional do selo "Testado por
nós" (**não é alegação de teste** — correção do cliente de 17/08), a ressalva "o que depende de ter
o produto no ouvido nós não verificamos", bloco de autor canônico, "Fontes consultadas",
"não indica para quem" e a **régua de nota v2.0 aberta** (6 critérios com pesos) — diferencial
do post; só os valores de preço foram atualizados dentro dela.

### Nota recalculada após a alta de preço do ML
O critério Custo-benefício (peso 30%) fora calculado com R$ 169–186; com R$ 186–199 o rival mais
próximo (Buds Core) começa em R$ 219, então o 9,5 se sustenta.
`2,850 + 2,250 + 1,600 + 0,850 + 0,800 + 0,325 = 8,675` → **8,5/10 mantido**.

### Verificação independente (cabeçalho cortado)
JSON-LD parseia; `@graph` = Article + Review + FAQPage + BreadcrumbList; **0** ocorrências de
`aggregateRating`, `offers`, `priceValidUntil`, `availability`, `AggregateOffer`; `author.url` =
`/sobre-a-curadoria-prime/`; **0** `<br` dentro do script; 0 base64; 0 `data-src`; tags balanceadas
(div 47/47, p 86/86, a 41/41, li 51/51, td 133/133); 6 afiliados, 0 sem `rel` completo.
"testamos" e "medimos" aparecem 1× cada — ambos **em negação** ("Não testamos esta unidade",
"Não medimos a autonomia"), portanto válidos.

### Pendências de painel
1. `mercadolivre.com/sec/223qhqp` confirmado em 17/08: resolve para a **loja oficial QCY**, R$ 199.
2. Conferir a data de publicação no schema (`2026-03-16`) contra o painel.

**Status do lote áudio:** 3527 ✅ · 3545 ✅ · **3523 ✅** — trio concluído.

---

## §12 — 3523 revisado com as avaliações REAIS (17/08/2026)

Cliente subiu os dumps direto no GitHub (commit `28ad6ee`), após duas falhas do anexo pelo chat:
`articles/QCY-T13-ANC.amazom.txt` (937 linhas) e `articles/Fone-Qcy-T13-AncML.txt` (1.589 linhas).

### Números reais (substituem os obtidos por busca)
| | antes (busca) | **real (dump)** |
|---|---|---|
| Amazon | 4,6/5 · ~751 | **4,6/5 · 750** · 5★ 81% / 4★ 12% / 3★ 3% / 2★ 1% / 1★ 3% |
| Mercado Livre | 4,8/5 · ~6.546 | **4,8/5 · 6.630** · +10 mil vendidos · R$ 199 (26% OFF de R$ 269,90) |

Amostra lida: **89 avaliações com texto na Amazon + 78 no ML = 167.**

### 🔴 Achado grave: os 4 "Problemas relatados" eram INVENÇÃO ANALÍTICA
Busca por regex nos 167 comentários — **zero ocorrência** para os quatro:

| Problema afirmado no artigo | Ocorrências reais |
|---|---|
| Queda de conexão em ambiente congestionado (shopping/academia) | **0** |
| App não reconhece no 1º pareamento | **0** |
| Latência no modo jogo em iPhone | **0** |
| Ponteira M grande demais para canais menores | **0** |

Eram inferências plausíveis, escritas com aparência de dado ("Frequência: alta", "Frequência:
moderada"). **Seção inteira reescrita** com os padrões que existem de fato.

### O que os dados mostram (nova seção 10, por frequência real)
1. **Falha em um dos lados** — queixa negativa nº 1 na Amazon. Mesmo sintoma repetido: lado
   esquerdo baixa o volume sozinho até parar. De poucos dias a ~1 ano de uso. 1★+2★ = 4% de 750.
2. **Encaixe** — tema mais citado depois de som/ANC/bateria, com **sinal dividido**: "encaixa muito
   bem" vs. "sensação de não ser seguro, mas não cai". Produto vem com **4 tamanhos de ponteiras**.
3. **Um aparelho por vez** — multiponto confirmado ausente por comprador.
4. **Som fraco para minoria** — nas notas 2-3, "praticamente tem que aumentar todo o volume".
5. **Entrega/nota fiscal** — queixa de vendedor terceiro, não do produto (até 2 meses, sem DANFE).

### 🔴 Contradição corrigida: o chiado com vento
O artigo afirmava ser "a queixa que mais se repete nas avaliações negativas de uso ao ar livre".
**Zero relatos.** Os dois que citam vento são **positivos** ("cancela muito bem a vibração do vento").
Alerta mantido como característica da arquitetura feedforward, mas com a ressalva explícita de que
os relatos não o confirmaram.

### Relato âncora do ANC (substitui estimativa)
Comprador com 3 meses de uso: reduz ~**90% do ruído de um ventilador** e ~**80% do som de academia**,
com o alerta "se espera ficar isolado do mundo, talvez não seja a opção adequada". ANC é o tema
**mais citado** nas duas lojas, predominantemente como elogio.

### ⚠️ Viés de amostra registrado no artigo
A captura do ML trouxe **só 4★ e 5★** (78 blocos, distribuição 73×5★ / 5×4★). As críticas vêm
sobretudo da Amazon. Ressalva publicada na seção de Fontes.

### Regra 4.2 preservada
Nenhum depoimento virou bloco com selo/nome/data. Os trechos citados entram como **evidência
qualitativa dentro de síntese**, entre aspas curtas e sem identificação do autor.

**Validação:** checker 14/14, 0 erros · 6.263 palavras · JSON-LD 4 tipos, 0 offers/aggregateRating ·
41/41 tags `<a>` · 0 afiliado sem `rel` completo · 0 "compra verificada".

---

## §13 — Auditoria de 3527 e 3545 contra as avaliações REAIS (17/08/2026)

Dumps recebidos via GitHub (`f2ce32d`): `W820NB-Edifier-amazon.txt` (1.259 l.),
`W820NB-Plus-V25-ML.txt` (326 l.), `Samsung-Galaxy-Buds-Core-amazon.txt` (1.122 l.),
`Samsung-Galaxy-Buds-ML.txt` (5.243 l.). Aplicado o mesmo método que expôs o erro no 3523.

### 🔴 3545 — números publicados estavam ERRADOS
| | publicado | **real** |
|---|---|---|
| Amazon | 4,7/5 · ~164 avaliações | **4,8/5 · 2.883** (88% 5★, 7% 4★, 3% 3★, 2% 1★) |
| ML | 4,9/5 · ~11.283 | **4,9/5 · 7.116** |
| 5★ no veredito | "84%" | **88%** |
Corrigido em 4 pontos (hero, metodologia, seção 7, veredito).

### 🔴 Afirmações sem lastro — REMOVIDAS

**3527 (99 avaliações lidas, 4,7/5 em 1.483 · 82% 5★):**
| Afirmava | Ocorrências |
|---|---|
| "Demora para reconectar no Android — Frequência: moderada" | **0** |
| "Instabilidade do app no iOS — bateria, reinstalação" | **0** |
| "Troca de almofadas por veludo, R$ 40 a R$ 60" | **0** (preço inventado) |

**3545 (314 avaliações lidas — 100 Amazon + 214 ML):**
| Afirmava | Ocorrências |
|---|---|
| "Conexão instável em notebooks Windows — drivers desatualizados" | **0** — a única menção a Windows é **elogio** ("conecta rapidamente no note com Windows e com iPhone 13") |
| "ANC percebido como fraco — Frequência: alta nas 2-3★" | **0** — ANC aparece consistentemente como ponto positivo |

### ✅ O que os dados CONFIRMARAM (seções reescritas por frequência real)

**3527:** (1) **calor na orelha** — "as almofadas esquentam a orelha, e a orelha sua no verão";
alerta para academia: "a espuma vai descascar e reduzir a qualidade do cancelamento". Contraponto
sobre pressão: "vi várias reviews falando que aperta, não aperta não… é EXTREMAMENTE macio".
(2) **microfone é o ponto mais criticado** — "o mic dele é ruim… não é limpo, não é claro";
"precisa falar bem alto para ele liberar o mic"; cliques em carro porque o mic de ANC fica no topo
da concha. **Novo na seção — não estava no artigo.** (3) **chiado com vento forte** — "melhor
desligar a supressão". (4) **app limitado, sem equalizador**, incompatível com PS4.

**3545:** (1) **desconforto após 1-2h e em orelhas menores** — ressalva nº 1, aparece até em 5★:
"a barbatana por mais de 1 hora começou a machucar"; "tenho orelha pequena e ele dói… minha mãe
usa e não sente dor" → a anatomia decide. (2) **estojo inferior ao do Buds FE** — "aparentam ter
fragilidade maior". (3) **Galaxy AI exige Samsung + One UI 6.1**.

### 🔴 Achado que alterou o CARD DE COMPRA do 3527
`W820NB-Plus-V25-ML.txt`: nota 4,9/5 mas com **apenas 21 opiniões**. Entre elas, um comprador que
tinha o W820NB original considerou a **Plus V25 INFERIOR no ANC**, com vazamento de som pela espuma.
O card recomendava a Plus V25 como upgrade natural. **Ressalva publicada no card**: base pequena,
não há confirmação de que supere o original em ANC — a mudança documentada é só o Bluetooth 6.1.
Se o ANC é prioridade e o branco está a R$ 437,57, não há motivo comprovado para pagar mais.

### ⚠️ Viés de amostra (declarado nos artigos)
3545: as capturas trouxeram quase só 4★ e 5★ (Amazon 99×5★+1×4★; ML 207×5★+7×4★) — a seção reflete
ressalvas **dentro de avaliações positivas**, não o conteúdo das notas baixas. Mesmo padrão do ML
no 3523. O dump do Edifier foi o único com críticas reais acessíveis (5×3★, 1×2★).

### Padrão sistêmico identificado
Nos **três** artigos as seções "Problemas relatados" tinham sido escritas por inferência plausível,
com rótulos de falsa precisão ("Frequência: alta/moderada"). O texto era verossímil e por isso não
disparava o checker — só o cruzamento com o dump expõe. **Regra nova: seção de problemas só se
apoiada em dump de avaliações; sem dump, declarar explicitamente que a lista é dedutiva.**

**Validação:** os 3 arquivos com checker 14/14 · 0 erros · JSON-LD Article+Review+FAQPage+
BreadcrumbList · 0 offers/aggregateRating · 0 afiliado sem `rel` completo · tags balanceadas.
3527 = 5.154 palavras · 3545 = 5.106 · 3523 = 6.263.

---

## §14 — Segunda passada nos dumps do Edifier (17/08/2026)

Cliente reapontou os 4 dumps (`f2ce32d`, sem alteração — md5 conferido). Na §13 eu havia extraído
**só as críticas 1-3★**; esta passada minerou os temas restantes, inclusive dentro de avaliações 5★.
Rendeu 4 achados que não estavam no artigo.

### Novos blocos publicados no 3527
1. **Botões que afundam com o tempo** — dono de ~2 anos: *"os botões, com o tempo, afundam, mesmo
   utilizando normalmente; parece que é um defeito crônico"*. Defeito de longo prazo, invisível em
   avaliação de primeira semana.
2. **Espuma das almofadas descasca** — *"os forros começaram a descascar com 8 meses de uso diário"*
   + alerta de quem transpira: *"a espuma vai descascar e reduzir a qualidade do cancelamento"*.
   Almofadas são substituíveis (sem preço citado — não inventar).
3. **A cor "branca" é off-white com espuma bege — 10 menções.** *"Comprei na cor branca e para minha
   surpresa chegou um bege"*, *"um branco velho (off-white) com as espumas mais escuras"*. **Crítico
   para este artigo**: o card de compra vende exatamente essa cor. Aviso replicado no card.
4. **Sem entrada P2 e não dobra** — comparação com o W800BT Plus. Se a bateria acaba, não há cabo.

### Bateria: ancorada em relatos (a tabela era só ficha oficial)
6h/dia → carrega 1×/semana · 2h/dia → *"dura quase um mês"* · *"não sei se dura 49 horas, mas deve
estar bem perto"*. Incluída também a leitura crítica: *"autonomia igual à dos concorrentes"*.

### Buds Core — reminerado, nada novo a corrigir
69 menções a bateria, 22 a microfone, 296 a ANC, 21 a outras marcas. Tudo convergente com o texto
atual. O relato do **Redmi 12 com volume baixo** já constava corretamente na seção 3. Confirmações:
6-8h de reprodução por relato, microfone bom em ambiente controlado, iPhone funciona sem app.

**Validação:** 3 arquivos, checker 14/14, 0 erros · JSON-LD válido, 0 offers/aggregateRating ·
0 afiliado sem `rel` · tags balanceadas · 3527 = 5.570 palavras (era 5.154), 3545 = 5.106, 3523 = 6.263.

---

## §15 — Conferência dos 3 posts NO AR (17/08/2026)

Cliente pediu verificação das URLs publicadas. Resultado: **os três estão no ar com as correções
desta sessão aplicadas.**

### ✅ Confirmado no ar
- **3523 QCY**: hero "R$ 186–199", metodologia citando "167 avaliações lidas uma a uma",
  bloco de compradores com 6.630 (ML) e 750 · 81% 5★ (Amazon), síntese editorial sem selo,
  e a queixa de falha em um dos lados publicada.
- **3527 Edifier**: seção de problemas reescrita (calor, microfone como ponto mais criticado,
  chiado com vento, app sem EQ), o bloco "O que os dados NÃO confirmaram", a ressalva das
  21 opiniões da Plus V25 e o card só com Amazon a R$ 437,57.
- **3545 Buds Core**: números corrigidos (4,8/5 em 2.883 · 88% 5★ · ML 7.116), seção de problemas
  com os 3 padrões reais e o bloco do que os dados não confirmaram.

### 🔴 Divergência encontrada e corrigida no 3523
Contradição interna: "O que vem na caixa" listava **3 pares de ponteiras** (ficha oficial) enquanto
a síntese dos relatos falava em **4 tamanhos** (dois compradores mencionam 4 nas duas lojas).
Corrigido para explicitar a divergência entre ficha e relatos, em vez de escolher um número.

### 🔄 Shortlinks que o CLIENTE aplicou no painel (não estavam no repo) — sincronizados
| Onde | Antes (repo) | **Agora (igual ao ar)** |
|---|---|---|
| W800BT Pro Amazon | `amazon.com.br/dp/B0DF5NF475` | **`link.amazon/B06BFey5m`** |
| W800BT Pro ML | `mercadolivre.com.br/p/MLB41983700` | **`meli.la/2gDAGge`** |
| Plus V25 Amazon | `amazon.com.br/dp/B0G534R9BZ` | **`link.amazon/B04teGQck`** |

Fecha a pendência 🔴 "shortlink do W800BT Pro". O preço do W800BT Pro no repo já batia com o ar
(R$ 284,05 Pix ML / R$ 299 Amazon).

### ⚠️ Observação sobre o QCY no ar
`fetch_page` na home do 3523 retornou **HTTP 500** na primeira tentativa e funcionou na segunda —
instabilidade momentânea do servidor, não erro de conteúdo. Vale reconferir se voltar a ocorrer.

### Pendência que continua
🔴 Shortlink ML do **W820NB branco (MLB19052272)**: o card do 3527 e o do guia 3336 seguem com
**um único botão** (Amazon). O cliente informou ter adicionado, mas não chegou ao repositório nem
aparece no ar — pedir o link direto no chat.

**Validação:** 3 arquivos, checker 14/14, 0 erros, JSON-LD válido, 0 offers/aggregateRating,
0 afiliado sem `rel` completo, tags balanceadas.

---

## §16 — DECISÃO FECHADA: W820NB branco só na Amazon (17/08/2026)

Cliente: *"ficou só da Amazon, do Mercado Livre está muito caro."* **Pendência encerrada.**

### 🔴 ERRO MEU, corrigido na sequência
Ao justificar a decisão, busquei o `MLB19052272` (branco) e publiquei que o ML pedia **R$ 499**
pelo branco, com ofertas de terceiros a partir de R$ 389,99. **Cliente corrigiu:** *"o ML tinha o
W820NB cinza ~700, o branco não."* Ele está certo — e o dossiê já registrava isso desde a §4:

| MLB | cor | preço verificado 17/08 |
|---|---|---|
| `MLB19052273` | **cinza** | **R$ 708,39**, "último disponível" — fora de linha |
| `MLB19052272` | branco | página de catálogo, **sem oferta ativa confirmada** |

O que eu fiz de errado: tratei o resultado de `web_search` no catálogo do branco como se fosse uma
**oferta ativa verificada**. Números de página de catálogo do ML (R$ 499 / R$ 389,99 de terceiros)
não são captura confirmada — e contradiziam a verificação própria já registrada nas §4 e §10.
**A fonte interna existente valia mais que a busca nova, e eu não cruzei.**

### Texto corrigido nos dois artigos
O bloco "Por que só a Amazon?" agora diz o que de fato se apurou: no ML a oferta encontrada era a
**cor cinza**, fora de linha, a **R$ 708,39** (~60% acima da faixa histórica de R$ 355–437). Não é
o mesmo produto do card — o card é do **branco**, e para ele a Amazon a R$ 437,57 é a origem
verificada. Nenhum número de "R$ 499 no branco" permanece em qualquer arquivo.

### Situação final dos links do Edifier
| Item | Amazon | Mercado Livre |
|---|---|---|
| W820NB **branco** | `link.amazon/B06vz0YO0` ✅ R$ 437,57 | ❌ sem oferta verificada |
| W820NB cinza | fora de linha (`B09MDC77QX`) | só como prova de preço (R$ 708,39, `MLB19052273`) |
| Plus V25 | `link.amazon/B04teGQck` | `meli.la/1EapXtQ` ✅ |
| W800BT Pro | `link.amazon/B06BFey5m` | `meli.la/2gDAGge` ✅ |

**Todas as pendências de link do cluster áudio estão fechadas.**

### ⚠️ REGRA (vale para toda a fila)
Antes de publicar preço obtido por `web_search`, **cruzar com o que o dossiê já registrou por
captura própria**. Divergência = a captura própria prevalece, ou refazer a verificação. Resultado
de catálogo do ML não é oferta ativa.

---

## §17 — Faixa de preço histórica aplicada aos 3 reviews + virou REGRA (17/08/2026)

Cliente: *"repete para os 3 artigos já no ar, e torna este procedimento regra."*

### Regra gravada na skill
- `skills/curadoria-review/references/regras-editoriais.md` → **§18. Faixa de preço histórica
  (OBRIGATÓRIA em review e guia de compra)**, com 5 subitens: fontes aceitas, como escrever a
  leitura, proibições, justificativa e onde colocar.
- `skills/curadoria-review/assets/checklist-bloqueio.md` → 6 novos itens de verificação.

**Os 4 campos obrigatórios por produto:** piso já visto · faixa típica · preço de hoje com data ·
**leitura** (frase que diz o que o preço de hoje significa).

**Proibições registradas:** nunca publicar o piso como preço de hoje; nunca levar faixa histórica
para `offers`/`priceValidUntil`; nunca citar loja não re-verificada na data; não inventar "média
de mercado" sem captura datada.

### Blocos publicados nos 3 reviews
Cada review recebeu a faixa do **próprio produto + concorrentes diretos citados no texto**, dentro
de "Onde comprar":

**3523 QCY** — T13 ANC R$ 136 / R$ 170–199 / R$ 186–199 · Buds Core · Redmi.
Leitura: no teto da faixa; abaixo de R$ 170 é boa compra; não vale adiar por R$ 20–30.

**3527 Edifier** — branco R$ 351 / R$ 370–437 / **R$ 437,57 (no teto e subindo)** · cinza R$ 708,39
(~60% acima) · W800BT Pro · Buds Core. Caixa laranja: **único do cluster que encareceu**, de
R$ 379,04 (27/05, Amazon, de R$ 449) para R$ 437,57 — causa é fim de linha, não demanda.

**3545 Buds Core** — R$ 184 / R$ 220–270 / R$ 219–268 · QCY · Buds FE.
Leitura: quedas abaixo de R$ 200 vêm de **cupom em data comercial** (R$ 184,14 em 20/07 com VIPMELI;
R$ 198,20 em 09/03 com HRPRIME), não de desconto permanente — esperar campanha economiza até R$ 80.

### Validação dos 4 arquivos
| Arquivo | Faixa | offers | aggRating | rel incompleto | tags | palavras |
|---|---|---|---|---|---|---|
| 3523 QCY | ✅ | 0 | 0 | 0 | OK | 6.523 |
| 3527 Edifier | ✅ | 0 | 0 | 0 | OK | 5.941 |
| 3545 Buds Core | ✅ | 0 | 0 | 0 | OK | 5.354 |
| 3336 guia | ✅ | 0 | 0 | 0 | OK | 5.134 |

Checker 14/14 em todos, 0 erros.

### ⚠️ Todos os 4 precisam ser recolados no WordPress
O que está no ar ainda **não** tem a faixa histórica. Pendências acumuladas por arquivo:
- **3336**: seção 8 nova + tabela (R$ 437,57) + frase da conclusão + faixa.
- **3527**: bloco "Por que só a Amazon" corrigido + 3 shortlinks do painel + faixa.
- **3523**: contradição das ponteiras + faixa.
- **3545**: faixa.

---

## §19 — 3550 (JBL Wave Buds 2): cluster de áudio CONCLUÍDO

Último dos 6 posts do cluster. Detalhes em `audit/estado-3550.md`.

**Placar final do cluster** — todos checker 14/14, 0 erros:

| Post | Produto | Palavras | Nota |
|---|---|---|---|
| 3523 | QCY T13 ANC | 6.523 | 8,5 |
| 3527 | Edifier W820NB | 5.941 | 8,8 |
| 3545 | Galaxy Buds Core | 5.354 | 8,5 |
| 3336 | Guia Top 5 até R$ 500 | 5.134 | — |
| 3548 | Redmi Buds 6 Play | 4.794 | 8,2 |
| **3550** | **JBL Wave Buds 2** | **3.633** | **8,4** |

**Violação mais grave encontrada no 3550:** era o **único post do cluster sem declaração de
não-teste físico**, e ainda usava "unboxing" descrevendo impressões de uso. Reforça a regra:
a ausência da declaração é mais perigosa quando o texto tem vocabulário de mão-na-massa,
porque o leitor conclui teste próprio sem que o artigo precise afirmá-lo.

**§19.1 — Dispersão de preço como conteúdo editorial.** O Wave Buds 2 aparecia em 17/08 a
R$ 222 na Amazon e R$ 426,87 no Magalu — quase o dobro, mesmo produto, mesma data. Quando a
dispersão entre varejistas passa de ~50%, ela vira **informação útil ao leitor** e deve ganhar
caixa de alerta com o teto a evitar, não só o link da loja mais barata.

**§19.2 — Relato de manutenção vale mais que relato de defeito.** O achado mais valioso do dump
não foi uma queixa, foi uma **solução**: limpar a saída de som com cotonete recuperou um fone
dado como morto (16 votos de útil). Ao minerar dumps, procurar ativamente relatos de
**"resolvi assim"** — eles têm utilidade prática maior que a enésima confirmação de que o som é bom.

**§19.3 — Tema com amostra pequena: publicar com o número à vista.** Chamadas apareceram em
apenas 3 das 100 avaliações. Em vez de omitir a seção ou generalizar, o artigo abre declarando
"3 das 100 avaliações lidas, o que é pouco para afirmar um padrão" e complementa com o dado
de hardware (2 microfones × 6 do concorrente). Amostra pequena não impede publicar — impede
afirmar frequência.
