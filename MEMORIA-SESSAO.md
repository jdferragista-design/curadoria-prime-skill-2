# 🧠 MEMÓRIA DA SESSÃO — Limpeza de Conformidade Curadoria Prime

> ⭐ **RETOMADA EM CHAT NOVO:** leia `audit/retomada-2026-08-16.md` — contém o
> registro completo da sessão E o prompt pronto para colar num novo chat.
>
> Registro do que foi feito nesta sessão (branch `arena/01a0028f-curadoria-prime-skill-2`;
> continuação em `arena/01a00f98-curadoria-prime-skill-2`).
> Atualizado em: **17/08/2026**. Serve para retomar o trabalho sem perder contexto.

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
| 5 | `samsung-u8600f-vs-lg-au801-vs-philips-50pug7019` | Samsung U8600F vs LG AU801 vs Philips | `articles/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019.html` | ✅ reescrito + validado (16/08) |
| 6 | `samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1` | Samsung HW-B400F vs JBL SB180 vs LG SQC1 | `articles/samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1.html` | ✅ reescrito + validado (16/08) |
| 7 | `samsung-s90f-qd-oled-review` | Samsung S90F QD-OLED | `articles/samsung-s90f-qd-oled-review.html` | ✅ reescrito + validado (16/08) |
| 8 | `philips-50pug7019-review` | Philips 50PUG7019 | `articles/philips-50pug7019-review.html` | ✅ reescrito + validado (16/08) |
| 9 | `good-vision-kit-cameras-wifi-review` | Good Vision Kit 2 Câmeras | `articles/good-vision-kit-cameras-wifi-review.html` | ✅ reescrito + validado (16/08) |

**Dossiês em `audit/`:** `estado-3181.md`, `estado-3809.md`, `estado-3336.md`, `estado-4397.md`, `estado-4541.md`, `estado-3153.md`, `estado-3226.md`, `estado-3139.md`, `estado-3183.md`, `estado-3033.md` + análises de layout `analise-3336-layout.md`, `analise-4397-layout.md`.

### 3153 (Samsung U8600F vs LG AU801 vs Philips 50PUG7019) — detalhes
- 9 links sponsored (3 topo + 3 tabela + 3 rodapé); shortlink Amazon da Samsung unificado em `4biQQdq` (o `4rhzNx7` descartado — confirmar com o cliente).
- Alegações de tempo/teste removidas (boot "15-20s", "Netflix 2-3s", "5× mais rápido", "depois de usar"); seção "Desempenho real" eliminada.
- Citações inventadas → "Síntese editorial dos relatos" (sem aspas/nome); "compradores verificados" → "avaliações publicadas por compradores".
- "Pontos de Atenção" ×3 (≥3 itens cada); preços em faixa com data 16/08/2026 (Samsung R$ 2.399 Amazon · LG R$ 2.242 ML · Philips volátil).
- JSON-LD: TechArticle + ItemList (4 itens) + FAQPage + BreadcrumbList, sem aggregateRating/offers, autor canônico.
- Philips 50PUG7300 (sucessora 2025) entra como OPÇÃO na seção da Philips (11 links sponsored no total): Amazon `link.amazon/B09uCSSBI` + ML `meli.la/27D4FgZ` (cliente).
- Pendências: colar no WP; confirmar shortlink Samsung; conferir specs Philips (HDMI 2.1 / 8 ms); α7 "Gen 8" vs 3181 "Gen 5".

### 3226 (Samsung HW-B400F vs JBL Cinema SB180 vs LG SQC1) — detalhes
- 9 links sponsored (3 topo + 3 tabela + 3 rodapé); divulgação já existia (14/08), corrigida para "avaliações publicadas por compradores" + box metodologia.
- "Pontos de Atenção" ×3; preços em faixa 16/08 (Samsung R$ 595–700 · JBL R$ 840–930 · LG volátil R$ 1.190→1.651).
- Spec Samsung corrigida: 40W RMS (não "20W consumo"). Link "Veja também" quebrado corrigido.
- ⚠️ LG SQC1 (2024) estoque reduzido; sucessora LG S40T (~R$ 894) caso queira trocar depois.
- Pendências: colar no WP; título "JBL SB180"→"JBL Cinema SB180"; conferir specs LG (BT 4.0 / sem ARC).

### 3033 (Good Vision Kit 2 Câmeras Wi-Fi) — detalhes
- 2 links sponsored (CTA topo + rodapé; o publicado tinha 3 âncoras, consolidadas em 2); "dados de compradores verificados" → "avaliações publicadas por compradores".
- "Desvantagens" → "Pontos de Atenção" (5 itens); nota 7,8/10 + "para quem NÃO é" adicionados (faltavam).
- "à prova d'água" → "resistente à água (IP66), não submersível" (§6). Alternativas 4K (G.Eye A28 / iCSee A28B) citadas.
- Categoria `casa-inteligente-e-seguranca` (427).
- ⚠️ Anúncio vinculado (shortlink 2w2H2mP) aparece "pausado"/última unidade em 16/08/2026 — cliente deve conferir/regenerar o link.
- 2 imagens são hotlinks do ML (http2.mlstatic.com) — cliente baixa e renomeia (padrão 3226).

### 3183 (Philips 50PUG7019) — detalhes
- 8 links sponsored (3 Philips 7019 + Samsung + LG + 2 da sucessora 7300); Samsung unificada em `4biQQdq` (o publicado usava `461ctv6`, mesma U8600F).
- "líder de vendas"/"mais inteligente"/"não trava" suavizados; "compradores verificados" → "avaliações publicadas por compradores"; box metodologia.
- Preços 16/08: 7019 (2024) fim de linha volátil; sucessora 50PUG7300 como OPÇÃO (R$ 1.935 ML / R$ 2.199 Amazon).
- 3 slugs "Veja também" quebrados corrigidos (comparativo 3153, `samsung-u8600f-review`, `lg-au801-50-review`); legenda triplicada do comparativo removida.
- JSON-LD: TechArticle + Product (8,7/10) + FAQ + Breadcrumb. Autor canônico.
- ⚠️ 50PUG7019 fim de linha: monitorar estoque (possível 301 futuro p/ 7300 ou consolidação no 3153).

### 3139 (Samsung S90F QD-OLED) — detalhes
- 4 links sponsored (2 Samsung + 2 LG); botões LG "Comparar Preços" do publicado estavam SEM href (quebrados) — corrigidos.
- 5 citações sem fonte ("Usuário verificado", Reddit, fórum) → síntese editorial; "depois de usar Magic Remote" e "3-5x mais rápido" suavizados.
- Placeholders vazados removidos ("[INSERIR FOTO 3/6]", "Nome do arquivo:", "Alt text:"); typos "WOOLD"→"WOLED"; texto duplicado corrigido.
- Preços 16/08: S90F R$ 6.478 (ML) · LG C5 R$ 5.851-6.595 (diferença ~R$ 600, não R$ 1.000).
- JSON-LD: TechArticle + Product (reviewRating 9,3/10) + FAQ + Breadcrumb.
- ⚠️ Shortlink LG C5 (`1rZFCkW`) resolve para LISTA VAZIA do afiliado — cliente precisa conferir/regenerar.

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

- **Urgência falsa:** ~~3336~~ ✓ · ~~4397~~ ✓ · ~~4541~~ ✓ (reposicionado, ver §11).
- **Comparativos P0 (sem sponsored):** ~~3153~~ ✓ · ~~3226~~ ✓ · ~~3139~~ ✓ (recolado e conferido 17/08) · ~~3183~~ ✓ · ~~3033~~ ✓ (16/08) · **2888 — diagnóstico feito (17/08), ver `audit/estado-2888.md`; reescrita aguarda 2 pendências de link do cliente** · 2884.
- **Lote de schema (29):** 4414, 4474, 4456, 4254, 4251, 4185, 4159, 4155, 3871, 3858, 3924, 3835, 3548, 3550, 3523, 3320, 3310, 3250, 3169, 3126, 2982, 3002, 2954, 2935, 2921, 2905 (3809 e 3336 já feitos).
- **Alegações de teste (18 artigos):** piores 3523 (7), 3002 (6), 4541 (4).
- **3014 e 4537:** reconstruídos pelo cliente, falta colar no WP.
- **Outros:** deletar repo "Contex" do GitHub; discutir solução estrutural de preço (shortcode/campo dinâmico) quando a fila limpar.

---

## 7b. ⭐ STATUS DOS 5 POSTS REESCRITOS — PUBLICADOS (conferido no ar 16/08/2026)
Todos os 5 posts desta sequência foram colados pelo cliente e conferidos no ar:

| Post | Estado no ar |
|---|---|
| 3153 (TVs) | ✅ correto (botões OK; hero trocada pelo cliente p/ `comparativo-tvs-samsung-lg-philips-2026-2048x1143.webp`) |
| 3226 (soundbars) | ✅ correto (imagens renomeadas `...-one-remote.webp` / `...-subwoofer-mdf.webp` / `...-sb180-subwoofer.webp` no ar) |
| 3139 (S90F) | ✅ **RESOLVIDO (17/08/2026)** — cliente recolou; conferido no ar: link C5 canônico `/p/MLB53613524`, "4,8/5 · ~38 (16/08)", aviso de estoque + gancho C6, autor canônico, JSON-LD limpo |
| 3183 (Philips) | ✅ correto (nota 8,7/10, fim de linha avisado, opção 7300) |
| 3033 (Good Vision) | ✅ correto (imagens locais lente dupla + visão noturna) |

### 7c. ⭐ Ganchos de estoque para PAUTA FUTURA (adicionados 16/08/2026)

Aviso "estoque baixo ou zerado" + motivo (sucessora chegando) + gancho "em breve:
review dedicado" adicionados em:

- **3139** (S90F): LG C5 com estoque baixo/zerado → gancho para **review LG C6 (2026)**.
- **3183** (Philips 7019): 7019 baixo/zerado → gancho para **review Philips 50PUG7300**.
- **3153** (comparativo TVs): idem, no bloco da 7300.

**PAUTA FUTURA (novos posts a criar quando tiver links/estoque):**
1. **LG C6 55″ (OLED55C6PSA)** — sucessora da C5; α11 Gen3, VRR 165Hz, webOS 26.
   Amazon ASIN `B0H4HKXMFH` (sem oferta destacada ainda) · ML ainda sem listagem.
2. **Philips 50PUG7300** — sucessora da 7019; Google TV + Dolby Atmos.
   Shortlinks já com o cliente: Amazon `B09uCSSBI` + ML `27D4FgZ`.

Quando esses posts saírem: trocar o texto "em breve…" pelos links internos reais.

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


---

## 12. Consolidação 4474/4476 — ✅ FECHADO (16/08)

- Canônica `tablets-para-volta-as-aulas-2026` (4476): corrigida, no ar.
- Canibal `-2` (4474): retarget → post novo `alternativas-galaxy-tab-s10-fe-ipad-estudar` (id 4884).
- 301 ativo (`-2/` → alternativas). Recíproco colado. Link quebrado corrigido.
- Skill criada: `skills/curadoria-reviews/` + `tools/reviews_ml.py`.


---

## 13. Sessão 17/08/2026 — retomada

### 13.1. 3139 (Samsung S90F) — ✅ FECHADO

Primeira tarefa da fila era "recolher o 3139". **Já estava resolvido:** o cliente
recolou em 16/08 às 21:03 (`modified` da REST API). Conferido no ar item a item
contra os sintomas registrados — todos corrigidos. Dossiê `audit/estado-3139.md`
atualizado para ✅ FECHADO. Revalidação local: **✅ Aprovado, 0 erros / 0 alertas**,
4/4 links sponsored, zero base64.

Pendências que **continuam com o cliente** (não bloqueiam o post):
gerar shortlink ML novo para a LG C5 (`1rZFCkW` quebrado — hoje o artigo usa o
link canônico como fallback) e monitorar o retorno de estoque na Amazon
(ASINs S90F `B0FNT5H95K` · C5 `B0F5X3WY5N`).

### 13.2. 2888 (Kit Teclado e Mouse Ultra Slim) — 🔎 DIAGNÓSTICO

Dossiê completo em **`audit/estado-2888.md`**. O CSV subestimava o risco: são
**14 alegações de teste físico**, não 2 (o artigo inteiro é narrado como unboxing).
Achados principais:

- 0/6 links com `rel="sponsored"`;
- **link Amazon do produto principal aponta para o ASIN ERRADO** (`B0dKNIkQE` →
  `B0B59YC5N4`, um kit **preto** diferente do Ultra Slim branco do review);
- 2 dos 6 botões são **buscas genéricas do ML** (`?q=logitech+mk235` / `+mk270`),
  sem tracking e sem checkout;
- JSON-LD com **`<br />` em cada linha** (colado em bloco de parágrafo → Google
  descarta), `offers.price` fixo R$ 69,90, `availability: InStock` inventado,
  `offers.url` apontando para slug inexistente `/kit-teclado-mouse-slim-review/`,
  autor como `Organization`, sem Article e sem BreadcrumbList;
- 5 aspas de "usuários" sem plataforma/data; "dados de compradores verificados";
- **sem bloco de autor**, **sem "Fontes consultadas"**, **sem box "Tipo de análise"**;
- auto-link (aponta para si mesmo) + link **404** para `/review-logitech-mk270/`;
- instrução interna vazada ao leitor (dica de instalar o plugin "Table of Contents Plus");
- Anatel nº 210032214394 e sensor "Pro Elite" **não verificáveis** → `[VERIFICAÇÃO HUMANA NECESSÁRIA]`.

**Capturas 17/08/2026:** Ultra Slim ML **MLB-4168372465** R$ 63,99 (cupom) /
R$ 64,99 · MK235 Amazon **B07643MPGS** · MK270 Amazon **B074WL3VZF** R$ 152,93.

**Bloqueios para a reescrita** (4 pendências do cliente, ver §4 do dossiê):
shortlink Amazon correto do produto principal, shortlinks ML de MK235/MK270,
confirmação da Anatel e definição da categoria WP do post.


---

## 14. Mudança de cadência (17/08/2026): 3 artigos por vez

Cliente pediu para trabalhar **3 por vez, escolhendo artigos que compartilhem
produtos**. Critério adotado: agrupar por **cluster de produto**, para que uma
captura de preço e uma decisão editorial sirvam aos 3 — e para não gerar
divergência entre posts que se citam.

**Lote escolhido — CLUSTER ÁUDIO:** 3523 (QCY T13 ANC) · 3545 (Galaxy Buds Core) ·
3527 (Edifier W820NB). Os três se citam mutuamente como alternativa e apontam para
o guia-mãe 3336. Dossiê: **`audit/estado-cluster-audio.md`**.

### Achados que mudam o plano

1. 🔴 **Edifier W820NB fora de linha/ruptura.** Publicado a "R$ 399"; hoje (17/08) a
   Amazon marca **"Não disponível"** e o ML pede **R$ 708,39** ("último disponível").
   Sucessor **W820NB Plus V25** a R$ 499 nas duas lojas. Isso contamina **3 posts**
   (3527, 3545 e 3523 citam o preço antigo) + o guia 3336. Gatilho nível 1 da §17.2.
2. 🔴 **3545 narra teste físico que não houve**: "testamos durante duas semanas em
   três cenários reais" (Galaxy S25 / Xiaomi 14T / iPhone 15), tabela de 4 cenários de
   chamada com aspas de participantes, "testes de conforto de até 3 horas", comparação
   direta com o QCY "no mesmo teste" e "unidade adquirida pelo autor". É o pior caso
   de veracidade encontrado até agora na fila.
3. 🟢 **3523 já teve as 7 alegações corrigidas** (reescrita de 15/08) — o CSV está
   desatualizado. Restam citações com aspas, `priceValidUntil` e FAQ do schema
   divergente da FAQ visível.
4. 🟡 **Slugs curtos** (`/qcy-t13-anc-review/`, `/edifier-w820nb-review/`, etc.) usados
   nos links internos dos 3 — resolvem por 301, mas devem apontar para o canônico.
5. 🟡 **3545 com `<br/>` já injetado dentro dos cards de compra** — wpautop corrompeu
   o HTML publicado (problema da §10.3).

### Capturas 17/08/2026 (servem aos 3 posts + ao guia 3336)

| Produto | Amazon | ML |
|---|---|---|
| QCY T13 ANC | `B0BWRBKMCK` R$ 186,10 | `MLB34102640` **R$ 199** (era R$ 169 → +18%) |
| Galaxy Buds Core | `B0FP8KDP36` **R$ 219,31 Pix** / R$ 243,68 | `MLB57492226` R$ 243,68 (branco) · R$ 279,37 (preto) |
| Edifier W820NB | `B09MDC77QX` ⛔ **esgotado** | `MLB19052273` **R$ 708,39** (último) |
| W820NB Plus V25 (sucessor) | `B0G534R9BZ` R$ 499 | `MLB63419175` R$ 499 |

### Bloqueios antes de reescrever

1. Destino do 3527 (Edifier): suspender bloco de compra + apontar Plus V25
   (recomendado), trocar o produto principal, ou manter sem CTA.
2. Shortlinks do W820NB Plus V25.
3. **Confirmar que não houve teste físico no 3545** — se houve, preciso das 8
   evidências da §2.2; senão, removo toda a narrativa.
4. Notas duplas (3545 e 2888) → unificar?

### Fila seguinte sugerida

Completar o cluster áudio: **3548** (Redmi Buds 6 Play) + **3550** (JBL Wave Buds 2)
+ **2888** (Kit Teclado, diagnóstico já pronto e bloqueado por links).

---

## 15. Sessão 17/08/2026 (tarde) — cluster áudio fechado e auditado contra dados reais

### 15.1 Entregas
| Post | Arquivo | Palavras | Checker |
|---|---|---|---|
| 3527 Edifier W820NB | `articles/edifier-w820nb-review-2026-vale-a-pena.html` | 5.570 | 14/14 ✅ |
| 3545 Galaxy Buds Core | `articles/samsung-galaxy-buds-core-vale-a-pena.html` | 5.106 | 14/14 ✅ |
| 3523 QCY T13 ANC | `articles/qcy-t13-anc-review-2026-vale-a-pena.html` | 6.263 | 14/14 ✅ |

Commits: `0c05723` → `cbe942d` (12 no total). Dossiê: `audit/estado-cluster-audio.md` §7–§14.
CSV `audit/auditoria-48-artigos.csv` atualizado: 3523, 3527 e 3545 marcados CORRIGIDO-17/08/2026.

### 15.2 🔴 LIÇÃO CENTRAL DA SESSÃO — seções de "problemas" eram inferência
Nos **três** artigos a seção "Problemas relatados por compradores" tinha sido escrita por dedução
plausível, com rótulos de falsa precisão ("Frequência: alta/moderada"). O texto era verossímil e
**não disparava o checker**. Só o cruzamento com dumps reais de avaliações expôs:

| Artigo | Afirmação publicada | Ocorrências reais |
|---|---|---|
| 3523 | queda de conexão em shopping/academia | **0** |
| 3523 | app não reconhece no 1º pareamento | **0** |
| 3523 | latência no modo jogo em iPhone | **0** |
| 3523 | ponteira M grande demais | **0** |
| 3523 | chiado com vento = queixa mais comum | **0** — os 2 relatos de vento são ELOGIOS |
| 3527 | demora para reconectar no Android | **0** |
| 3527 | instabilidade do app no iOS | **0** |
| 3527 | almofadas de veludo "R$ 40 a R$ 60" | **preço inventado** |
| 3545 | conexão instável em notebook Windows | **0** — única menção a Windows é elogio |
| 3545 | ANC percebido como fraco (2-3★) | **0** — ANC aparece como positivo |

**REGRA NOVA (vale para toda a fila):** seção de problemas só se houver dump de avaliações.
Sem dump, declarar explicitamente que a lista é dedutiva. Nunca rotular frequência sem contagem.

**REGRA 2:** não basta ler as notas 1-3★. Os defeitos de longo prazo (botões que afundam aos 2
anos, espuma que descasca aos 8 meses) só aparecem **dentro de avaliações 5★**. Minerar por tema,
não por nota.

### 15.3 Números corrigidos (haviam sido obtidos por busca, não por captura)
| Produto | publicado | **real (dump)** |
|---|---|---|
| Buds Core Amazon | 4,7/5 · ~164 | **4,8/5 · 2.883** (88% 5★) — erro de 18× |
| Buds Core ML | 4,9/5 · ~11.283 | 4,9/5 · **7.116** |
| QCY Amazon | 4,6/5 · ~751 | **4,6/5 · 750** (81% 5★) |
| QCY ML | 4,8/5 · ~6.546 | **4,8/5 · 6.630** (+10 mil vendidos) |
| Edifier Amazon | — | **4,7/5 · 1.483** (82% 5★) |
| Plus V25 ML | — | **4,9/5 · apenas 21 opiniões** |

### 15.4 Achados que mudaram cards de compra
- **Plus V25**: só 21 opiniões, e **um comprador que tinha o W820NB original considerou o ANC da
  Plus V25 INFERIOR** (vazamento pela espuma). O card a recomendava como upgrade natural →
  ressalva publicada: a única melhoria documentada é o Bluetooth 6.1.
- **Cor do W820NB branco**: 10 menções de que o tom real é **off-white com almofadas bege**. É a
  cor que o card vende → aviso no card e na seção de problemas.

### 15.5 Infraestrutura: anexos de chat NÃO chegam
O sandbox reinicia a cada turno (`uptime` = 1 min) e só persiste o que está **dentro do repositório**.
Anexos vão para `/home/user/uploads/`, fora dele → somem antes de qualquer leitura. Duas tentativas
falharam. **Solução adotada: cliente commita os dumps direto no GitHub** (`28ad6ee`, `f2ce32d`) e eu
dou `git fetch`. Dumps agora versionados em `articles/*.txt` — disponíveis em qualquer sessão futura.

### 15.6 Dumps de avaliações disponíveis no repo
`QCY-T13-ANC.amazom.txt` · `Fone-Qcy-T13-AncML.txt` · `W820NB-Edifier-amazon.txt` ·
`W820NB-Plus-V25-ML.txt` · `Samsung-Galaxy-Buds-Core-amazon.txt` · `Samsung-Galaxy-Buds-ML.txt` ·
`Wave-Buds-2.txt` · `soundcore-Liberty-4.txt` · `Anker.txt` · `Samsung-Galaxy-Watch7.txt`

⚠️ Viés recorrente: capturas do ML e da Amazon do Buds Core trazem quase só 4-5★. Declarar nos artigos.

### 15.7 Próximo: 3336 (guia-mãe Top 5)
Botão ML do Edifier `meli.la/1pXMdaD` → lista vazia (quebrado, no ar). Preços de 14/08 desatualizados.

## 🔴 CADÊNCIA — UM ARTIGO POR VEZ (17/08/2026)

> "Vamos voltar para um por vez, muitos de uma vez eu me confundo."

**Substitui a instrução anterior de trabalhar 3 artigos por vez.**

Regras da cadência:
- Trabalhar **um único artigo** do começo ao fim antes de abrir o próximo.
- Entregar, esperar o retorno do cliente, só então seguir.
- Não misturar produtos ou posts diferentes na mesma resposta.
- Não abrir frente nova enquanto o artigo atual não estiver fechado.
- Vale também para as correções: uma pendência por vez, não lotes.


## 🔴 REGRA PERMANENTE — PRESERVAÇÃO DE IMAGENS (17/08/2026)

> "Mantenha sempre as imagens ao atualizar os artigos. Nunca remova as imagens de
> artigos que forem atualizados. É obrigatório preservar as imagens originais
> durante a atualização dos artigos."

Vale para **todo** artigo, em **toda** atualização. Antes de commitar qualquer
edição em `articles/*.html`:

```
python3 tools/checar_imagens_preservadas.py articles/<arquivo>.html
```

O hook `.githooks/pre-commit` bloqueia o commit automaticamente.
Ativar em sandbox novo: `git config core.hooksPath .githooks`

Detalhes e procedimento: §22 de `skills/curadoria-review/references/regras-editoriais.md`
