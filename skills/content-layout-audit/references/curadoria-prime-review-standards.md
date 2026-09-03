# Curadoria Prime — Padrão Canônico do Review (Golden Model)

**Fonte canônica: `skills/curadoria-review/assets/modelos/modelo-review-golden.html`.**

Esta régua descreve os marcadores de uma review em alta conversão e autoridade
no curadoriaprime.com. Um auditor deve validar qualquer HTML de review contra
este documento, usando o **src do golden** como referência pixel-perfect.

> ⚠️ **Cada tipo de conteúdo tem seu próprio golden.** Review = `modelo-review-golden.html`.
> Lista = `modelo-lista-golden.html`. VS = `modelo-vs-golden.html`. As paletas divergem
> (ex.: o acento `#5a4fcf/#764ba2` é do **lista**; o review usa `#2997ff`). Audite sempre
> com o golden do tipo correspondente — nunca generalize uma paleta entre tipos.

---

## 1. Identidade visual — tokens (do golden de review)

### Box de transparência / metodologia / nota (âmbar)
```html
background:#fffbeb; border:1px solid #fde68a; color:#78350f;
border-radius:10px; font-size:13.5px; line-height:1.7; padding:16px 20px; margin-bottom:24px;
```
Usado em: "Tipo de análise", "Metodologia deste review", "Transparência", "Como chegamos à nota".
Link dentro do box: `color:#78350f; font-weight:700; text-decoration:underline`.

### Header de impacto (hero)
```html
background:linear-gradient(135deg,#1d1d1f 0%,#000000 100%); color:#fff;
padding:28px 30px; border-radius:14px; margin-bottom:30px; font-size:15.5px; line-height:1.75;
```
- Badge "📌 Review Completo — ano": `background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.28); font-size:11px; font-weight:bold; letter-spacing:.1em; text-transform:uppercase; padding:4px 12px; border-radius:100px`.
- Título com destaque realçado: `<strong style="color:#2997ff;">`.
- Pills de dados (nota Amazon/ML, preço, atualizado): `background:rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.28); padding:6px 14px; border-radius:100px; font-size:13px`. Container: `display:flex; flex-wrap:wrap; gap:10px`.

### Imagem hero
```html
width:100%; max-width:1000px; height:auto; border-radius:12px; display:block; margin:0 auto;
box-shadow:0 4px 16px rgba(0,0,0,.14);
```
Legenda abaixo: `text-align:center; font-size:12px; color:#7c7c9a; margin:8px 0 0`.

### Box de seção ("O que dizem os compradores", "Índice do conteúdo")
```html
background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:20px 24px; margin-bottom:28px;
```
Título: `font-size:16px; font-weight:700; color:#1e293b`.

### Cards de avaliação por loja
- **Amazon:** `background:#fff; border:1px solid #ffd499; border-left:4px solid #FF9900; border-radius:10px` · título `<strong style="color:#FF9900;">`.
- **Mercado Livre:** `background:#fff; border:1px solid #a9cdfa; border-left:4px solid #3485DB; border-radius:10px` · título `<strong style="color:#3485DB;">`.

### Resposta rápida (grid 3×1)
`display:grid; grid-template-columns:repeat(3,1fr); gap:16px; margin-bottom:28px`.
- ✅ Vale a pena: `background:#f0fdf4; border:2px solid #22c55e` · título `color:#166534`.
- 🤔 Depende: `background:#eff6ff; border:2px solid #3b82f6` · título `color:#1e40af`.
- ⏳ Pode esperar: `background:#fffbeb; border:2px solid #f59e0b` · título `color:#92400e`.

### Container "Onde comprar"
```html
background:white; border:1px solid #e9ecef; border-radius:20px; padding:35px 25px;
box-shadow:0 4px 20px rgba(0,0,0,0.05);
```
Cada card de oferta: `border-radius:14px; padding:20px; margin-bottom:18px`.
- **Card "Menor preço"**: `border:2px solid #16a34a`. Badge: `linear-gradient(135deg,#16a34a 0%,#166534 100%); color:white`.
- **Card "Recomendado"**: `border:2px solid #1d1d1f`. Badge: `linear-gradient(135deg,#1d1d1f 0%,#000000 100%); color:white`.
- **Card neutro**: `border:2px solid #e9ecef`. Badge: `background:#f1f5f9; color:#475569`.
- Alerta de transparência dentro do card: `background:#fff7ed; border:1px solid #fed7aa; color:#9a3412`.
- Nome da oferta: `font-weight:bold; color:#1a1f36; font-size:17px`. Detalhe: `color:#888; font-size:14px`.
- Corpo: `font-size:14px; color:#666`.

### CTAs de afiliado (gradientes por loja)
- **Mercado Livre:** `linear-gradient(135deg,#2d3277 0%,#1a1f5c 100%); color:#ffe600; box-shadow:0 2px 8px rgba(45,50,119,0.3)`.
- **Amazon:** `linear-gradient(135deg,#ff9900 0%,#ff8500 100%); color:white; box-shadow:0 2px 8px rgba(255,150,0,0.3)`.
- **Dark (Apple/loja oficial não afiliada):** `linear-gradient(135deg,#1d1d1f 0%,#000000 100%); color:white; box-shadow:0 2px 8px rgba(0,0,0,0.3)`.
- Padrão do botão: `padding:12px 20px; border-radius:8px; font-weight:800; font-size:15px; flex:1; min-width:150px; text-align:center`.

### Tabela "Ficha técnica"
- Container: `overflow-x:auto; margin-bottom:28px`.
- Tabela: `width:100%; border-collapse:separate; border-spacing:0; font-size:14px; background:#fff; border:1px solid #e9ecef; border-radius:14px; overflow:hidden; box-shadow:0 2px 12px rgba(0,0,0,0.04)`.
- Linha de cabeçalho: `background:#1d1d1f; color:#fff`.
- Linhas alternadas: `background:#f8fafc` (ímpar neutro, par listrado).
- Borda de célula: `border-bottom:1px solid #edf2f7`, `padding:12px 14px`.

### Veredito final (scorecard — Régua v2.0)
Container:
```html
border-radius:16px; padding:28px; background:linear-gradient(135deg,#ffffff 0%,#f8fafc 100%);
border:1px solid #e2e8f0; box-shadow:0 2px 8px rgba(15,23,42,0.04);
```
- Cabeçalho: tabela de nota geral à direita em badge:
  `background:linear-gradient(135deg,#0f172a 0%,#1e1b4b 100%); padding:14px 22px; border-radius:12px; box-shadow:0 4px 12px rgba(15,23,42,0.3)`.
  Nota `font-size:36px; font-weight:800; color:#fff`; divisor `height:44px; width:1px; background:rgba(255,255,255,0.3)`.
- Grid de critérios (3×2): `display:grid; grid-template-columns:repeat(3,1fr); gap:16px`.
  Cada card: `background:#fff; border:1px solid #e2e8f0; border-radius:12px; padding:18px; text-align:center`.
  Rótulo: `font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.05em; color:#64748b`.
  Nota: `font-size:36px; font-weight:800` — **Custo-benefício `#f59e0b` (âmbar)**; demais `#22c55e` (verde).
  Sub (justificativa): `font-size:12.5px; color:#475569`.
- Responsivo: em ≤782px `repeat(2,1fr)`; em ≤480px `1fr` e reduzir padding.

### Escolha rápida (CTA final, gradiente dark)
```html
background:linear-gradient(135deg,#1d1d1f 0%,#000000 100%); color:#fff; border-radius:20px;
padding:30px 26px; margin:28px 0; text-align:center;
```
- Subtítulo: `color:#c7c7cc; font-size:14px`.
- CTA primário (vermelho-menor-preço): `linear-gradient(135deg,#16a34a 0%,#166534 100%); color:white; box-shadow:0 2px 10px rgba(22,163,74,.4)`.
- CTA claro (loja oficial): `linear-gradient(135deg,#ffffff 0%,#e5e5ea 100%); color:#1d1d1f; box-shadow:0 2px 10px rgba(255,255,255,.25)`.
- Link em nota: `color:#ffb340`.

---

## 2. Marcadores estruturais (ordem obrigatória numa review)

1. **Box "Tipo de análise"** (transparência: não testamos fisicamente) — âmbar.
2. **Meta descrição SEO** (comentário para Rank Math).
3. **Header de impacto** (badge "Review Completo", título com preço real destacado, pills de nota/preço/data).
4. **Imagem hero** (com legenda centrada).
5. **Box "Metodologia deste review"** (fonte: specs oficiais, fonte primária, avaliações verificadas).
6. **Box "O que dizem os compradores"** (cards por loja).
7. **Box "Índice do conteúdo"** (links de âncora `#...`).
8. **Resposta rápida** (grid 3×1 ✅/🤔/⏳).
9. **Onde comprar** (container de ofertas com CTAs por loja).
10. **Ficha técnica** (tabela dark header).
11. Seções de análise por aspecto.
12. **Veredito final** (scorecard 6 critérios da Régua v2.0).
13. **Box "Como chegamos à nota"** (âmbar — explica os pesos).
14. **Escolha rápida** (CTA final) + **FAQ** + **Fontes consultadas**.

## 3. Requisitos técnicos

- **CMS:** comentários de bloco WordPress (`<!-- wp:html -->`, `<!-- wp:paragraph -->`, `<!-- wp:heading -->`).
- **SEO:** bloco de meta descrição no topo; âncoras `#` apontando para IDs existentes.
- **JSON-LD:** `@graph` com `Article`/`TechArticle` + `FAQPage` + `BreadcrumbList`.
  ⚠️ Nunca emitir `aggregateRating`/`ratingCount`/`reviewCount` de terceiros como se fosse nosso (Régua §2.4).
- **Afiliados:** todo link de loja com `rel="sponsored noopener noreferrer nofollow"`.
- **Autoria:** assinatura é de uma pessoa (Régua §2.6) — `author` como `Person`, nunca `Organization`.
