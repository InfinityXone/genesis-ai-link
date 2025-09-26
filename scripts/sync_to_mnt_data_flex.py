#!/usr/bin/env python3
"""
sync_to_mnt_data_flex.py — Smart Sync for Genesis Agent System
Automatically syncs all important folders and files between your local genesis-ai-link repo
and the /mnt/data/genesis-sync/ mount. Creates folders as needed.
"""

import os
import shutil
import time
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SYNC_ROOT = Path("/mnt/data/genesis-sync")

INCLUDE_EXTS = {'.task', '.log', '.py', '.json', '.txt'}
INCLUDE_FOLDERS = {'agents', 'logs', 'plans', 'data', 'scripts', 'sandbox', 'queue', 'outbox'}

def ensure_dirs():
    for folder in INCLUDE_FOLDERS:
        (PROJECT_ROOT / folder).mkdir(parents=True, exist_ok=True)
        (SYNC_ROOT / folder).mkdir(parents=True, exist_ok=True)

def sync_dir(src_dir, dst_dir):
    for item in src_dir.glob("*"):
        if item.is_file() and item.suffix in INCLUDE_EXTS:
            dst_item = dst_dir / item.name
            if not dst_item.exists() or item.stat().st_mtime > dst_item.stat().st_mtime:
                shutil.copy2(item, dst_item)

def sync_reverse(dst_dir, src_dir):
    for item in dst_dir.glob("*"):
        if item.is_file() and item.suffix in INCLUDE_EXTS:
            src_item = src_dir / item.name
            if not src_item.exists() or item.stat().st_mtime > src_item.stat().st_mtime:
                shutil.copy2(item, src_item)

def full_sync():
    for folder in INCLUDE_FOLDERS:
        src = PROJECT_ROOT / folder
        dst = SYNC_ROOT / folder
        sync_dir(src, dst)
        sync_reverse(dst, src)

def loop(interval=5):
    print(f"🔁 Smart Sync running: {PROJECT_ROOT} ⇄ {SYNC_ROOT}")
    while True:
        try:
            full_sync()
        except Exception as e:
            print(f"[sync error] {e}")
        time.sleep(interval)

if __name__ == "__main__":
    ensure_dirs()
    loop()
