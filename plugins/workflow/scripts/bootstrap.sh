#!/usr/bin/env bash
# bootstrap.sh — myskills/workflow auto-installer
# spec: specs/auto-install — design.md §4.2
# Fail-soft por bloco: NÃO usa `set -e` global de propósito.
set -uo pipefail

PLUGIN_NAME="workflow"
TAG="[myskills/${PLUGIN_NAME}]"

# Guards: env vars devem vir do Claude Code. Se ausentes, hook foi
# disparado fora de contexto — sai silencioso (FR-7, NFR-3).
: "${CLAUDE_PLUGIN_ROOT:?}" 2>/dev/null || exit 0
: "${CLAUDE_PLUGIN_DATA:?}" 2>/dev/null || exit 0

MANIFEST="${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json"
[ -f "$MANIFEST" ] || exit 0

# Parse "version": "x.y.z" sem jq (FR-3). Funciona em bash 3.2 (macOS).
VERSION="$(sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$MANIFEST" | head -n1)"
VERSION="${VERSION:-unknown}"

MARKER="${CLAUDE_PLUGIN_DATA}/.bootstrapped-v${VERSION}"
LOG="${CLAUDE_PLUGIN_DATA}/bootstrap.log"

# Fast path: marker já existe — no-op silencioso <100ms (FR-4, NFR-1).
[ -f "$MARKER" ] && exit 0

mkdir -p "${CLAUDE_PLUGIN_DATA}"

# Header de execução no log (NFR-5).
{
  echo "===== $(date -u +%Y-%m-%dT%H:%M:%SZ) bootstrap v${VERSION} ====="
} >> "$LOG" 2>&1

echo "${TAG} instalando skills standalone…"

# Cada bloco roda em subshell e captura falha individual sem matar o script.
# Fontes vêm de plugins/workflow/commands/setup.md (FR-8).
FAILED=0

run_step() {
  local label="$1"; shift
  {
    echo "--- ${label} ---"
    "$@"
  } >> "$LOG" 2>&1
  local rc=$?
  if [ $rc -ne 0 ]; then
    echo "[FAIL rc=${rc}] ${label}" >> "$LOG"
    FAILED=1
  fi
}

run_step "GSD bundle" \
  npx -y skills add git@github.com:glittercowboy/get-shit-done.git -y

run_step "find-skills (vercel-labs)" \
  npx -y skills add github:vercel-labs/skills --skill find-skills -y

run_step "1password (openclaw)" \
  npx -y skills add github:openclaw/openclaw --skill 1password -y

if [ "$FAILED" -eq 0 ]; then
  touch "$MARKER"
  echo "${TAG} ok"
else
  echo "${TAG} bootstrap adiado — ver ${LOG}"
fi

exit 0
