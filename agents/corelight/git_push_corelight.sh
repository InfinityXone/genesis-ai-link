#!/bin/bash
cd ~/genesis-ai-link
mkdir -p agents/corelight
cp /mnt/data/corelight_agent_package/* agents/corelight/
git add agents/corelight/
git commit -m "🚀 Corelight Agent: Persona, Loader, Memory & Cleaner added"
git push
