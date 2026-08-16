# 🔀 Cruzamento dos dois chats — Curadoria Prime (16/08/2026)

Objetivo: saber exatamente o que **cada chat** já entregou, onde houve **duplicação**
e o que **realmente sobrou** da fila. Para a gente nunca mais refazer trabalho pronto.

---

## 1. Quem fez o quê

### Chat A — ESTA sessão (branch `arena/01a0028f-curadoria-prime-skill-2`)

| ID | Slug | Produto | Resultado |
|---|---|---|---|
| 3181 | `lg-au801-50-review` | LG AU801 50″ | ✅ reescrito + validado |
| 3809 | `samsung-galaxy-fit3-vale-a-pena` | Galaxy Fit3 | ✅ reescrito + validado |
| 3336 | `melhor-fone-bluetooth-ate-500-reais-2026` | Top 5 fones ≤ R$ 500 | ✅ reescrito + validado |
| 4397 | `presentes-dia-dos-pais-tech-ate-300` | 7 presentes ≤ R$ 300 | ✅ reposicionado (sazonal→permanente) |
| 4541 | `presentes-dia-dos-pais-2026-tech-premium` | 5 presentes premium | ✅ reposicionado + reviews 2+2 |

### Chat B — outro chat (workspace-1.zip / `main` / outro ambiente)

| ID | Slug | Produto | Resultado |
|---|---|---|---|
| 4537 | `apple-tv-4k` | Apple TV 4K | ✅ publicado (0 erros — conferido no ar) |
| 3523 | `qcy-t13-anc-review-2026-vale-a-pena` | QCY T13 ANC | ✅ publicado (mod 16/08 09:41) |
| 3002 | `lg-55au801-review-2026` | LG 55AU801 | ✅ publicado (mod 15/08 21:26) |
| 3014 | `purificador-de-agua-electrolux-pe12g-review` | Purificador PE12G | 🟡 schema reconstruído — **falta colar** |
| — | plugin `curadoria-conformidade` (WP) | ferramenta de conformidade | 🛠️ pronto (fora do meu escopo) |
| — | `corrigir_artigos-v3-SCHEMA.py` | lote de schema | 🛠️ pronto (não está no repo atual) |

### IDs que o Chat B citou mas NÃO resolvem no site público

`4846 · 4675 · 4683 · 4709` → a WP API retorna **404** para eles. São rascunhos
(status draft), outro ambiente, ou já deletados. **Não contar como "feito no ar"**
até confirmar com o editor.

---

## 2. Duplicações (trabalho feito 2×) — sem conflito

| Item | Chat A (eu) | Chat B (outro) | Conclusão |
|---|---|---|---|
| **3181** | reescrevi o artigo INTEIRO (com JSON-LD válido) | fez só o `schema-manual/3181-COLAR-NO-WP.html` | **vale o meu** (já inclui o schema) |
| **4541** | reescrevi inteiro (filosofia 4397: sem "Dia dos Pais") | pacote "PERENE" (mantinha "Dia dos Pais 2026" no título) | **vale o meu** (decisão do editor) |

> Lição: o Chat B deixou o `STATUS-FINAL` de cada post — **sempre conferir** antes de
> assumir que um ID está na fila. O 3523 e o 3002 estavam na minha fila mental mas já
> tinham sido fechados pelo outro chat.

---

## 3. A fila REAL que sobrou

### A) Lote de schema (29 posts) — **24 restantes**

Originais: 4414, 4541, 4474, 4456, 4254, 4251, 4185, 4159, 4155, 3871, 3858,
3924, 3835, 3809, 3336, 3548, 3550, 3523, 3320, 3310, 3250, 3169, 3126, 2982,
3002, 2954, 2935, 2921, 2905.

Já resolvidos: **4541 · 3809 · 3336** (eu) + **3523 · 3002** (Chat B).
→ **Restam:** 4414, 4474, 4456, 4254, 4251, 4185, 4159, 4155, 3871, 3858, 3924,
3835, 3548, 3550, 3320, 3310, 3250, 3169, 3126, 2982, 2954, 2935, 2921, 2905.

> ⚠️ **4474** é a duplicata de **4476** (mesmo guia "tablets volta às aulas").
> Antes de mexer no schema, decidir a **consolidação/301** (ver audit/README.md).

> ⚠️ O lote tem solução **mecânica**: `corrigir_artigos-v3-SCHEMA.py` (Chat B) faz
> `_limpar_rating` + `AUTOR_CANONICO`. Trazer esse script para o repo e rodar em lote
> é mais rápido que reescrever 24 posts à mão. **Reescrever manualmente só onde há
> alegação de teste ou outro problema além do schema.**

### B) Alegações de teste (18 artigos / 36 trechos + 2 em meta)

Piores 3 (já feitos): **3523 (7) · 3002 (6) · 4541 (4)** ✅.
→ **Restam ~15 artigos** (≈19 trechos + 2 meta). Destaques: **2943** (2 em meta
description — "teste de isolamento 24h+ com gelo"), **2982**, **3545**, **2892**,
**2888**, **3320**, **3310**, **4251**, **4185**, **3550**, **3527**, **3153**,
**3139**, **3183**, **3052**, **3033**, **4435**.

### C) Consolidar duplicata — **4474 ↔ 4476**

`tablets-para-volta-as-aulas-2026-2` (4474, mod 02/08) vs
`tablets-para-volta-as-aulas-2026` (4476, mod 14/08). 301 de um para o outro.
(Sugestão do próprio repo: 4474 → 4476.)

### D) Pendências do painel (fora dos arquivos HTML)

1. **Campo Título / Rank Math** — remover "Dia dos Pais 2026" e aspa reta:
   - 4397: "Dia dos Pais 2026: 7 Presentes Tech até R$ 300" → **"7 Presentes Tech até R$ 300 em 2026"**
   - 4541: "Dia dos Pais 2026: 5 Presentes Tech Premium" → **"5 Presentes Tech Premium em 2026"**
   - 3181: aspa reta de polegada → "50 polegadas" no título SEO.
2. **Perfil WP:** nome de exibição → **"Cristiano Martins"** (era "Cristiano").
3. **Fuso horário:** ✅ já corrigido (usuário confirmou).
4. **3014:** colar o schema reconstruído (Chat B deixou `3014-COLAR-NO-WP.html`).
5. **Deletar repo "Contex"** do GitHub (backup já feito).
6. **Assunto estrutural (depois da fila):** preço fixo apodrece — discutir shortcode/campo dinâmico.

---

## 4. Próximo recomendado

1. **4474/4476** — decidir a consolidação (duplicata = canibalização ativa).
2. **Lote de schema mecânico** — trazer `corrigir_artigos-v3-SCHEMA.py` e rodar em lote (24 posts), com `--dry-run` primeiro e conferência pós (`grep -c aggregateRating` = 0).
3. **Alegações de teste** — os ~15 restantes, um a um (rewrite manual onde houver alegação).

> Regra de ouro reafirmada: **antes de qualquer ID, conferir `audit/` + o que o
> outro chat deixou em `correcoes/`** — o cruzamento acima evita refazer o 3523/3002/4541/3181.
