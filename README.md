# Ai-skill — Curadoria Prime

Skill editorial para o curadoriaprime.com, alinhada às regras editoriais
(v2.0, 19/08/2026 — fonte canônica: `skills/curadoria-review/references/regras-editoriais.md`).

## Skills

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

## Como usar

```bash
cp -R skills/curadoria-review ~/.claude/skills/curadoria-review
cp -R skills/curadoria-mercado ~/.claude/skills/curadoria-mercado
