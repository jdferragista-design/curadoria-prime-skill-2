# ESTADO DO POST 3181 — LG AU801 50 polegadas

**Atualizado:** 13/08/2026
**URL:** https://curadoriaprime.com/lg-au801-50-review/
**Status:** ✅ artigo completo pronto — **aguardando colagem no WordPress**

---

## 🎯 ENTREGÁVEL PRINCIPAL

**`/home/user/correcoes/3181-LG-AU801/3181-ARTIGO-COMPLETO.html`** (78 KB)

Artigo inteiro, já corrigido, construído **em cima do HTML publicado** (layout,
cores e componentes originais preservados). Substitui todo o conteúdo do post.

### Como aplicar
1. WordPress → post 3181 → menu ⋮ (canto superior direito) → **Editor de código**
2. Apagar **todo** o conteúdo atual
3. Colar o arquivo **inteiro** (o comentário do topo pode ficar, é invisível no site)
4. Atualizar

### ⚠️ Duas coisas que NÃO estão no arquivo (fazer no painel)
1. **Rank Math → Título SEO:** trocar a aspa reta de polegada por `50 polegadas`.
   Hoje está `LG AU801 50" Vale a Pena? Review 2026`. A aspa reta **quebra o
   JSON-LD gerado pelo plugin** e não é corrigível pelo conteúdo do post.
   Isso conserta `<title>` + `og:title` + schema do Rank Math de uma vez.
2. **Perfil do usuário WP:** nome de exibição → `Cristiano Martins`
   (hoje é só `Cristiano`; afeta também o `twitter:data1`).

### Validar depois de publicar
```bash
curl -s https://curadoriaprime.com/lg-au801-50-review/ \
  | grep -c '1\.941\|verificado há\|Estoque limitado\|aggregateRating\|815'
# esperado: 0
```
Depois: https://search.google.com/test/rich-results
→ devem aparecer 4 nós válidos (TechArticle, Product, FAQPage, BreadcrumbList),
  sem aviso de rating agregado.

---

## ✅ AS 13 CORREÇÕES APLICADAS

| # | Problema | Solução |
|---|---|---|
| 1 | `⏰ Preço verificado há 2 horas \| Estoque limitado` (vermelho `#e11d48`, negrito) | Faixa + data fixa em cinza `#7c7c9a` + "marketplaces alteram preços sem aviso" |
| 2 | `R$ 1.941` no hero | `R$ 1.973 – R$ 2.088` |
| 3 | `R$ 1.941` na intro | faixa + `(agosto/2026)` |
| 4 | `R$ 1.941` no CTA principal | faixa + data de consulta |
| 5 | `R$ 1.941` em "Preço médio" (specs) | linha vira **"Faixa de preço"** `R$ 1.973 – R$ 2.088 (ago/2026)` |
| 6 | `R$ 1.941` na tabela comparativa | `R$ 1.973` |
| 7 | `~R$ 1.941` no box final | `R$ 1.973 – R$ 2.088` |
| 8 | "Philips vence em preço (**R$ 47** mais barata)" | **R$ 79** (1.973 − 1.894) |
| 9 | "**testamos** os pontos mais críticos" | "cruzamos com **medições publicadas por laboratórios independentes**" |
| 10 | "mais de **815** compradores verificados" (intro) | "relatos de compradores verificados" (sem número inflado) |
| 11 | Linha `Reviews 815 / 194 / 9.091` na tabela | **linha removida** — comparava contagens de lojas diferentes |
| 12 | "acumula cerca de **815** avaliações com média 4.6" | "**4,6 de 5** em **50 avaliações** (Amazon, 13/08/2026)" + ressalva de volume baixo |
| 13 | Heading "Upscaling: Onde a LG AU801 **Massacra** a Concorrência" | "**se Destaca da** Concorrência" |

**Datas:** rodapé `Julho de 2026` → `13 de agosto de 2026`;
box final `Preços verificados em Julho/2026` → `Preços consultados em 13/08/2026`.

---

## ➕ BLOCOS NOVOS (não existiam no post)

Todos escritos no **vocabulário visual do próprio post**, não em estilo inventado.

1. **🔍 Como avaliamos esta TV** — card branco, borda-esquerda `4px #1a1a2e`,
   itens com `✓` em absolute. Posição: logo antes da divulgação de afiliado.
   Declara: **não recebemos unidade para teste em bancada**; a análise é
   documental (specs oficiais + medições de terceiros + relatos de compradores
   + monitoramento de preço).
2. **❌ Limitações que você precisa aceitar** — card `#fff1f2` / borda `#e11d48`,
   5 contras consolidados (contraste IPS, brilho, sem 120 Hz/VRR/ALLM, som,
   busca do WebOS). Posição: antes do card de notas.
3. **📚 Fontes consultadas** — clone visual do "📺 Veja também", 3 links
   (LG Brasil, Amazon BR, Mercado Livre) com data de consulta.
4. **✍️ Bloco do autor** — ver seção própria abaixo.

---

## 🖼️ IMAGENS — ARMADILHA RESOLVIDA

O HTML publicado tem lazy-load do plugin:
```html
<img data-lazyloaded="1"
     src="data:image/svg+xml;base64,..."   ← placeholder cinza
     data-src="https://curadoriaprime.com/...webp">   ← URL real
```
Ao copiar o markup publicado, vinha o **placeholder** no `src`.
Se colado assim, o placeholder ficaria **gravado no banco** como imagem oficial.

**Correção:** `data-src` → `src`; removidos `data-lazyloaded`, `data-src`,
`data-srcset`, `data-sizes`. Mantido `loading="lazy"` nativo (o plugin reaplica
o dele em cima da URL certa).

Também corrigido: `title="Review LG AU801 50&quot;: ..."` → `50&#8243;` (7 imagens).

**As 7 imagens do corpo, verificadas por `curl` em 13/08/2026 (todas HTTP 200):**

| # | Arquivo | Peso |
|---|---|---|
| 1 | `LG-AU801-em-ambiente-de-sala-exibindo-conteudo-de-TV-e1769374039853.webp` | 145 KB |
| 2 | `D_NQ_NP_2X_722466-MLA101387258064_122025-F.webp` | 23 KB |
| 3 | `lg-painel-ips-angulo-visao.webp` | 29 KB |
| 4 | `LG-Suporte-Interativo-AI-Chatbot-Interface-e1769260136122.webp` | 127 KB |
| 5 | `webOS-para-entretenimento-LG-BR.png` | 208 KB |
| 6 | `LG-AI-Magic-Remote-Recursos-Inteligentes-e1769259838998.webp` | 58 KB |
| 7 | `webOS-para-entretenimento-LG-BR-1.png` | 219 KB |

(8ª imagem = foto do autor.)

⚠️ **Pendência aberta:** a imagem #7 está na seção de **Gaming** com alt
"LG AU801 conectada a console de videogame", mas o nome do arquivo
(`webOS-para-entretenimento-LG-BR-1.png`) sugere que é variação do print do
WebOS (imagem #5). Provável que a imagem certa de gaming nunca tenha sido
enviada. **Conferir na biblioteca de mídia.**

---

## ✍️ BLOCO DO AUTOR — CANÔNICO

**Arquivo:** `/home/user/correcoes/_BLOCO-AUTOR-CANONICO.html`
(duas variantes de paleta + trecho de JSON-LD)

🔴 **REGRA PERMANENTE: este bloco é fornecido pelo usuário. NÃO inventar
variação, NÃO recriar. Colar este.** (Errei isso uma vez: escrevi um bloco
genérico com avatar de iniciais em CSS. O usuário corrigiu.)

Conteúdo: foto real, nome, "fundador e editor-chefe", motorista de aplicativo em
Uberlândia (MG), **+16 mil viagens Uber/99**, 8+ h/dia com GPS/apps/fones
Bluetooth, link "Seguir no X →".

**Por que é superior ao que eu tinha feito:** entrega o primeiro **E** do E-E-A-T
(Experience) com credencial específica e checável, e uma entidade verificável
fora do site. Resolve a tensão do post: quem depende de tecnologia 8 h/dia tem
autoridade para julgar o que aguenta uso real, mesmo sem bancada de laboratório.

**Recursos verificados 13/08/2026:**
- Foto `https://curadoriaprime.com/wp-content/uploads/2026/08/cristiano-curadoria-prime.jpg` → HTTP 200, 20.476 bytes, image/jpeg
- `https://x.com/CuradoriaPrime` → HTTP 200

**Adaptação de paleta feita no 3181** (texto e estrutura intactos):
`#f8fafc`→`#f5f5fb` · `#e2e8f0`→`#e2e2f0` · `#334155`→`#4a4a68` ·
`#64748b`→`#7c7c9a` · link do X mantido em `#1d4ed8`.
Acrescentados `loading="lazy"` e `decoding="async"` na foto.

---

## 🔧 JSON-LD

**Antes:** 3 blocos separados, todos corroídos por `<br />` do `wpautop`, com
`aggregateRating` 4.6/815, `offers` com preços de **concorrentes** (1894–2154),
autor `Cristiano`, fuso `+03:00` (Moscou).

**Depois:** um único `@graph` com 4 nós — `TechArticle`, `Product`, `FAQPage`
(6 perguntas), `BreadcrumbList`.

- ❌ `aggregateRating` / `reviewCount` — **removidos** (rating externo é proibido, §2.4)
- ✅ `review` 8.4/10 — mantido (avaliação própria, legítima)
- ✅ `offers`: `AggregateOffer` `lowPrice 1973` / `highPrice 2088` / `offerCount 2`
- ✅ `datePublished` `2026-01-27T08:00:00-03:00` · `dateModified` `2026-08-13T12:00:00-03:00`
- ✅ `author` = Person **Cristiano Martins** com `jobTitle`, `description`,
  `image` e **`sameAs: ["https://x.com/CuradoriaPrime"]`**
- ✅ Zero aspa reta (`50"`) — usa `50 polegadas` / `50″` (U+2033)

---

## 🧾 DADOS DE REFERÊNCIA DO POST

**Preços reais (13/08/2026)**
- Mercado Livre `MLB61517857` (TNT Info): **R$ 1.973** Pix / R$ 2.077 em 10×
- Amazon `B0FRHV3HCG`: **R$ 2.088,10** Pix
- Philips 7019: R$ 1.894 · Samsung U8600F: R$ 2.154
- Diferença LG × Philips = **R$ 79**

**Avaliações reais:** Amazon 4,6/5 com **50 avaliações** (print enviado pelo usuário)

**8 links de afiliado, na ordem (todos com `rel="sponsored noopener noreferrer nofollow"`)**
1. `mercadolivre.com/sec/2eZsRku` — CTA principal
2. `link.amazon/B03wia3Ue` — CTA principal
3. `mercadolivre.com/sec/2eZsRku` — CTA intermediário (pós-upscaling)
4. `mercadolivre.com/sec/2eZsRku` — cabeçalho da tabela comparativa
5. `amzn.to/4biQQdq` — Samsung, tabela
6. `mercadolivre.com/sec/2BCYUF5` — Philips, tabela
7. `mercadolivre.com/sec/2eZsRku` — box final
8. `link.amazon/B0bDYSbFl` — box final

**3 links internos ("Veja também")**
- `/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019-qual-tv-4k-50-comprar/`
- `/samsung-u8600f-50-vale-a-pena-em-2025-review-completo-da-crystal-uhd-4k/`
- `/philips-50pug7019-50-2025-google-tv-som-acima-da-media-e-preco-competitivo-a-surpresa-do-varejo-brasileiro/`

**Notas:** Upscaling 9.5 · Design 8.5 · Imagem 7.5 · WebOS 8.5 ·
Magic Remote 9.5 · Custo-Benefício 8.0 · **Geral 8.4**

---

## 🎨 SISTEMA VISUAL DO POST (para reusar nos próximos)

Descoberto ao auditar o HTML publicado. **Não inventar paleta** — é este.

| Elemento | Padrão |
|---|---|
| Hero / CTA escuro / rodapé | `linear-gradient(135deg,#1a1a2e 0%,#16213e 100%)`, destaque `#fde68a` |
| Texto corrido | `#4a4a68` · títulos `#1a1a2e` · secundário `#7c7c9a` |
| Bordas / divisórias | `#e2e2f0` · fundo alternativo `#f5f5fb` |
| Caixa positiva | `#f0fdf4` + borda-esquerda `4px #22c55e`, texto `#14532d`/`#166534` |
| Caixa negativa | `#fff1f2` + borda-esquerda `4px #e11d48`, texto `#9f1239` |
| Caixa azul (destaque BR) | `linear-gradient(135deg,#eff6ff,#dbeafe)` + borda `2px #3b82f6` |
| Listas | parágrafos com prefixo `▸` ou `✓` (`position:absolute; left:0`) — **não** `<ul>` |
| Tabelas | wrapper `overflow-x:auto` + `border-radius` + `box-shadow`; thead em gradiente escuro, uppercase 12px; zebra `#f5f5fb`/`#fff`; vencedor em `#22c55e` bold |
| Cards FAQ | `#fff`, `border-radius:12px`, pergunta com borda inferior, `box-shadow: 0 2px 8px rgba(26,26,46,.07)` |
| Headings | `<h2 class="wp-block-heading">`, alguns com `has-text-align-center` |
| Separadores | `<hr class="wp-block-separator has-alpha-channel-opacity"/>` (15 no post) |
| Botão ML | `#ff9900` · Botão Amazon escuro `#1a1a2e` com borda branca |

---

## 📁 ARQUIVOS

| Caminho | O que é |
|---|---|
| `3181-LG-AU801/3181-ARTIGO-COMPLETO.html` | 🎯 **ENTREGÁVEL** — colar no WP |
| `3181-LG-AU801/_original-publicado.html` | página publicada inteira (backup) |
| `3181-LG-AU801/_corpo-bruto.html` | só o `post-content` extraído (base da edição) |
| `3181-LG-AU801/CORRECOES.md` | pacote anterior de 8 itens (trechos localizados) |
| `3181-LG-AU801/3181-COLAR-NO-WP.html` | só o JSON-LD corrigido (superado pelo completo) |
| `3181-LG-AU801/3181-bloco-preco-CORRIGIDO.html` | só o bloco de preço (superado) |
| `_BLOCO-AUTOR-CANONICO.html` | bloco do autor, 2 variantes + JSON-LD |
| `ESTADO-3181.md` | este arquivo |

---

## ✅ VALIDAÇÃO DO ARQUIVO FINAL

```
JSON-LD .................. válido (4 nós)
divs balanceadas ......... 0 (abre = fecha)
imagens .................. 8, todas src HTTP, 0 base64, 0 alt vazio
links de afiliado ........ 8, ordem original preservada, 8/8 rel=sponsored
tabelas .................. 6   headings h2 ... 15   separadores ... 15
termos-problema .......... 0 ('1.941', '815', 'R$ 47', 'Julho',
                              'testamos', 'aggregateRating',
                              'Estoque limitado', 'Massacra', '+03:00')
aspa reta no texto ....... 0
```

---

## ⏭️ DEPOIS DO 3181

Protocolo do usuário: **um post por vez, resolver tudo antes de passar adiante.**

Fila de urgência falsa: **3809** (próximo) → 3336 → 4397 → 4541.
Outras filas: lote de schema (29 posts) · colagem do 3014 · 36 alegações de
teste + 2 em `description` · 4537 · deletar o repo `Contex`.

**Causa-raiz a discutir depois:** preço fixo escrito no corpo do texto nasce
certo e apodrece sozinho. Solução estrutural (shortcode / campo dinâmico /
bloco reutilizável) deve ser tratada quando os posts fecharem.
