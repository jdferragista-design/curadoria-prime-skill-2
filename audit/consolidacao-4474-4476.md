# Consolidação 4474 ↔ 4476 — tablets volta às aulas

**Status:** 🟡 60% pronto — a canônica já foi corrigida e publicada; falta o retarget do `-2` + 301.

---

## 1. O que são os dois posts

| ID | Slug | Conteúdo | Situação |
|---|---|---|---|
| **4476** | `tablets-para-volta-as-aulas-2026` | **Canônica** — 3 tablets (S10 FE, iPad 11 A16, A11+) + custo da caneta | ✅ corrigida e **publicada** (12/08) |
| **4474** | `tablets-para-volta-as-aulas-2026-2` | **Canibal** — 7 tablets, mesmo título/alvo | ⏳ ainda no ar com a versão antiga (02/08) |

Ambos disputam a MESMA consulta ("tablet para volta às aulas 2026"). Canibalização ativa.

---

## 2. Decisão do editor (12/08/2026) — NÃO é um 301 simples

> **Retarget**, não 301 para a canônica:
> - `-2` → novo slug **`/alternativas-galaxy-tab-s10-fe-ipad-estudar/`** (2 SKUs que não estão na canônica: Idea Tab + Xiaomi Pad 7).
> - **301** de `/tablets-para-volta-as-aulas-2026-2/` → o slug novo (nunca para a canônica).
> - Recíproco: uma linha "alternativas" na canônica, depois do slug novo no ar.

> ⚠️ O `audit/README.md` do repo ainda diz "301 do 4474 para o 4476" — **está desatualizado**.
> A decisão acima (12/08, no `articles/alternativas-...md`) a substitui.

---

## 3. O que JÁ está pronto

| Item | Arquivo | Estado |
|---|---|---|
| Canônica corrigida (3 tablets) | `articles/tablets-para-volta-as-aulas-2026.html` | ✅ publicada no ar (mod 14/08 01:57) |
| Diagnóstico + artigo da canônica | `articles/tablets-para-volta-as-aulas-2026.md` | ✅ |
| Artigo "alternativas" (2 SKUs) | `articles/alternativas-galaxy-tab-s10-fe-ipad-estudar.html` | ✅ pronto + checker 0 erros — **NÃO publicado** |
| Diagnóstico/plano do alternativas | `articles/alternativas-galaxy-tab-s10-fe-ipad-estudar.md` | ✅ |

Validação local (16/08): os dois HTML passam no `checar_conformidade.py` (0 erros).

---

## 4. O que FALTA (ações humanas — exigem painel WP)

### A) Criar o post novo
1. WP → Posts → **Adicionar novo**.
2. Título: **"Alternativas ao Galaxy Tab S10 FE e ao iPad para estudar"**.
3. Slug: **`alternativas-galaxy-tab-s10-fe-ipad-estudar`**.
4. Editor de código → colar `articles/alternativas-galaxy-tab-s10-fe-ipad-estudar.html`.
5. Publicar.

### B) 301 do canibal
Depois do post novo **no ar** (nunca antes):
- Rank Math → Redirecionamentos → Adicionar novo:
  - **Origem:** `/tablets-para-volta-as-aulas-2026-2/`
  - **Destino:** `/alternativas-galaxy-tab-s10-fe-ipad-estudar/`
  - **Tipo:** 301 Permanent
- (Alternativa: plugin Redirection, mesmo par.)

### C) Recíproco na canônica
No post 4476, seção "📚 Leia também", adicionar:

```html
<li><a href="https://curadoriaprime.com/alternativas-galaxy-tab-s10-fe-ipad-estudar/" rel="noopener">Alternativas ao Galaxy Tab S10 FE e ao iPad para estudar</a></li>
```

### D) Corrigir link quebrado na canônica (feito no arquivo local; conferir no ar)
- ❌ `https://curadoriaprime.com/slug-presentes-dia-dos-pais-tech-ate-300/` (placeholder)
- ✅ `https://curadoriaprime.com/presentes-dia-dos-pais-tech-ate-300/`
- Já corrigi no `articles/tablets-para-volta-as-aulas-2026.html` e atualizei o rótulo para "7 Presentes Tech até R$ 300 (guia permanente)". **No site, trocar o link manualmente** (o HTML publicado carrega o mesmo placeholder).

### E) Pendências editoriais do artigo "alternativas" (do `.md`)
- [ ] Conferir foto `lenovo-tab-p12-…` = SKU ZAFR0856BR.
- [ ] S9 FE+ e iPad 10 saíram da indicação (hero já diz "2 alternativas") — confirmar se quer mesmo deixar de fora.
- [ ] Confirmar se Xiaomi Brasil lista o Pad 7 (ficha fora de mi.com/br na captura).

### F) Opcional — despublicar o canibal
Com o 301 ativo, o `-2` para de receber tráfego. Pode deixar publicado (o 301 cuida) ou passar para rascunho. Recomendo **deixar publicado** (histórico + o 301 faz o trabalho).

---

## 5. Por que NÃO reescrevi nada agora

- A canônica (4476) **já está corrigida e publicada** — nada a reescrever.
- O artigo "alternativas" (substituto do 4474) **já está pronto e validado** localmente.
- O que resta é **publicação + 301 + recíproco** — ações de painel que exigem credencial de WP, não edição de conteúdo.

Única alteração de conteúdo que fiz: o link quebrado `slug-presentes…` na canônica local.
