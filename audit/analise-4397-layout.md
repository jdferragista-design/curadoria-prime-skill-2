# Análise detalhada (pré-correção) — presentes-dia-dos-pais-tech-ate-300

**Tipo:** guia sazonal/listicle (7 presentes tech até R$ 300)
**URL:** https://curadoriaprime.com/presentes-dia-dos-pais-tech-ate-300/
**Título (H1):** Dia dos Pais 2026: 7 Presentes Tech até R$ 300
**Título SEO (meta):** "Título SEO: Dia dos Pais 2026: 7 Presentes Tech até R$ 300"
**Publicado:** 27/07/2026 · **Modificado:** 02/08/2026
**Paleta:** azul royal `#0076ff` (chips/badges/CTA de ML), verde `#22c55e` (callouts), âmbar (atenção), cinza `#f5f5fb`.

---

## ⚠️ 0. Contexto sazonal (o problema dominante)

**O Dia dos Pais 2026 foi 09/08. Hoje é 14/08 — a data já passou.**
O artigo inteiro fala no presente: "Dia dos Pais 2026", "presente para o Dia dos Pais",
"encontrado a partir de R$ 98,99". É exatamente o caso da §17.3 (guia sazonal com ano
no título): ao fim da temporada, decidir explicitamente entre **consolidar em URL
permanente**, **manter com aviso de contexto histórico**, ou **301**.

Atenção: **4541** (`presentes-dia-dos-pais-2026-tech-premium`) é outro guia do MESMO
evento — possível canibalização de intenção entre os dois.

---

## 1. Layout — arquitetura de blocos (top-down)

| # | Bloco | Tratamento | Conteúdo |
|---|---|---|---|
| 1 | Hero | gradient azul, badge "🎁 Guia de Presentes — Dia dos Pais 2026" | parágrafo + 3 chips (💰 a partir de R$ 98,99 · 🎧 categorias · ⚠️ preços podem mudar) |
| 2 | Imagem hero | `<img>` full | **`Gemini_Generated_Image_2zz2vr2zz2vr2zz2.webp` (IA!)** |
| 3 | Aviso sobre preços | box 📌 | explica variação de preço entre vendedores |
| 4 | Índice | lista de 9 âncoras | TOC |
| 5 | Intro | h2 + 3 parágrafos | apresenta 3 categorias (smartband/fone/power bank) |
| 6 | Transparência | box 📣 | divulgação de afiliado |
| 7 | h2 Smartbands | 2 cards de produto | Band 10 + Fit3 |
| 8 | h2 Fones | 4 cards | QCY + JBL + Redmi + Edifier |
| 9 | h2 Power bank | 1 card | Power Bank 20000mAh |
| 10 | Comparativo | tabela 5 colunas | 7 linhas |
| 11 | Por que varia? | `<ul>` 7 itens | cupons, vendedor, frete, estoque, cor, pagamento, reputação |
| 12 | Para cada tipo de pai | 5 boxes h3 | ✅ saúde · 🎧 música · 💻 pc · 💰 econômico · 🔋 bateria |
| 13 | FAQ | 6 cards | perguntas |
| 14 | Veredito | h2 + bullets → | decisão por perfil |
| 15 | Fontes | h4 + `<ul>` 6 itens | "Fontes e critérios considerados" |
| 16 | JSON-LD | 1 `<script>` @graph | ItemList + FAQPage |

### Estrutura de CADA card de produto (7 cards)

1. Badge ("🏆 MAIS COMPLETO", "📱 ECOSSISTEMA SAMSUNG", "🏆 MELHOR CUSTO-BENEFÍCIO COM ANC", "🔊 SOM JBL", "💸 MAIS BARATO", "🎧 OVER-EAR COM ANC", "🔋 BATERIA EXTRA") + **"N. Nome: faixa de preço"**
2. Imagem do produto + alt
3. 2–3 parágrafos (apresentação, menor preço, explicação da variação)
4. Callout verde "Vale a pena quando:" / "Melhor para:"
5. **2 botões**: "🔥 Ver na Amazon" + "🛒 Ver no Mercado Livre"
6. Link "📖 Ler review completo →"

---

## 2. Blocos de links de afiliado (foco)

**7 cards × 2 botões = 14 botões** (mas com 2 bugs).

| # | Produto | Amazon | Mercado Livre |
|---|---|---|---|
| 1 | Xiaomi Smart Band 10 | ❌ **ausente** | `meli.la/33vwRuh` (×2 — bug) |
| 2 | Samsung Galaxy Fit3 | `link.amazon/B05Uwnj8q` | `meli.la/2s1mWYW` |
| 3 | QCY T13 ANC | `link.amazon/B0b7hBdj6` | `mercadolivre.com/sec/223qhqp` |
| 4 | JBL Wave Buds 2 | `link.amazon/B0fl4XLa3` | `mercadolivre.com/sec/1Ezyrug` |
| 5 | Redmi Buds 6 Play | `link.amazon/B06aJfuhA` | `mercadolivre.com/sec/1U1WzWs` |
| 6 | Edifier W820NB | `link.amazon/B0buAeyna` | `meli.la/2gDAGge` |
| 7 | Power Bank 20000mAh | `link.amazon/B08vvzZ98` | `meli.la/1xXDJ4x` |

**Bugs/inconsistências:**
1. **Band 10**: os 2 botões ("🔥 Ver oferta" e "🛒 Comparar preço") apontam para o MESMO `meli.la/33vwRuh`, e **não há botão Amazon**.
2. **Mesmo produto, shortlinks diferentes entre artigos** (tracking inconsistente):
   - QCY Amazon: aqui `link.amazon/B0b7hBdj6` vs no guia 3336 `amzn.to/4pTnAPy`
   - Fit3 Amazon: aqui `link.amazon/B05Uwnj8q` vs no review 3809 `link.amazon/B0dY6J5t4`
3. `rel`: não capturável via fetch (precisa byte-a-byte); a auditoria de 13/08 não listou o 4397 entre os com sponsored ausente.

---

## 3. Outros elementos visuais

- **Tabelas:** 1 comparativa (7 linhas × 5 colunas).
- **Imagens:** 8 — 1 hero (**gerada por IA/Gemini**) + 7 de produto. Duas com nome de origem estranha: `Corpo-metalico-premium-...webp` (Band 10) e `Gemini_Generated...webp` (hero).
- **Badges:** 🏆/📱/🔊/💸/🎧/🔋 + "MAIS COMPLETO", "ECOSSISTEMA SAMSUNG", "MELHOR CUSTO-BENEFÍCIO COM ANC", "SOM JBL", "MAIS BARATO", "OVER-EAR COM ANC", "BATERIA EXTRA".
- **Caixas de cor:** azul = hero/CTA ML; verde = "vale a pena quando"; âmbar = atenção; não há caixa vermelha de contras.
- **CTA com urgência:** botões "🔥 Ver …" (fogo = urgência) em 7 cards.
- **Sem bloco de autor** (nenhum box de autor no corpo).
- **Sem box "metodologia/não testamos fisicamente".**

---

## 4. Problemas de conformidade (consolidado)

| # | Problema | Regra | Gravidade |
|---|---|---|---|
| 1 | **Sazonal vencido**: Dia dos Pais 2026 já passou; framing inteiro no presente | §17.3 / §9.4 | 🔴 decisão estrutural |
| 2 | **Preço sem data de verificação** (nenhum "verificado em X" no texto) | §2.5 / §17.1 | 🔴 |
| 3 | **Sem autor visível** (sem bloco de autor) | E-E-A-T "Quem" | 🔴 |
| 4 | **Sem declaração de método** ("não testamos fisicamente") | §2.1 / §15 | 🟠 |
| 5 | **Sem "Pontos de Atenção/Contras"** por produto (heading exato + `<ul>` ≥3) | §2.7 | 🔴 |
| 6 | **Imagem hero gerada por IA** (Gemini) sem legenda | §10 / regra 15 | 🟠 |
| 7 | **Premissa "até R$ 300" esticada**: Band 10 até R$ 489, Fit3 até R$ 599, Redmi até R$ 299 — o H1 promete "até R$ 300" mas vários passam | §9.2 (título honesto) | 🟠 |
| 8 | **Urgência falsa leve**: botões "🔥" | §8 | 🟡 |
| 9 | Schema **sem autor, sem datas** (só ItemList + FAQPage) | §7.3/E-E-A-T | 🟠 |
| 10 | Band 10 sem botão Amazon + botão duplicado | layout | 🟡 |

**O que está OK:** divulgação de afiliado presente ✓ · sem "testamos" ✓ · sem "compra verificada" ✓ ·
schema SEM aggregateRating ✓ · preços como FAIXA (não valor fixo) ✓ · aviso "preços podem mudar" ✓ ·
comparativo + FAQ + "por que varia" ✓.

---

## 5. Preços — hoje (14/08) vs. guia (01/08)

Já verificados hoje (das sessões anteriores): QCY **R$ 199** (ML Pix) ✓ dentro da faixa ·
JBL **R$ 255** (Amazon) ✓ dentro · Redmi **R$ 78,05** (ML azul) 🔻 *abaixo* do guia ("a partir de R$ 98,99") ·
**Edifier R$ 355,49–422,90** 🔺 *acima* do guia (que dizia R$ 272–300 — anúncio barato esgotou).
Faltam verificar hoje: Xiaomi Smart Band 10 e Power Bank 20000mAh.

---

## 6. Decisões necessárias (antes de reescrever)

1. **Sazonal** — o que fazer com o guia? (a) reposicionar para "presentes tech até R$ 300" permanente, tirando o "Dia dos Pais 2026" do framing e do título; (b) manter com aviso "guia sazonal — temporada 2026 encerrada"; (c) 301/arquivar. **E a relação com o 4541** (outro guia do mesmo evento)?
2. **Autor** — adicionar o bloco canônico (o artigo não tem)?
3. **Contras** — posso redigir 3+ "Pontos de Atenção" verificáveis por produto (especificação/limitação objetiva), no padrão que usei nos outros?
4. **Preços** — confirmo que devo re-verificar hoje os 7 (já tenho 4; faltam Band 10 e Power Bank) antes de gravar valores?
5. **Premissa "até R$ 300"** — ajusto o título/intro para refletir a realidade (faixa real R$ 78–599)?
