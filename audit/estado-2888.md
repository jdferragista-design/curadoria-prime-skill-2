# ESTADO — 2888 (Kit Teclado e Mouse Ultra Slim)

**Status:** 🔎 DIAGNÓSTICO CONCLUÍDO (17/08/2026) — aguardando decisão do cliente antes da reescrita

- URL: https://curadoriaprime.com/kit-teclado-mouse-ultra-slim/
- Slug: `kit-teclado-mouse-ultra-slim`
- Título atual: "Kit Teclado e Mouse Ultra Slim: Review 2026 (Vale a Pena?)"
- Publicado: 15/01/2026 · Modificado: 14/08/2026
- Auditoria (CSV): risco 11 · 2 alegações ("testamos", "unboxing") · 0/6 links com `sponsored` · sem divulgação adequada
- Entregável previsto: `articles/kit-teclado-mouse-ultra-slim.html`

---

## 1. Problemas ENCONTRADOS no publicado

### 1.1. Alegações de teste físico (bloqueio §2.1) — o problema mais grave

O artigo inteiro é narrado como se a unidade tivesse sido comprada, aberta e usada.
Não são 2 ocorrências como o CSV indicava — são **14 trechos** que só se sustentam
com contato físico:

| # | Trecho publicado | Regra ferida |
|---|---|---|
| 1 | Seção inteira **"📦 Unboxing e Primeiras Impressões"** (título + índice) | §2.1 "fizemos unboxing" |
| 2 | "Ao abrir, **encontramos**: …" | §2.1 |
| 3 | "A primeira impressão **ao tirar o teclado da caixa** é de surpresa pela leveza" | §2.1 sensorial |
| 4 | "Ele é **visivelmente mais fino** do que a maioria dos teclados de membrana" | §2.1 sensorial |
| 5 | "acabamento em branco fosco que **transmite sofisticação**" | §2.1 sensorial |
| 6 | "O plástico é bem acabado, **sem rebarbas**, e as teclas têm uma impressão de letras nítida" | §2.1 sensorial |
| 7 | "o curso das teclas é curto e a **resposta tátil é suave**" | §2.1 sensorial |
| 8 | "**Em nosso teste**, ele foi significativamente mais silencioso do que combos concorrentes" | §2.1 medição inventada |
| 9 | "No uso diário, o kit **se mostrou confiável** e sem surpresas desagradáveis" | §2.1 |
| 10 | "A conexão 2.4GHz foi **estável durante todo o período de testes** — sem perda de sinal, delays perceptíveis ou caracteres fantasma" | §2.1 + §2.3 |
| 11 | "**Testamos** em Windows 10, Windows 11, macOS e Linux (Ubuntu), e em todos o reconhecimento foi instantâneo" | §2.1 |
| 12 | "**Compatibilidade testada e confirmada**" (lista de 6 SOs) | §2.1 |
| 13 | "📊 Desempenho na prática — **nossas impressões**" (lista com ✅/❌) | §2.1 |
| 14 | "o clique é suave e a roda de rolagem funciona de forma consistente" | §2.1 sensorial |

**Não há box de "Tipo de análise"** em lugar nenhum do artigo — nem metodologia,
nem a frase obrigatória "a Curadoria Prime não testou esta unidade fisicamente".

### 1.2. Links de afiliado (0/6 com `sponsored`)

6 links de compra, **nenhum** com `rel="sponsored noopener noreferrer nofollow"`:

| Card | Loja | href publicado | Resolve para |
|---|---|---|---|
| Kit Ultra Slim | Amazon | `link.amazon/B0dKNIkQE` | ⚠️ **ASIN B0B59YC5N4 — "Kit Teclado e Mouse Sem Fio … PRETO Ergonômico"** (R$ 56,55, 17/08). **Não é o produto do review** (branco, ultra slim) |
| Kit Ultra Slim | ML | `mercadolivre.com/sec/1u195Cz` | ✅ MLB-4168372465 "Kit Teclado e Mouse Sem Fio USB Ultra Slim Wireless 2.4GHz" (HOME BLESS) — R$ 63,99 c/ cupom (de R$ 64,99) |
| Logitech MK235 | Amazon | `link.amazon/B0hVNG47T` | ✅ ASIN B07643MPGS (MK235, 4,7/5 · 21.563 avaliações) |
| Logitech MK235 | ML | `mercadolivre.com.br/s?q=logitech+mk235` | ❌ **busca genérica, sem afiliado e sem checkout** (fere o checklist de mercado) |
| Logitech MK270 | Amazon | `link.amazon/B0dRqNKEG` | ✅ ASIN B074WL3VZF (MK270) |
| Logitech MK270 | ML | `mercadolivre.com.br/s?q=logitech+mk270` | ❌ **busca genérica, sem afiliado e sem checkout** |

### 1.3. Prova social indevida e "compradores verificados"

- Box de transparência: *"nossa nota é baseada em pesquisa técnica e **dados de compradores verificados**"* → proibido pela §4.2 (sem selo explícito da plataforma). Trocar por "avaliações publicadas por compradores".
- Seção "Problemas Comuns" usa **5 aspas duplas** ("Não encontrei o receptor USB na caixa", "O mouse trava/desconecta…", "As pilhas acabam rápido", "O teclado é muito fino, escorrega na mesa", "Não funciona na minha Smart TV") apresentadas como falas de compradores, **sem plataforma, sem data e sem link** → §4.2 "transformar paráfrase em citação direta". Converter em **Síntese editorial dos relatos**, sem aspas.
- "a **taxa de satisfação** dos compradores é bastante positiva" — número/afirmação sem fonte.
- "⭐ 4,3 ML" no card — nota externa sem data de consulta (§2.4 permite no texto, mas exige fonte + data).

### 1.4. JSON-LD (parse quebrado + dados proibidos)

O bloco `<script type="application/ld+json">` está num bloco de **parágrafo**, e o
WordPress injetou **`<br />` em toda linha** — exatamente a falha da MEMÓRIA §2.4.
**O Google descarta esse schema.** Além disso:

- `Product.offers.price = "69.90"` **fixo** → §2.5 (preço volátil sem captura do dia; o ML está R$ 63,99 e a Amazon R$ 56,55 em 17/08);
- `offers.availability = InStock` inventado → §2.5;
- `offers.url` aponta para **`/kit-teclado-mouse-slim-review/`** — URL que **não existe** (o slug real é `kit-teclado-mouse-ultra-slim`);
- `review.author` = `Organization "Curadoria Prime"` → deve ser `Person "Cristiano Martins"` (§2.6 / padrão da sessão);
- `reviewRating` sem `worstRating`;
- **não há** `TechArticle`/`Article`, nem `BreadcrumbList` — o `@graph` só tem FAQPage + Product.

### 1.5. Links internos quebrados / canibalização

| Link no texto | Destino | Situação |
|---|---|---|
| "guia completo com os melhores teclados para home office em 2026" | `/kit-teclado-mouse-ultra-slim/` | ❌ **auto-link** — aponta para o próprio artigo |
| "review detalhado do MK270" | `/review-logitech-mk270/` | ❌ **HTTP 404** (post não existe; busca na REST API por "logitech" só retorna o 2888) |

### 1.6. Bloco de autor AUSENTE

Não há assinatura nenhuma no artigo — falta o bloco canônico
(foto `cristiano-curadoria-prime.jpg` + bio "Motorista de aplicativo em Uberlândia (MG), 16 mil viagens…" + `https://x.com/CuradoriaPrime`).

### 1.7. "Fontes consultadas" AUSENTE

Nenhuma seção de fontes (§3.4). A única fonte externa linkada no corpo é a página
do MK235 na Logitech. Faltam: página do produto no ML, Amazon, e a consulta Anatel
que sustentaria o nº de homologação.

### 1.8. Instrução interna vazada para o leitor

> *"💡 Dica: Para uma navegação perfeita neste artigo, recomendamos usar o plugin
> 'Table of Contents Plus' no WordPress, que transformará os títulos abaixo em um
> sumário clicável automático."*

Isso é uma nota de produção dirigida ao **editor**, publicada como se fosse dica ao
leitor. Remover (mesma classe do "comentário interno vazado" do 4541).

### 1.9. Dados a verificar antes de republicar

| Dado publicado | Situação |
|---|---|
| Homologação Anatel **nº 210032214394** | ⚠️ **[VERIFICAÇÃO HUMANA NECESSÁRIA]** — número de 12 dígitos atribuído a um produto genérico sem marca; precisa ser conferido no sistema da Anatel ou sai do artigo |
| Sensor "**Pro Elite**" 1.200 DPI | ⚠️ nome comercial do anúncio do ML, não de fabricante identificável — tratar como "informado pelo vendedor" |
| "Garantia: **30 dias** (vendedor)" | conferir no anúncio atual (MLB-4168372465) |
| "Pilhas AAA inclusas como **brinde do vendedor**" | idem — é condição do vendedor, muda sem aviso |
| Preço "~R$ 60–80" | desatualizado na Amazon; capturas de 17/08: **ML R$ 63,99** (cupom) / **Amazon R$ 56,55** (mas ASIN errado — ver 1.2) |
| "Última atualização: **Março 2026**" | o post foi modificado em **14/08/2026** — data visível mente |
| Nota **7,5/10 escritório · 6,0/10 avançado** | nota dupla é confusa; padrão da sessão é uma nota /10 |

### 1.10. Faltantes do padrão editorial da sessão

- ❌ "Pontos de Atenção" com `<h4>` + `<ul>` ≥3 — existe "👎 Contras" com 8 itens (**o título "Contras" é aceito pela §2.7**, mas o padrão dos posts já fechados é "Pontos de Atenção");
- ❌ "para quem NÃO é" explícito — só há um parágrafo difuso no veredito;
- ❌ box de divulgação **antes do primeiro link** (o primeiro link de afiliado aparece muito depois do topo, e a divulgação só surge na seção "Onde Comprar");
- ❌ data de verificação de preço visível junto aos valores.

---

## 2. O que PRESERVAR (regra: nunca reescrever do zero)

- Estrutura de 15 seções e o índice numerado (é bom para a intenção de busca);
- Tabela de especificações técnicas e a tabela comparativa vs MK235;
- Seção "Problemas Comuns" — **o conteúdo é útil**, só precisa perder as aspas falsas;
- Cards de compra com "Escolha do Editor" / "Alternativa", classes e cores do tema;
- FAQ de 4 perguntas (as respostas são corretas);
- Imagens já hospedadas no domínio (`/wp-content/uploads/2026/01/…webp`).

---

## 3. Plano de correção proposto (a executar após aprovação)

1. Baixar o HTML publicado e reescrever **preservando** layout/classes/styles inline.
2. Eliminar as 14 alegações de teste: "Unboxing e Primeiras Impressões" → **"O que vem na caixa (segundo o anúncio e o manual)"**; "nossas impressões" → "o que a ficha técnica e os relatos indicam"; "Testamos em Windows…" → "o fabricante/vendedor declara compatibilidade com…".
3. Inserir o box **"Tipo de análise"** logo abaixo do H1 + box de metodologia.
4. Divulgação de afiliado **antes** do primeiro link.
5. `rel="sponsored noopener noreferrer nofollow"` em 6/6 links.
6. Trocar as 2 buscas genéricas do ML por links de produto reais (**pendência do cliente:** gerar shortlinks para MK235 e MK270) ou remover os botões.
7. Corrigir o link Amazon do produto principal (**pendência do cliente:** o `B0dKNIkQE` leva a um kit PRETO diferente).
8. 5 aspas → "Síntese editorial dos relatos"; "compradores verificados" → "avaliações publicadas por compradores"; nota do ML com data.
9. Preços em **faixa com data** (17/08/2026) nos cards e no aviso.
10. "Contras" → **"Pontos de Atenção"** (h4 + ul, os 8 itens já existem) + parágrafo "para quem NÃO é".
11. Nota única /10 (sugestão: manter 7,5/10 e explicar o critério, movendo o "6,0 para uso avançado" para dentro do texto).
12. JSON-LD reconstruído (parse → mutar → redump) em bloco `<!-- wp:html -->` **sem `<br/>`**: `@graph` = TechArticle + Product (reviewRating 7,5/10 com `worstRating`, **sem `offers`**) + FAQPage + BreadcrumbList (categoria a definir — ver pendência) + autor `Person "Cristiano Martins"`.
13. Remover o auto-link e o link 404 do MK270; adicionar "Veja também" com posts reais.
14. Adicionar **"Fontes consultadas"** + bloco de **autor canônico**.
15. Remover a dica do plugin "Table of Contents Plus".
16. Anatel: confirmar ou remover (não inventar).
17. Validar: `python3 tools/checar_conformidade.py articles/kit-teclado-mouse-ultra-slim.html` → 0 erros / 0 alertas.

---

## 4. Pendências do CLIENTE (bloqueiam a entrega final)

1. 🔴 **Link Amazon do produto principal** (`link.amazon/B0dKNIkQE`) resolve para o **ASIN B0B59YC5N4 — kit PRETO ergonômico**, não o Ultra Slim branco do review. Gerar shortlink correto **ou** decidir remover o botão Amazon (o ML tem o produto certo).
2. 🔴 **Shortlinks de afiliado ML para MK235 e MK270** — hoje são buscas genéricas `?q=`, sem tracking e sem checkout.
3. 🟡 **Homologação Anatel 210032214394** — confirmar; sem confirmação, o número sai do artigo.
4. 🟡 **Post "review-logitech-mk270"** — o link existe no texto mas a página é 404. Criar o post ou remover a menção.
5. 🟡 **Categoria WP do post** — não é nenhuma das já mapeadas (`tv-e-home-theater`, `audio-e-som`, `smartphones-e-wearables`, `tablets`, `destaques`, `reviews`, `casa-inteligente-e-seguranca`). Definir antes de montar o BreadcrumbList.
6. 🟡 **Nota**: manter 7,5/10 como nota única?

---

## 5. Capturas de mercado (17/08/2026)

| Produto | Amazon BR | Mercado Livre |
|---|---|---|
| Kit Ultra Slim (branco, 2.4GHz) | ASIN do link atual está **errado** (B0B59YC5N4 = modelo preto, R$ 56,55) | **MLB-4168372465** (HOME BLESS) — R$ 63,99 com cupom / R$ 64,99 · 3× R$ 21,66 · frete grátis 1ª compra |
| Logitech MK235 | **B07643MPGS** — 4,7/5 · 21.563 avaliações | sem shortlink (só busca) |
| Logitech MK270 | **B074WL3VZF** — R$ 152,93 (referência do próprio anúncio) | sem shortlink (só busca) |

Concorrentes diretos vistos no ML (para a seção de alternativas, se o cliente quiser):
Newdragon Ultra Slim branco R$ 61,98 · Piracomp Super Slim preto R$ 78,99 ·
"Ultra Slim preto" R$ 79,90 (mais vendido).
