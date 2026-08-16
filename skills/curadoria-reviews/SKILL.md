---
name: curadoria-reviews
description: >
  Coleta avaliações REAIS de compradores (Amazon e Mercado Livre) e monta o
  bloco "O que dizem os compradores" no padrão da Curadoria Prime — sem inventar
  citação, com paridade de plataformas. Use when the user precisa de prova
  social, depoimentos, notas/contagens de avaliação, ou auditar bloco de
  reviews em artigo de review/listicle.
---

# Curadoria Reviews — coleta e bloco de avaliações

Assistente para a etapa mais trabalhosa dos posts de produto: **prova social real**.

Regra de ouro: **nunca inventar citação, nome, data, nota ou contagem** (§4.2).
Aspas só em transcrição fiel. Sem depoimento real para a cota, use "Síntese
editorial dos relatos" (sem aspas, sem nome) — nunca complete com texto plausível.

---

## 1. Onde conseguir avaliações (do mais barato ao mais caro)

### A) Mercado Livre — GRÁTIS, sem login ✅

Endpoint público de catálogo (mesmo usado pela vitrine do ML):

```
https://www.mercadolivre.com.br/noindex/catalog/reviews/<MLB_ID>/search?noindex=true&siteId=MLB&limit=5&offset=0&sort=relevancy
```

- `<MLB_ID>`: o identificador do produto (ex.: `MLB38058572` = Watch7; vem da URL `/p/MLB...`).
- Retorna JSON: `reviews[].comment.content.text`, `reviews[].rating`, `reviews[].date` ("Há X meses"), `country`.
- **Não expõe o nome do autor** (só texto/nota/data) — por isso os cards ML usam "— 5★, set/2025".
- `country != "Brasil"` → marcar "(traduzido)".
- Troque `sort=relevancy` por `sort=time_desc` para tentar avaliações mais recentes.

Script pronto: `tools/reviews_ml.py`.

### B) Amazon — login wall ❌ (o gargalo real)

- A página de avaliações (`/product-reviews/<ASIN>`) exige login. `curl`/fetch simples e até **Playwright** devolvem estrela+data, mas **o texto do review vem vazio** (confirmado nesta sessão).
- **Fluxo mais confiável (grátis):** pedir ao editor que cole a seção "Avaliações de clientes" da página do produto — ele vê tudo logado. Foi assim que fechamos o 4541 com citação verbatim + nome + data + "compra verificada".
- **Se precisar de volume/pagamento:** APIs pagas que contornam o muro —
  - **Apify** "Amazon Reviews Scraper" (US$ 3/1k, no-login, suporta `amazon.com.br`) — devolve rating/título/texto/reviewer/verified/data/país.
  - **ScrapingDog** `/amazon/reviews?asin=...&domain=com.br` · **ScraperAPI** (structured Amazon Reviews) — nota: a própria ScraperAPI declara que o endpoint de reviews está **indisponível** por causa do login; usar o de product page.
- **NUNCA** rodar Playwright na esperança de quebrar o muro da Amazon: não quebra, e consome tempo.

### C) Playwright (para o que renderiza em JS, fora Amazon)

O outro chat deixou o padrão pronto (`scrape-reviews.py`): Chromium headless + antidetecção básica. Útil para páginas que carregam conteúdo via scroll (SPA, listas do ML), mas **inútil contra login obrigatório**.

---

## 2. Padrão do bloco "O que dizem os compradores"

Decidido com o editor (16/08/2026):

1. **Em listicle, o bloco fica DENTRO de cada seção de produto** (depois de "Pontos de Atenção", antes do próximo `<h2>`) — nunca como caixa única agregada no topo (isso é layout de review de produto único).
2. **Paridade de plataformas:** 2 Amazon + 2 Mercado Livre (ou 3+3), sempre em par.
3. **Estrutura do bloco** (grid 2 colunas):

```
🗣️ O que dizem os compradores
[AMAZON · nota (total)]            [MERCADO LIVRE · nota (total)]
 "citação" — Nome, X★ · verif.     "citação" — X★, mês/ano (traduzido?)
 "citação" — Nome, X★ · verif.     "citação" — X★, mês/ano
```

4. **Atribuição:**
   - Amazon: `— Nome, 5★ · compra verificada · 11/jan/2026`.
   - Mercado Livre: `— 5★, set/2025` (sem nome — a API não fornece) + `(traduzido)` quando `country ≠ Brasil`.
5. **Cores:** Amazon = laranja `#FF9900`; Mercado Livre = azul `#3485DB`.
6. **Equilíbrio:** inclua ao menos um comentário com ressalva (contra) — dialoga com os "Pontos de Atenção" e atende ao Google (benefícios E desvantagens).

---

## 3. Notas e contagens (sempre com fonte)

- Amazon: "4,6/5 · 10.037 avaliações globais (84% nota 5)" — copiar da página do produto.
- Mercado Livre: "4,8★ · 1.364 opiniões" — da página ou do JSON do catálogo.
- **Nunca** transformar essas notas em `aggregateRating` no JSON-LD (§2.4).

---

## 4. Lições de layout (evitar retrabalho)

- **`wpautop`** insere `<p>`/`<br>` fantasma em containers `flex`/`grid` quando há quebra de linha no HTML colado. **Não dependa de `gap` nem da contagem de filhos** — use `margin` no próprio elemento (ex.: `margin-right` na `<img>`). Entregar o HTML em `<!-- wp:html -->` (Gutenberg) protege; editor clássico re-injeta.
- **Deslazyficar** imagens copiadas do publicado (promover `data-src` → `src`, remover `data-lazyloaded`/`data-srcset`/`data-sizes`).
- **Checar o termo "testamos"** em citações: o `checar_conformidade.py` pode acusar falso positivo se a palavra aparecer dentro de aspas de comprador ("Testei por uma semana…"). Se acontecer, troque por outra citação equivalente sem o gatilho — sem distorcer texto real.

---

## 5. Validação antes de entregar

```bash
python3 tools/checar_conformidade.py articles/<arquivo>.html   # 0 erros
```
- contar `&#8220;` (aspas) = 4 por produto (2 AMZ + 2 ML) — ou 6 (3+3);
- contar "compra verificada" = nº de citações Amazon;
- `grep -c "Síntese editorial"` = 0 quando há citações reais;
- balanço `<div>`/`<span>` OK.

---

## Referências cruzadas

- Regras editoriais canônicas: `skills/curadoria-review/references/regras-editoriais.md` (§4 avaliações, §2.4 aggregateRating, §2.7 contras).
- Skill irmã: `skills/curadoria-review` (criação/atualização do artigo).
- Tool: `tools/reviews_ml.py` (coleta ML via API).
- Exemplo real aplicado: `articles/presentes-dia-dos-pais-2026-tech-premium-artigo-completo.html` (blocos 2+2 dentro das seções).
