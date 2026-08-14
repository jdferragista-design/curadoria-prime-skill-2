# Análise técnica e estética — layout Apple TV 4K

Fonte: [`../assets/modelos/modelo-layout-apple-tv-4k.html`](../assets/modelos/modelo-layout-apple-tv-4k.html) (blocos `<!-- wp:html -->` + estilo inline).  
Escopo: só composição, hierarquia e identidade gráfica. Sem conteúdo editorial.

**Regra de cor (oficial da casa):** o hero veste a **marca do produto** (no modelo 1, preto + `#2997ff` da Apple). Os CTAs vestem a **plataforma** (Amazon laranja, ML navy + amarelo, Apple Store preta). Paleta completa: [cores.md](cores.md).

## Identidade gráfica

O modelo não é “card de e-commerce genérico”. É um sistema **Apple-escuro + semáforo editorial + cores de loja**.

| Token | Valor | Função |
| --- | --- | --- |
| Preto Apple | `#1d1d1f` → `#000000` | Hero, cabeçalho de tabela, card “compra segura”, CTA oficial |
| Azul produto | `#2997ff` | Único highlight no hero (nome do produto e preços) |
| Âmbar jurídico | fundo `#fffbeb`, borda `#fde68a`, texto `#78350f` | Tipo de análise, metodologia, transparência |
| Semáforo | verde `#22c55e` / azul `#3b82f6` / âmbar `#f59e0b` | Vale / depende / espera |
| Amazon | `#FF9900` e gradiente `#ff9900` → `#ff8500` | Filete e CTA |
| Mercado Livre | navy `#2d3277` → `#1a1f5c` + amarelo `#ffe600` | CTA (não o amarelo chapado da logo) |
| Neutros | `#f8fafc`, `#e2e8f0`, `#64748b`, `#1e293b` | Índice, FAQ, relatos |
| Alerta | `#fef2f2` / `#fecaca` / `#7f1d1d` | Box de risco |

**Raio:** 10px (boxes jurídicos), 12px (índice, relatos, scores), 14px (hero e cards de compra), 20px (wrapper de “onde comprar” e bloco final de escolha). Pills do hero: `border-radius: 100px`.

**Tipo:** hierarquia por peso e tamanho, não por família. Kicker 11px / bold / `letter-spacing: .1em` / uppercase. Lead 18px / 600. Chips 13px. Preço no título do card 17px bold + 14px cinza `#888`. Score 26px / 800. CTA 15px / 800. Corpo dos cards 14px / `#666`.

**Sombra:** hero `0 4px 16px rgba(0,0,0,.14)`; wrapper de compra `0 4px 20px rgba(0,0,0,0.05)`; CTA `0 2px 8px` na cor da marca.

Não há CSS de componente (`.cp-atv`). Tudo é **inline no bloco Gutenberg**. Recriar com um stylesheet próprio quebra a identidade e o comportamento no tema do WP.

---

## 1. Faixa de dados (hero)

Não é uma fileira de chips sobre fundo claro. É um **bloco único escuro**, o único momento “produto premium” da página.

```
[ kicker pill: Review Completo — 2026 ]
[ lead 18px, 2–4 linhas; só produto e preço em #2997ff ]
[ 4 pills em flex-wrap, gap 10px ]
```

Composição:

- Fundo `linear-gradient(135deg,#1d1d1f 0%,#000000 100%)`, padding `28px 30px`, raio 14px.
- Kicker: vidro (`rgba(255,255,255,.16)` + borda `.28`), pill 100px, uppercase, tracking largo. É rótulo de *gênero*, não dado.
- Lead ocupa a largura toda. O azul `#2997ff` aparece **só** em âncoras de decisão (nome + preços). O resto do texto é branco. Isso cria um único eixo de leitura.
- Chips: mesmo vidro do kicker, `6px 14px`, sem ícone isolado — emoji + dado na mesma linha. Quatro unidades: duas provas sociais, uma faixa de preço, uma data.
- Os chips **não competem** com o lead: são metadados, 13px, peso normal.

O que a faixa *não* é: barra preta de disclaimer, chips pretos sobre branco, ou quatro pílulas sem o bloco-gradiente. O disclaimer jurídico fica **acima**, no box âmbar — separado do hero. Misturar os dois (preto + texto legal) destrói o contraste de função: um é compliance, o outro é vitrine.

Hero fotográfico vem **depois**, full-bleed até 1000px, raio 12px, sombra, legenda 12px `#7c7c9a` centralizada. A foto não entra no gradiente.

---

## 2. Cards de veredito (resposta rápida)

Três colunas `repeat(auto-fit, minmax(280px, 1fr))`, gap 16px. Não são cards de score (esses só no fim). São **painéis semânticos de decisão**.

| Card | Fundo | Borda 2px | Título |
| --- | --- | --- | --- |
| Vale | `#f0fdf4` | `#22c55e` | `#166534` |
| Depende | `#eff6ff` | `#3b82f6` | `#1e40af` |
| Espera | `#fffbeb` | `#f59e0b` | `#92400e` |

Diagramação interna:

1. Título numa linha: emoji + rótulo da decisão (15px / 700). Sem preço gigante.
2. Corpo 14px / 1.6, mesma cor do texto-base do card. O preço, quando existe, está **dentro do parágrafo**, em bold — não é um display de 22px.
3. Sem foto, sem botão, sem “R$” como herói. O card responde *para quem*, não *quanto*.

A hierarquia é **decisão → condição → detalhe**. Preço aqui seria ruído: o sistema reserva o número grande para o card de compra.

No fechamento do artigo o semáforo volta em **grade de scores** (`minmax(170px, 1fr)`), centralizado: rótulo 12.5px uppercase implícito, número 26px/800, legenda 12px. Verde para eixos fortes, azul para um eixo médio, âmbar para o ponto fraco, roxo só na nota geral. É um segundo uso do semáforo, não uma repetição dos três cards de cima.

---

## 3. Cards de compra (foto + hierarquia)

Não são três colunas iguais. São **três cartões empilhados**, full-width, dentro de um wrapper branco (`padding 35px 25px`, raio 20px, sombra suave). A leitura é vertical: uma oferta por vez, como prateleira.

Ordem visual de cada cartão:

```
[ pill de função + nome da loja + preço em cinza ]
[ foto full-width, raio 10px ]
[ parágrafo 14px #666 — o argumento ]
[ box de alerta, se houver ]
[ CTA(s) em flex, min-width 150px ]
```

Hierarquia de ênfase pelos **contornos**, não pelo tamanho:

1. **Menor preço** — borda 2px `#16a34a`. Pill em gradiente verde `#16a34a` → `#166534`. Foto presente.
2. **Compra segura** — borda 2px `#1d1d1f` (Apple). Pill preto. Foto presente. Mesmo peso visual do verde; o preto diz “oficial”, o verde diz “barato”.
3. **Também nacional / acessório** — borda 2px `#e9ecef` (neutra). Pill cinza `#f1f5f9` / `#475569`. No review de um SKU (Apple TV) o terciário pode ficar sem foto. Em guia com vários produtos, **cada card leva a foto do SKU** — senão o leitor lê “oferta menor”, não “outro tablet”.

A foto fica **depois do título e antes do texto**, centralizada — o olho cai no produto depois de saber *qual oferta* é. Três colunas com foto quadrada invertem isso e deixam os três preços gritando ao mesmo tempo.

Tamanho: no Apple TV a foto pode ir `width 100%` porque o objeto é pequeno em fundo branco. Em tablet, notebook ou TV a mesma regra estoura o card. Nesses SKUs use `max-width: 260px; max-height: 170px; width: auto; height: auto; object-fit: contain`. A foto identifica o produto; o CTA carrega o preço.

O título do card é uma linha só: loja em 17px bold `#1a1f36` + preço/estrelas em 14px `#888`. O preço grande mora no **botão**, não no título.

Alerta de importado (quando existe) é um box laranja claro *dentro* do card verde, antes do CTA — a ressalva interrompe o fluxo de compra de propósito.

---

## 4. CTAs

Cada loja tem um botão-assinatura. Não se usa laranja Amazon no ML, nem amarelo chapado no ML.

| Destino | Fundo | Texto | Sombra |
| --- | --- | --- | --- |
| Mercado Livre | `#2d3277` → `#1a1f5c` | `#ffe600` | navy 0.3 |
| Apple Store | `#1d1d1f` → `#000` | branco | preto 0.3 |
| Amazon | `#ff9900` → `#ff8500` | branco | laranja 0.3 |
| Fecho “menor preço” (bloco escuro final) | `#16a34a` → `#166534` | branco | verde 0.4 |
| Fecho Apple (bloco escuro final) | branco → `#e5e5ea` | `#1d1d1f` | branco 0.25 |

Regras de forma:

- `padding: 12px 20px` (fecho: `13px 22px`)
- raio 8px (mais duro que o card — o botão é ferramenta, o card é superfície)
- `font-weight: 800`, 15px
- `flex: 1; min-width: 150px; text-align: center` — se há dois CTAs, eles **dividem a linha** com gap 10px
- rótulo = verbo + loja + preço (`Ver no Mercado Livre — R$ 1.465,85 no Pix`)
- `rel="sponsored noopener noreferrer"` nos afiliados; Apple sem `sponsored`

O bloco final de “escolha rápida” inverte o fundo (mesmo gradiente do hero) e põe os CTAs no centro. É a única vez em que o botão verde “barato” e o botão branco “Apple” aparecem lado a lado sobre preto — reprise do hero, agora acionável.

---

## O que o HTML anterior errou (só o visual)

- Inventou um design system (`.cp-atv`, Inter, chips pretos no branco) em vez do inline Gutenberg.
- Transformou a faixa de dados numa barra de metadados; tirou o gradiente `#1d1d1f` e o azul `#2997ff`.
- Colocou preço display nos cards de veredito — no modelo o preço grande é do CTA.
- Montou compra em **3 colunas iguais**, todas com foto. O modelo empilha e **tira a foto** da oferta terciária.
- CTAs Amazon laranja / ML amarelo chapado / oficial preto sólido. O ML verdadeiro é **navy + amarelo no texto**.
- Scores no veredito viraram três cards de perfil. O modelo fecha com **grade de notas** + bloco escuro de escolha.

Replicar o layout é copiar esses tokens e essa ordem, em blocos `wp:html`, não reinterpretar o moodboard.

---

# Análise técnica e estética — modelo 2 (Power Bank no Avião)

Fonte: [`../assets/modelos/modelo-power-bank-aviao.html`](../assets/modelos/modelo-power-bank-aviao.html) (mesmos blocos `<!-- wp:html -->` + inline).  
Mesmo chassi da Apple TV 4K. Pele e módulos de decisão diferentes: aqui o assunto é **regra + risco**, não produto premium.

## Identidade gráfica

O hero deixa de ser Apple-escuro e vira **alerta de viagem** em ciano.

| Token | Valor | Função |
| --- | --- | --- |
| Ciano guia | `#0e7490` → `#164e63` | Hero, pills de destaque, cabeçalho de tabela, borda dos cards âncora, links da metodologia |
| Highlight frio | `#67e8f9` | No lead: norma, limites, “5 modelos” |
| Highlight quente | `#fbbf24` | No lead: confisco e multa — a única cor quente no hero |
| Âmbar jurídico | `#fffbeb` / `#fde68a` / `#78350f` | Igual ao modelo 1 (metodologia, afiliado, atualização) |
| Semáforo regulatório | verde / âmbar / **vermelho** | Livre / autorização / proibido — o azul some desta tríade |
| Amazon / ML | iguais ao modelo 1 | CTAs |
| Neutros | iguais (`#f8fafc`, `#e2e8f0`, `#64748b`) | Índice, FAQ, escolha rápida |

Raio, tipo e padding do hero são **os mesmos** (14px, kicker 11px uppercase, lead 18px/600, chips 13px, gap 10px). O que muda é o **matiz e o que os chips dizem**.

Sombra da foto: `0 4px 16px rgba(14,116,144,.12)` — a sombra também é ciano, não preta. O produto (Apple TV) projeta peso; o guia de regra projeta atmosfera.

Não há box âmbar *antes* do hero. A ordem é: faixa ciano → foto → metodologia → transparência. O modelo 1 põe o tipo de análise **acima** do preto. Aqui o kicker “Alerta de Viagem” já carrega o gênero; o jurídico desce.

---

## 1. Faixa de dados

Mesma ossatura:

```
[ kicker pill: Alerta de Viagem — Guia 2026 ]
[ lead 18px; âncoras em #67e8f9; penas em #fbbf24 ]
[ 4 pills ]
```

Os quatro chips **não são prova social**. São o mapa da regra:

- `✅ Até 100Wh = livre`
- `⚠️ 100-160Wh = autorização`
- `❌ +160Wh = proibido`
- `🕒 Atualizado: …`

Isso antecipa o veredito. No modelo 1 os chips são metadado (estrelas, faixa de preço). Aqui eles *são* a decisão. Por isso o terceiro chip é vermelho semântico no texto, mesmo dentro do vidro branco.

O lead é mais longo e mais denso que o da Apple TV. Visualmente ainda é um único parágrafo 18px/600 — a hierarquia continua no **dois highlights**, não em subtítulos dentro do hero.

---

## 2. Cards de veredito (resposta rápida)

Não são os painéis “vale / depende / espera” com parágrafo. São **azulejos de limite**, centrados, `minmax(180px, 1fr)`:

```
[ emoji 28px ]
[ número 22px / 800 ]     ← ≤100Wh / 100-160Wh / >160Wh
[ conversão 12px ]        ← ~27.000mAh
[ status 13px ]
```

| Card | Fundo | Borda 2px | Número |
| --- | --- | --- | --- |
| Livre | `#f0fdf4` | `#22c55e` | `#166534` |
| Autorização | `#fffbeb` | `#f59e0b` | `#92400e` |
| Proibido | `#fef2f2` | `#ef4444` | `#991b1b` |

O azul `#3b82f6` **sai** desta grade. No guia de risco, o terceiro estado é veto, não “depende do perfil”. `text-align: center` + número grande: aqui o display *é* o critério (Wh), não o preço.

Há um segundo “veredito” no fim, de outra espécie: painel `#dbeafe` com borda `#0e7490` e **quatro mini-tiles brancos** (74Wh, 88,8Wh, 2, 100Wh) — números 20px ciano, legenda 12px. Não é grade de notas 9.6/10. É um *dashboard* da regra. Abaixo, “Escolha Rápida” em 2×2 cards brancos sobre `#f8fafc`, sem CTA.

---

## 3. Cards de compra (hierarquia sem foto)

Cinco cartões **empilhados**, full-width, cada um depois do respectivo H2. Sem o wrapper branco de 35px do modelo 1. Sem foto de produto.

Ordem interna:

```
[ pill de função (só nos âncoras) + nome 17px + preço/Wh em #888 14px ]
[ linha 14px #666 — marca, watts, notas de loja, Wh ]
[ dois CTAs flex ]
```

Ênfase pela **borda ciano**, não pela foto:

1. **Basike** e **Anker 737** — borda 2px `#0e7490`, pill em gradiente ciano. São os dois polos (barato / teto permitido).
2. **i2GO, Nano, Zolo** — borda 2px `#e2e8f0`. Pills pequenas só quando há eixo extra (verde “ultracompacto”, azul “para notebooks”). Sem pill = oferta do meio da lista.

Tirar a foto é coerente com o gênero: o leitor não está escolhendo um unboxing; está checando se o Wh cabe. A hierarquia visual do cartão cai no **par preço | Wh ✅** da linha de título. O check verde no Wh é o selo de passagem — equivalente funcional da foto no modelo 1.

O H2 acima de cada card (`💸 1. Basike…`) faz o trabalho que a foto faria: identidade + rank. Duplicar isso com imagem full-width seria ruído.

---

## 4. CTAs

Idênticos ao modelo 1 nos dois marketplaces. Sem botão preto Apple. Sem reprise escura no fecho.

| Destino | Fundo | Texto |
| --- | --- | --- |
| Amazon | `#ff9900` → `#ff8500` | branco |
| Mercado Livre | `#2d3277` → `#1a1f5c` | `#ffe600` |

Sempre **dois botões** na mesma linha (`flex: 1`, `min-width: 150px`, raio 8px, 15px/800, `12px 20px`). Rótulo = loja + preço. `rel="sponsored noopener noreferrer"`.

O fecho comercial é a grade “Escolha Rápida” — texto, sem botão. A compra ficou nos cinco cards; o veredito não compete com eles.

---

## Módulos que o modelo 2 acrescenta (e o 1 não tem)

- **Pode / não pode** — mesma casca verde/vermelha dos prós/contras da Apple TV, mas lista sem bullet e com divisores internos (`#bbf7d0` / `#fecaca`).
- **Incidentes** — cards de gravidade: vermelho (caso grave), âmbar (alerta), verde (dado). Título 15px/700 na cor do eixo.
- **Processo em 5 etapas** (thermal runaway) — tiles claros com rampa de cor no número (ciano → âmbar → laranja → vermelho → tile vermelho final). O último quebra o padrão de borda 1px e ganha 2px vermelha: clímax visual.
- **Tabelas** — thead `#0e7490` (não `#1d1d1f`). Linhas pintadas pelo semáforo (verde livre, azul destaque 20k/27k, âmbar, vermelho). A cor da linha *é* o status.
- **Dicas** — único bloco azul `#eff6ff` / borda `#3b82f6`: procedimento, não risco.
- **FAQ** — H3 + parágrafo, sem os cards `#f8fafc` empilhados do modelo 1.
- **Separadores** `<hr class="wp-block-separator">` entre seções. O modelo 1 encadeia blocos sem linha.
- **Rodapé afiliado** — `border-top: 3px solid #0e7490`, não reprise do hero.

Relatos: filete 4px **ciano** (viajante) ou **vermelho** (reclamação). No modelo 1 o filete era laranja Amazon / azul ML — loja. Aqui o filete é **fonte do relato**, não o marketplace.

---

## Os dois modelos, lado a lado

| Peça | Modelo 1 — Apple TV 4K | Modelo 2 — Power bank |
| --- | --- | --- |
| Pele do hero | Preto `#1d1d1f` + `#2997ff` | Ciano `#0e7490` + `#67e8f9` / `#fbbf24` |
| Chips do hero | Prova social + preço + data | Mapa da regra (livre / autorização / veto) + data |
| Tipo de análise | Âmbar **acima** do hero | Some; kicker assume o gênero |
| Veredito rápido | 3 painéis com parágrafo (vale/depende/espera) | 3 azulejos centrados (Wh) |
| Compra | 3 cards, 2 com foto, wrapper branco | 5 cards, **sem foto**, H2 + card |
| Destaque de oferta | Borda verde vs preta Apple | Borda ciano nos dois polos |
| Fecho | Scores + bloco preto com CTAs | Dashboard Wh + escolha rápida sem botão |
| Tabela | Cabeça preta | Cabeça ciano; linha = status |
| CTA loja | Amazon / ML / Apple | Amazon / ML |

Regra de família: **mesmo esqueleto Gutenberg e mesmos botões de loja**. A pele do hero e o tipo de veredito mudam com o gênero da página (review de um SKU vs. guia de regra + lista). Não misturar: um guia de tablets “vale a pena” puxa o modelo 1; um guia “o que a ANAC deixa” puxa o modelo 2.
