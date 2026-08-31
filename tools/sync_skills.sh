#!/usr/bin/env bash
# sync_skills.sh — propaga skills do repo (fonte de verdade) para o ambiente do agente.
#
# Por que existe: o repo ~/Documentos/skill site curadoria./curadoria-prime-skill-2/
# e o SKILL.md canonicos. O agente Hermes consome skills a partir de
# ~/.hermes/skills/ (curadoria-prime) e ~/.claude/skills/ (curadoria-review etc.).
# Sem este script, as duas cópias podem divergir (drift = regra que só existe
# num lugar). Este script torna o repo a UNICA fonte e espelha pro agente.
#
# Uso:
#   bash tools/sync_skills.sh            # dry-run: mostra o que mudaria
#   bash tools/sync_skills.sh --apply    # copia repo -> destinos
#
# Regra: repo SEMPRE vence (fonte de verdade). Nao ha sync reverso.

set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
HERMES="$HOME/.hermes/skills"
CLAUDE="$HOME/.claude/skills"

APPLY=0
for a in "$@"; do
  case "$a" in
    --apply) APPLY=1 ;;
    *) echo "opcao desconhecida: $a"; exit 2 ;;
  esac
done

# (origem do repo, destino no agente)
DIRS=(
  "skills/curadoria-prime     $HERMES/productivity/curadoria-prime"
  "skills/curadoria-review    $CLAUDE/curadoria-review"
  "skills/curadoria-mercado   $CLAUDE/curadoria-mercado"
  "skills/curadoria-reach     $CLAUDE/curadoria-reach"
)

MODE="DRY-RUN"
[ "$APPLY" -eq 1 ] && MODE="APPLY"
echo "== sync_skills ($MODE) | repo=$REPO =="

sync_one() {
  local src="$REPO/$1" dst="$2" rel="$1"
  if [ ! -d "$src" ]; then
    echo "  [skip] $rel  (origem nao existe no repo)"
    return
  fi
  if [ ! -d "$dst" ]; then
    if [ "$APPLY" -eq 1 ]; then
      mkdir -p "$dst"
      cp -R "$src/." "$dst/"
      echo "  [+novas] $rel -> $dst"
    else
      echo "  [~criar] $rel -> $dst"
    fi
    return
  fi
  # compara conteudo; reporta arquivos que divergem
  local diffs
  diffs="$(diff -rq "$src" "$dst" || true)"
  if [ -z "$diffs" ]; then
    echo "  [ok] $rel  (identico)"
  else
    if [ "$APPLY" -eq 1 ]; then
      cp -R "$src/." "$dst/"
      echo "  [atualizado] $rel"
      # mostra o que mudou (limitado) para auditoria
      diff -rq "$src" "$dst" | head -20 || true
    else
      echo "  [DIVERGE] $rel — rodar com --apply para propagar:"
      echo "$diffs" | sed 's/^/      /' | head -30
    fi
  fi
}

for d in "${DIRS[@]}"; do
  read -r src dst <<< "$d"
  sync_one "$src" "$dst"
done

echo
if [ "$APPLY" -eq 1 ]; then
  echo "Feito. As skills do repo foram propagadas aos destinos do agente."
else
  echo "Nada foi alterado (dry-run). Use --apply para propagar a fonte de verdade."
fi
