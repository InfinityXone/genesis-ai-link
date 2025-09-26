#!/bin/bash

# 🌐 Git Auto Sync for Genesis Agent System

cd ~/genesis-ai-link || exit 1

# Add all relevant files
git add agents/ scripts/ logs/ tasks/ *.py

# Commit with timestamp
git commit -m "🧠 AutoPush: Synced at $(date '+%Y-%m-%d %H:%M:%S')" 

# Push to GitHub
git push origin main
