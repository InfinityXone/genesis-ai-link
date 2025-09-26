import json, datetime, os

LOG_FILE = "logs/conversations.log"

def log_conversation(agent_name, user_message, agent_response):
    timestamp = datetime.datetime.utcnow().isoformat()
    entry = {
        "agent": agent_name,
        "user_message": user_message,
        "agent_response": agent_response,
        "timestamp": timestamp
    }
    os.makedirs("logs", exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"✅ Logged conversation at {timestamp}")
