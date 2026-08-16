# Pesquisa — 4541 (presentes-dia-dos-pais-2026-tech-premium) · 6 meses

Data: 16/08/2026. Objetivo: validar specs + estimar faixa de preço de ~6 meses (fev→ago/2026)
para os 5 produtos, antes da reescrita (filosofia do 4397: guia permanente, sem "Dia dos Pais 2026").

## Faixas de preço (6 meses) — consolidadas

| Produto | Faixa 6m (R$) | Fontes/pontos |
|---|---|---|
| Apple Pencil Pro | **900 – 1.500** (nacional); importado já apareceu a R$ 824 | Amazon list R$ 1.499 (B0D3J71RM7, 4,6★/9.633); ML: nacional R$ 1.045–1.459, importado R$ 824–929 |
| Galaxy Watch7 44mm BT | **1.050 – 1.590** | Amazon R$ 1.399 (B0D96V7WRB, verde); KaBuM R$ 1.259; ML novo R$ 1.019–1.499; Magazine Luiza/Casas Bahia R$ 1.575–1.589; Zoom "média R$ 1.259 / 40 dias"; mixvale (mai/26) "a partir de R$ 1.019" |
| Anker 737 PowerCore 24K | **600 – 1.080** (hoje R$ 600–800) | Lançamento out/25: sugerido R$ 1.079, Amazon R$ 799; hoje ML ~R$ 628,93 (15/08). A1289, 24.000mAh/140W, ANATEL |
| Soundcore Liberty 4 NC | **370 – 450** | Amazon R$ 379,05–408,50–444,50 (B0BZV8HLX3); 15/08 R$ 407,55 |
| JBL Wave Buds 2 | **220 – 290** | Amazon R$ 227,05→242,25→255; ML R$ 234–289 |

> Regra aplicada: onde o preço oficial (lista) é muito acima do praticado, uso a faixa
> **praticada** (mín e máx observados no período), não o preço de tabela.

## Validação de specs

- **Apple Pencil Pro** (MX2D3AM/A, ASIN B0D3J71RM7): compatível iPad Pro M4, iPad Air M2/M3,
  iPad mini A17 Pro. NÃO funciona em iPad 11 (A16)/iPad 10 (usam Pencil USB-C). ✅
- **Galaxy Watch7 44mm BT** (SM-L310, B0D96V7WRB): Super AMOLED 1,5" (480×480), 425mAh (~40h),
  Wear OS Powered by Samsung, BioActive, GPS dupla frequência, 32GB, IP68+5ATM, NFC. ✅
- **Anker 737 PowerCore 24K** (A1289): 24.000mAh (~90Wh, ≤100Wh ANAC), 140W PD3.1,
  2 USB-C + 1 USB-A, display digital, ActiveShield 2.0, homologação ANATEL. ✅
- **Soundcore Liberty 4 NC** (B0BZV8HLX3): ANC adaptativo 98,5%, 50h totais, IPX4, HearID 2.0,
  recarga sem fio. ✅
- **JBL Wave Buds 2** (B0DHL63KWK): ANC + Smart Ambient, 40h totais, IP54 (fones), Fast/Swift Pair. ✅

## ⚠️ Decisões necessárias (antes da reescrita)

1. **"Testamos na bancada" (Watch7) / "Já testamos" (Liberty 4 NC) / "testado por nós" (JBL):**
   o outro chat manteve por "ter review publicada". A REGRA DO CLIENTE (§2.2) só permite
   "testado por nós" com as 8 evidências. **Perguntar: você testou fisicamente esses 3?**
   Se não → substituir por "Analisamos em detalhe". (Filosofia manual que usei nos outros posts.)
2. **"Dia dos Pais 2026" no título/schema:** remover por completo (filosofia do 4397),
   reposicionando como guia permanente de "presentes tech premium".
3. **O pacote PERENE do outro chat NÃO é Gutenberg limpo** (contém `<header>`, `<picture>` do tema,
   lazy-load base64). Vou reescrever do zero em `<!-- wp:html -->`, no padrão dos outros 4 posts.

## Verificação 4537 (feita em paralelo)

- ✅ "Testamos a fundo" → "Analisamos a fundo" CONFIRMADO no ar.
- ✅ `aggregateRating` REMOVIDO do JSON-LD (agora: Article + Review + FAQPage + Breadcrumb).
- ⚠️ Menores (não bloqueiam): `author.url` aponta `/author/cristian/` (slug antigo, minúsculo);
  `offers` com `priceValidUntil: 2026-08-31` (data futura, ok, mas decai); ainda há
  "compradores verificados" (2×) e "compra verificada" no corpo (§4.2) — fora do escopo do outro chat.
