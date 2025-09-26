#!/usr/bin/env python3
import socket
import json

# === CONFIG ===
SOCKET_PATH = "/tmp/agent_one.sock"
API_KEY = "098dad28f0cca0b17842e37f33d081422d1dbe11dbcbefd9e3c86068500754bb"
COMMAND = "status report"

# === CONNECT TO SOCKET ===
def ping_agent(command):
    try:
        print(f"🧠 Connecting to {SOCKET_PATH}...")
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(SOCKET_PATH)

        request = {
            "api_key": API_KEY,
            "command": command
        }

        sock.send(json.dumps(request).encode())
        response = sock.recv(65536)
        sock.close()

        print("✅ Agent One replied:")
        print(response.decode())

    except Exception as e:
        print("❌ Failed to reach Infinity Agent One.")
        print(f"Error: {e}")

if __name__ == "__main__":
    ping_agent(COMMAND)
