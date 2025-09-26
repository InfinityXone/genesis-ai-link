#!/bin/bash

# 📁 Go to your local repo
cd ~/genesis-ai-link || { echo "❌ Folder not found"; exit 1; }

# 🧠 Add all changes (tracked + untracked)
git add .

# 📝 Commit with a timestamped message
git commit -m "🚀 AutoPush: Full local sync before nuke - $(date '+%Y-%m-%d %H:%M:%S')"

# ⬆️ Push to origin main
git push origin main

echo "✅ Local changes pushed to GitHub"
