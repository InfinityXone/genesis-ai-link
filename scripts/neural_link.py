#!/usr/bin/env python3
import time, json, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_DIR = ROOT / "tasks"
COMPLETED_DIR = TASK_DIR / "completed"
LOG_DIR = ROOT / "logs"
APPROVAL_DIR = TASK_DIR / "approvals"
PROPOSAL_DIR = TASK_DIR / "proposals"
for d in (COMPLETED_DIR, LOG_DIR, APPROVAL_DIR, PROPOSAL_DIR): d.mkdir(parents=True, exist_ok=True)

def log(agent, msg):
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    with (LOG_DIR / f"{agent}.log").open("a") as f:
        f.write(f"{now} {msg}\\n")
    print(f"[{agent}] {msg}")

def parse_task(path):
    with open(path) as f:
        try: return yaml.safe_load(f)
        except: return {"raw": f.read()}

def request_approval(task_id, detail):
    proposal = PROPOSAL_DIR / f"{task_id}.proposal.json"
    proposal.write_text(json.dumps({"task_id": task_id, "detail": detail}, indent=2))
    log("orchestrator", f"Proposal created for {task_id}")
    approval = APPROVAL_DIR / f"{task_id}.approved"
    for i in range(10):
        if approval.exists():
            log("orchestrator", f"Approval found for {task_id}")
            return True
        time.sleep(1)
    return False

def simulate_agent(agent, task):
    log(agent, f"Processing {task.get('id')}")
    if task.get("sensitive") or task.get("human_approval_required"):
        if not request_approval(task["id"], {"agent": agent}): return {"status": "blocked"}
    time.sleep(0.5)
    log(agent, "Simulated execution complete.")
    return {"status": "simulated"}

def main():
    for task_file in sorted(TASK_DIR.glob("*.task")):
        task = parse_task(task_file)
        if not task: continue
        agent = "compute_harvester" if task["type"] == "data_processing" else "generic_agent"
        result = simulate_agent(agent, task)
        task_file.rename(COMPLETED_DIR / task_file.name)
        log("orchestrator", f"Task {task['id']} completed with status: {result['status']}")

if __name__ == "__main__":
    main()
