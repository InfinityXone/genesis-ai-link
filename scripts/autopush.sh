#!/bin/bash

REPO_DIR="$HOME/genesis-ai-link"
cd $REPO_DIR || { echo "Repo directory not found."; exit 1; }

git add .
git commit -m "🤖 [AutoPush] Hourly sync at $(date '+%Y-%m-%d %H:%M:%S')" || echo "Nothing to commit"
git push origin main
