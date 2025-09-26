#!/usr/bin/env python3
"""
sync_to_mnt_data.py — Sync GPT file state to /mnt/data/genesis-sync
Supports bi-directional mirroring for .task, .log, .approved, .proposal files.
"""

import os
import shutil
from pathlib import Path
import time

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYNC_ROOT = Path("/mnt/data/genesis-sync")

# Map local subdirs to shared sync paths
MAPPINGS = {
    "tasks": SYNC_ROOT / "tasks",
    "logs": SYNC_ROOT / "logs",
    "tasks/approvals": SYNC_ROOT / "approvals",
    "tasks/proposals": SYNC_ROOT / "proposals"
}

def ensure_dirs():
    for src, dst in MAPPINGS.items():
        (PROJECT_ROOT / src).mkdir(parents=True, exist_ok=True)
        dst.mkdir(parents=True, exist_ok=True)

def sync_dir(src_dir, dst_dir):
    for item in src_dir.glob("*"):
        dst_item = dst_dir / item.name
        if item.is_file() and not dst_item.exists():
            shutil.copy2(item, dst_item)
        elif item.is_file() and item.stat().st_mtime > dst_item.stat().st_mtime:
            shutil.copy2(item, dst_item)

def sync_reverse(dst_dir, src_dir):
    for item in dst_dir.glob("*"):
        src_item = src_dir / item.name
        if item.is_file() and not src_item.exists():
            shutil.copy2(item, src_item)
        elif item.is_file() and item.stat().st_mtime > src_item.stat().st_mtime:
            shutil.copy2(item, src_item)

def full_sync():
    for src_sub, dst in MAPPINGS.items():
        src = PROJECT_ROOT / src_sub
        sync_dir(src, dst)
        sync_reverse(dst, src)

def loop(interval=5):
    print(f"🔁 Starting GPT sync loop between {PROJECT_ROOT} ⇄ {SYNC_ROOT}")
    while True:
        try:
            full_sync()
        except Exception as e:
            print(f"[sync error] {e}")
        time.sleep(interval)

if __name__ == "__main__":
    ensure_dirs()
    loop()
