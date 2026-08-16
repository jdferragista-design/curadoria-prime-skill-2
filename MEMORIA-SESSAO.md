# 🧠 MEMÓRIA DA SESSÃO — Limpeza de Conformidade Curadoria Prime

> Registro do que foi feito nesta sessão (branch `arena/01a0028f-curadoria-prime-skill-2`).
> Atualizado em: **14/08/2026**. Serve para retomar o trabalho sem perder contexto.

---

## 1. Contexto e objetivo

- **Cliente:** Cristiano Martins — fundador/editor-chefe da Curadoria Prime (`curadoriaprime.com`).
- **Projeto:** limpeza de conformidade de 48 artigos publicados, por 3 classes de problema:
  1. alegações de teste físico que não ocorreram ("testamos por 30 dias");
  2. urgência falsa ("estoque limitado", "verificado há 2 horas");
  3. JSON-LD com `aggregateRating` inventado e autor errado.
- **Método (regra do cliente):** UM POST POR VEZ; nunca reescrever do zero; editar preservando layout/classes do tema; nunca inventar bloco de autor (usar o canônico); deslazyficar imagens; nunca editar JSON-LD por regex; validar antes de entregar (parse JSON-LD, balanço de `<div>`, contagens, `rel="sponsored"` em 100%, zero base64).

---

## 2. Regras/descobertas importantes (para não repetir erros)

1. **Referenciar posts por slug/título, não por ID** — pedido explícito do cliente.
2. **`curl` NÃO funciona neste sandbox** (TLS derrubado na borda). Use a **WP REST API aberta**:
   - `https://curadoriaprime.com/wp-json/wp/v2/posts/<ID>?_fields=content,title,link,date,modified`
   - A página renderizada (`https://curadoriaprime.com/<slug>/`) preserva os **hrefs** dos botões de afiliado; o `content.rendered` da API às vezes entrega as âncoras SEM href.
   - A página renderizada às vezes retorna **HTTP 500** no primeiro fetch (intermitente) — repetir resolve.
3. **Shortlinks `meli.la` NÃO são links quebrados**: resolvem pelo perfil social do afiliado (`social/6620250626180940`) — é o tracking do cliente no ML.
4. **JSON-LD:** colar em bloco `<!-- wp:html -->` SEM `<br />` (o `<br/>` dentro de `<script>` quebra o parse e o Google descarta o schema). Em bloco de parágrafo, o WP injeta `<br/>`.
5. **Categoria `tvs` não existe** — a real é `tv-e-home-theater`. Fones → `audio-e-som`. Wearables → `smartphones-e-wearables`. Guia geral → `destaques`.
6. **Paleta por artigo** (preservar na reescrita): 3181 = roxo claro `#5a4fcf`; 3809 (Fit3) = roxo `#5a4fcf→#764ba2`; 3336 = roxo `#5a4fcf`; 4397 = azul `#0b3d91→#1e88e5`.
7. **Checker do repo** (`tools/checar_conformidade.py`) tem falsos positivos conhecidos:
   - `[divulgacao] depois do primeiro link` — triggava com shortlink literal dentro de comentário HTML; manter comentários sem URLs de afiliado.
   - `[fontes]` — exige o termo exato **"Fontes consultadas"** (não "Fontes e referências").
   - `[valor-agregado]` — exige sinais "prós e contras" + "para quem NÃO é" no texto.
   - `[keyword-stuffing] 'samsung'` — densidade de nome de marca, aceitável.
8. **Bloco de autor canônico** (usar SEM variação):
   `cristiano-curadoria-prime.jpg` + bio "Motorista de aplicativo em Uberlândia (MG), 16 mil viagens…" + link X `https://x.com/CuradoriaPrime`.
9. **Schema padrão** dos artigos corrigidos: `@graph` = Article/TechArticle + (Product|ItemList) + FAQPage + BreadcrumbList; autor `Cristiano Martins` (@type Person); SEM `aggregateRating`/`reviewCount`; SEM `priceValidUntil`/`availability`; `reviewRating` com `worstRating` quando houver nota.
10. **Faixas de preço > valores fixos** quando não há captura do dia — decisão do cliente para o 4397.

---

## 3. Artigos trabalhados (status)

| # | Slug | Título/Produto | Arquivo entregue | Status |
|---|---|---|---|---|
| 1 | `lg-au801-50-review` | LG AU801 50″ | `articles/3181-lg-au801-50-artigo-completo.html` | ✅ FECHADO |
| 2 | `samsung-galaxy-fit3-vale-a-pena` | Galaxy Fit3 | `articles/samsung-galaxy-fit3-vale-a-pena-artigo-completo.html` | ✅ validado |
| 3 | `melhor-fone-bluetooth-ate-500-reais-2026` | Top 5 Fones até R$ 500 | `articles/melhor-fone-bluetooth-ate-500-reais-2026-artigo-completo.html` | ✅ validado |
| 4 | `presentes-dia-dos-pais-tech-ate-300` | 7 Presentes Tech até R$ 300 | `articles/presentes-tech-ate-300-artigo-completo.html` | ✅ reposicionado + validado |

**Dossiês em `audit/`:** `estado-3181.md`, `estado-3809.md`, `estado-3336.md`, `estado-4397.md` + análises de layout `analise-3336-layout.md`, `analise-4397-layout.md`.

### 3181 (LG AU801) — detalhes
- JSON-LD em `wp:html` sem `<br/>`; categoria `tv-e-home-theater`; sem aggregateRating; autor canônico.
- Ressalvas resolvidas: (a) imagem webOS errada removida da seção Gaming; (b) link `/transparencia-curadoria-prime/` reintroduzido.
- Contras: "Pontos de Atenção" + `<ul>` 5 itens. Shortlink Amazon unificado em `B03wia3Ue`.
- **Pendências:** Rank Math título SEO (aspa reta → "50 polegadas"); nome de exibição WP "Cristiano Martins"; confirmar `sku 50AU801` e logo `cropped-image-270x270.jpg`.

### 3809 (Galaxy Fit3) — detalhes
- Urgência removida; 4 JSON-LD consolidados em 1 `@graph`; "bateria real" → "relatada por compradores".
- Contras: "Pontos de Atenção" + `<ul>` 6 itens. Autor "Cristian" → canônico.
- 3 links internos quebrados corrigidos (A15→A16, S24, S25).
- **Pendências:** confirmar shortlink Amazon `B0dY6J5t4` (o original tinha `B05Uwnj8q` na prova social); recapturar preço (julho/2026 >30 dias) e reinserir `offers`.

### 3336 (Top 5 Fones até R$ 500) — detalhes
- **10 shortlinks de afiliado extraídos do artigo ao vivo** (mapa abaixo). Urgência do Dia dos Pais removida; preços re-verificados 14/08.
- Edifier W820NB MANTIDO (não trocado): link Amazon BRANCO novo `B06vz0YO0` + KaBuM como alternativa.
- JSON-LD: Article + ItemList (sem aggregateRating/ofertas) + FAQ + Breadcrumb.
- 5 blocos "Pontos de Atenção". ✅ Aprovado no checker.

### 4397 (7 Presentes Tech até R$ 300) — detalhes
- **Reposicionado de sazonal → permanente** (Dia dos Pais 2026 encerrado em 09/08). URL/slug preservados.
- Autor adicionado; 7 blocos "Pontos de Atenção"; preços em FAIXA (pesquisados 14/08).
- Bug da Smart Band 10 corrigido (2× ML igual → Amazon `B03Lb5iTz` + ML `2t1nuos`).
- Imagem destaque (1200×600, com texto) + hero (16:9, sem texto) geradas por IA com produtos reais.
- **Pendências:** título no painel (ainda "Dia dos Pais 2026: 7 Presentes Tech até R$ 300") — cliente não definiu o novo título ainda; slug ainda contém "dia-dos-pais" (avaliar 301 futuro).

---

## 4. Links de afiliado (referência valiosa — extraídos ao vivo)

### 3336 (Top 5 Fones)
| Produto | Amazon | Mercado Livre |
|---|---|---|
| Galaxy Buds Core | `amzn.to/4x9UVbh` | `meli.la/1etJ5dy` |
| QCY T13 ANC | `amzn.to/4pTnAPy` | `meli.la/1UjXuhQ` |
| Redmi Buds 6 Play | `amzn.to/4pTYqjQ` | `meli.la/1J2VMuY` |
| JBL Wave Buds 2 | `amzn.to/455lC55` | `meli.la/1qK8Kvf` |
| Edifier W820NB | `link.amazon/B06vz0YO0` (branco) | `meli.la/1pXMdaD` |

### 4397 (7 Presentes Tech)
| Produto | Amazon | Mercado Livre |
|---|---|---|
| Smart Band 10 | `link.amazon/B03Lb5iTz` (fornecido) | `meli.la/2t1nuos` (fornecido) |
| Galaxy Fit3 | `link.amazon/B05Uwnj8q` | `meli.la/2s1mWYW` |
| QCY T13 ANC | `link.amazon/B0b7hBdj6` | `mercadolivre.com/sec/223qhqp` |
| JBL Wave Buds 2 | `link.amazon/B0fl4XLa3` | `mercadolivre.com/sec/1Ezyrug` |
| Redmi Buds 6 Play | `link.amazon/B06aJfuhA` | `mercadolivre.com/sec/1U1WzWs` |
| Edifier W820NB | `link.amazon/B0buAeyna` | `meli.la/2gDAGge` |
| Power Bank 20000mAh 18W | `link.amazon/B08vvzZ98` | `meli.la/1xXDJ4x` |

> ⚠️ **Inconsistência de tracking detectada:** o MESMO produto usa shortlinks DIFERENTES entre artigos
> (ex.: QCY Amazon = `4pTnAPy` no 3336 vs `B0b7hBdj6` no 4397; Fit3 = `B0dY6J5t4` no 3809 vs `B05Uwnj8q` no 4397).
> Cliente precisa decidir se unifica.

---

## 5. Preços verificados em 14/08/2026 (para reuso)

| Produto | Preço hoje | Obs |
|---|---|---|
| Galaxy Buds Core | R$ 269,90 | Amazon |
| QCY T13 ANC | R$ 199 | ML Pix (26% off) |
| Redmi Buds 6 Play | R$ 78,05 (azul) / R$ 93,10 (preto) | ML |
| JBL Wave Buds 2 | R$ 255 | Amazon |
| Edifier W820NB | R$ 355,49 (KaBuM) / R$ 422,90 (Amazon branco) / Plus R$ 483 (ML) | subiu; saiu de ≤300 |
| Xiaomi Smart Band 10 | R$ 289–400 | faixa (ES ~289, Global ~387–397) |
| Galaxy Fit3 | R$ 219–300 (oferta) / cheio R$ 599 | Amazon |
| Power Bank 20000mAh 18W | R$ 130–230 (marketplace) / R$ 368–400 (oficial) | ampla |

---

## 6. Imagens geradas (`imagens/4397/`)

| Arquivo | Formato | Conteúdo |
|---|---|---|
| `presentes-tech-ate-300-destaque.jpg` | 1200×600 (2:1) | COM texto "Presentes Tech até R$ 300" / "Smartband · Fones · Power Bank" |
| `presentes-tech-ate-300-hero.jpg` | 16:9 | SEM texto, produtos reais |

- Estilo: gradiente preto→vinho + fitas douradas (réplica da imagem antiga), produtos reais como referência.
- Caminho no artigo: `wp-content/uploads/2026/08/presentes-tech-ate-300-hero.jpg` (já referenciado no HTML/JSON-LD).
- ⚠️ Modelo da smartband nas referências era Band 9 (a 10 não apareceu na busca); validar com o cliente.

---

## 7. Fila restante (do briefing do cliente)

- **Urgência falsa:** ~~3336~~ ✓ · ~~4397~~ ✓ · **4541** (próximo, `presentes-dia-dos-pais-2026-tech-premium` — guia do MESMO evento, avaliar canibalização com o 4397).
- **Lote de schema (29):** 4414, 4474, 4456, 4254, 4251, 4185, 4159, 4155, 3871, 3858, 3924, 3835, 3548, 3550, 3523, 3320, 3310, 3250, 3169, 3126, 2982, 3002, 2954, 2935, 2921, 2905 (3809 e 3336 já feitos).
- **Alegações de teste (18 artigos):** piores 3523 (7), 3002 (6), 4541 (4).
- **3014 e 4537:** reconstruídos pelo cliente, falta colar no WP.
- **Outros:** deletar repo "Contex" do GitHub; discutir solução estrutural de preço (shortcode/campo dinâmico) quando a fila limpar.

---

## 8. Pendências transversais (painel WP, fora dos arquivos)

1. **Nome de exibição do perfil WP** → "Cristiano Martins" (hoje "Cristiano").
2. **Título SEO do Rank Math** nos 4 posts (3181: aspa reta → "50 polegadas"; 3809/3336: conferir; 4397: remover "Dia dos Pais 2026").
3. **Trocar o H1/título do 4397** no campo Título do WP (cliente ainda não escolheu o texto final).
4. **Decidir unificação dos shortlinks** por produto (item 4).

---

## 10. ⭐ Trabalho do OUTRO CHAT (workspace-1.zip, branch main)

Lido em 16/08/2026. O outro chat trabalhou em paralelo e já avançou em vários itens da MESMA fila. Sobreposições críticas:

### Já FEITO pelo outro chat (não refazer sem conferir)

- **4541** (`presentes-dia-dos-pais-2026-tech-premium`) — pacote **PERENE** pronto:
  `pais2026-PERENE.zip` → `CORPO-para-colar.html` (70 KB) + `SCHEMA-para-colar.html` +
  `pais2026-PERENE-v1.html` (página inteira p/ preview). Reposicionou sazonal→perene,
  removeu urgência ("ainda dá tempo 09/08"), preços→faixas (17 edições), 5× Offer→AggregateOffer,
  removeu priceValidUntil, autor "Cristiano"→"Cristiano Martins", fuso +03:00→-03:00.
  **IMPORTANTE:** o outro chat MANTEVE "Dia dos Pais 2026" no título/schema (diferente do
  que fiz no 4397, onde removemos por completo — alinhar com o cliente).
- **4537** (`apple-tv-4k`) — corrigido e JÁ PUBLICADO (0 erros: "Testamos a fundo"→"Analisamos",
  aggregateRating removido). Mas o `wpautop` injetou 21 `<br>`/10 `<p>` no grid do índice →
  existe `4537-apple-tv-CORRIGIDO-v2.html` (HTML **de linha única**, imune ao wpautop), ainda NÃO colado.
- **3181** — schema manual reconstruído (`schema-manual/3181-COLAR-NO-WP.html`): removeu `<br>` + aggregateRating.
  (Eu já reescrevi o 3181 inteiro com JSON-LD válido — resultado convergente.)
- **3014** (`purificador-agua-electrolux-pe12g`) — JSON-LD quebrado (FAQPage não fechava) reconstruído
  (`schema-manual/3014-COLAR-NO-WP.html` + `3014-schema-corrigido.json`). Cliente disse "reconstruído, falta colar".
- **3523** (`qcy-t13-anc`) — construiu **plugin WordPress "curadoria-conformidade"** com fluxo
  "Sugerir" (23 trechos: 7 alegações de teste + 13 preco_sem_data + 3). Abordagem DIFERENTE da minha
  (reescrever via plugin, sem abrir editor). Ver `FLUXO-3523-sem-copiar-nada.md`.
- **Lote de schema (29–32 artigos)** — `corrigir_artigos-v3-SCHEMA.py` com `corrigir_schema`/
  `_limpar_rating`/`_blocos_jsonld` (remove aggregateRating/reviewCount/ratingCount + padroniza
  `AUTOR_CANONICO="Cristiano Martins"`). NÃO está no repo atual (o repo tem a v2, sem schema).

### Achados importantes do outro chat (valem para TODOS os posts)

1. **Fuso horário errado no site:** WordPress emite `+03:00` (Moscou); corrigir em
   **Configurações → Geral → Fuso horário → São Paulo**. Afeta os 48 artigos (schema + meta tags).
2. **Autor fragmentado no schema (5 variantes):** `Cristiano` (48×), `Cristian` (17×),
   `Cristiano Martins` (10×), `Curadoria Prime` (6×), `Equipe Curadoria Prime` (4×) → padronizar
   `Cristiano Martins`. Obs: o outro chat usou `sameAs:[x.com/martinscs08, x.com/CuradoriaPrime]`; eu usei só `x.com/CuradoriaPrime` — alinhar.
3. **`wpautop` injeta `<br>`/`<p>`** quando cola HTML com quebras de linha no **Editor de código** do WP
   (quebra grids/badges). Solução do outro chat: entregar HTML **numa linha só** (sem newline).
   ⚠️ Meus arquivos usam `<!-- wp:html -->` (Gutenberg) — colados via Editor de código Gutenberg ficam
   protegidos; mas se colados via editor clássico, correm o mesmo risco. Conferir após salvar.
4. **Comentário HTML interno vazado** no 4541 (4.099 chars, tokens `PEND_`, "alucinação", dados pessoais
   do cliente, estratégia comercial) — apagar; e varrer os outros 48 por comentários internos.
5. **meli.la = etiqueta de afiliado** (confirma o que já tínhamos): `social/6620250626180940`, produto no `ref=`.
6. **`priceValidUntil` no passado derruba rich result** — remover sempre.
7. **`Offer.price` exige valor exato**; para faixa usar `AggregateOffer` (lowPrice/highPrice).
8. **Link.amazon redireciona via `amzlinks.in` (terceiro)** — alternativa direta: `amazon.com.br/dp/<ASIN>?tag=martins73-20`.

### Preços verificados pelo outro chat (15/08/2026, post 4541)

Apple Pencil Pro R$ 1.286,10 · Galaxy Watch7 R$ 1.399 · Anker 737 ML R$ 628,93 ·
Anker A1695 R$ 759,05 · Liberty 4 NC R$ 407,55 · JBL Wave Buds 2 R$ 242,25.

### Links de afiliado do 4541 (12, já com rel correto)

| Produto | Amazon | ML |
|---|---|---|
| Apple Pencil Pro | ASIN B0D3J71RM7 | — (sem nacional confiável) |
| Galaxy Watch7 44mm | B0D96V7WRB | meli.la/1LuqqHm |
| Anker 737 | B0DMDJBCDP (A1695) | meli.la/2uyvRWS |
| Soundcore Liberty 4 NC | B0BZV8HLX3 | meli.la/2BweosK |
| JBL Wave Buds 2 | B0DHL63KWK | meli.la/2JLLpU1 |

---

## 11. Impacto na fila da SESSÃO ATUAL

- **4541:** ✅ REFAZIDO na filosofia do 4397 (sem "Dia dos Pais 2026", sem teste físico,
  contras §2.7, faixas de 6 meses). Arquivo: `articles/presentes-dia-dos-pais-2026-tech-premium-artigo-completo.html`.
  Aprovado no checker. O pacote PERENE do outro chat serviu de base de conteúdo, mas foi
  reescrito em Gutenberg limpo (o dele tinha markup de tema + lazy-load).
- **4537:** ✅ CONFERIDO — já publicado com "Analisamos a fundo" + sem aggregateRating.
  Pendências menores: `author.url` aponta `/author/cristian/` (slug antigo) + "compra verificada" no corpo.
- **3523:** decisão = REWRITE MANUAL (meu padrão), não o plugin. Pesquisa aprofundada antes.
- **Lote de schema:** trazer o `corrigir_artigos-v3-SCHEMA.py` para o repo (a v2 atual não tem schema).
- **Fuso horário:** OK — usuário confirmou que já corrigiu.

### Faixas de preço 6 meses (pesquisadas 16/08, para 4541 e reuso)

Apple Pencil Pro R$ 1.100–1.500 · Watch7 44mm BT R$ 1.050–1.590 · Anker 737 (A1289) R$ 600–800 ·
Liberty 4 NC R$ 370–450 · JBL Wave Buds 2 R$ 220–290.
(Ver `audit/pesquisa-4541.md` para fontes/specs validadas.)

