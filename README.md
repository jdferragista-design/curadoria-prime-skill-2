# Ai-skill — Curadoria Prime

Skill editorial para o curadoriaprime.com, alinhada às regras editoriais
(v2.0, 19/08/2026 — fonte canônica: `skills/curadoria-review/references/regras-editoriais.md`).

## Arquitetura de skills — fonte de verdade (repo)

**O repo é a ÚNICA fonte de verdade.** As skills vivem aqui e são propagadas
para o ambiente do agente via script, nunca editadas fora do repo.

| Origem (repo) | Destino (agente) | Script |
| --- | --- | --- |
| `skills/curadoria-prime/` | `~/.hermes/skills/productivity/curadoria-prime/` | `tools/sync_skills.sh` |
| `skills/curadoria-review/` | `~/.claude/skills/curadoria-review/` | `tools/sync_skills.sh` |
| `skills/curadoria-mercado/` | `~/.claude/skills/curadoria-mercado/` | `tools/sync_skills.sh` |
| `skills/curadoria-reach/` | `~/.claude/skills/curadoria-reach/` | `tools/sync_skills.sh` |

```bash
bash tools/sync_skills.sh          # dry-run: mostra o que divergiria
bash tools/sync_skills.sh --apply  # propaga repo -> destinos
```

O script é idempotente (repo sempre vence). **Depois de editar qualquer skill,
rode `--apply`** para o agente consumir a versão nova. Caso contrário haverá
drift (regra que só existe em um dos lados).

## Calendário editorial

- `pauta/calendario-editorial.md` — visão por data de publicação (posts no ar,
  agendados e em planejamento), + regras de canibalização por keyword.
- Fonte viva do estado por URL: `skills/curadoria-review/assets/fila-atualizacao.md`.

## Skills

### `curadoria-prime` (umbrella — orquestração)

- SKILL.md: fluxo editorial, regras de ouro, workflow obrigatório, pitfalls duráveis.
- references/: `checker-pitfalls.md` · `guia-produto-selecao.md` ·
  `imagens-prompts-convencoes.md` · `ledger-add-pitfalls.md` ·
  `schema-e-snippet-convencoes.md` · `seo-snippet-limits.md` ·
  `style-thumbnail-youtube.md`.

### `curadoria-review` (v2.2) — Geração de conteúdo

- Workflow completo: pesquisa → mercado → Régua v2.0 → template → validação
- Régua Curadoria Prime v2.0 (6 critérios: Custo-benefício 30%, Satisfação 25%, Ficha 20%, Recursos 10%, Consenso 10%, Confiança 5%)
- Golden references:
  - REVIEW → `assets/modelos/modelo-review-golden.html` (Apple TV 4K)
  - VS → `assets/modelos/modelo-vs-golden.html` (Lenovo vs Acer)
  - LISTA → `assets/modelos/modelo-lista-golden.html` (Top 5 Fones)
- Templates LOCKED em HTML Gutenberg:
  - `assets/template-review.md`
  - `assets/template-vs.md`
  - `assets/template-lista.md`
- Validação: `assets/checklist-bloqueio.md`
- Fila de prioridade: `assets/fila-atualizacao.md`

### `curadoria-mercado` — Gate de preço e checkout

- Obrigatória antes de qualquer card/CTA/preço
- LEDGER.csv com histórico real de capturas
- Classificação: FICA / FICA COM RESSALVA / SÓ UMA LOJA / FORA / SEM DADO
- Armadilhas de marketplace mapeadas

### `curadoria-reach` — Pesquisa auxiliar (Agent-Reach)

- Consenso técnico via YouTube transcripts (PT-BR)
- Leitura de fichas oficiais via Jina Reader
- RSS para monitoramento de concorrentes
- Venv isolado: `source ~/.agent-reach-venv/bin/activate`
- **NÃO cobre Amazon/ML** — apenas pesquisa auxiliar

## Como usar

```bash
# 1. Editar a skill no repo (única fonte de verdade).
# 2. Propagar para o agente:
bash tools/sync_skills.sh --apply
```
