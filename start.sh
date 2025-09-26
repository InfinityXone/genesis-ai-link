#!/usr/bin/env bash
set -euo pipefail
ENV="dev"
DRY_RUN=false
FORCE_HUMAN=false
while [[ $# -gt 0 ]]; do
  case "$1" in
    --env) ENV="$2"; shift 2;;
    --dry-run) DRY_RUN=true; shift ;;
    --force-human-approve) FORCE_HUMAN=true; shift ;;
    *) echo "Unknown arg $1"; exit 1 ;;
  esac
done
echo "🌐 ENV=$ENV DRY_RUN=$DRY_RUN HUMAN=$FORCE_HUMAN"
if [[ "$DRY_RUN" == "true" ]]; then
  echo "[DRY RUN] Starting orchestrator..."
  python3 scripts/neural_link.py --mode orchestrator --env "$ENV" --dry-run
  exit 0
fi
python3 scripts/neural_link.py --mode orchestrator --env "$ENV"
