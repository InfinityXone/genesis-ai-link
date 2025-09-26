import os, time, datetime

LOG_DIRS = ["logs", "tasks/completed"]
MAX_AGE_DAYS = 3

def clean_old_files():
    now = datetime.datetime.now()
    for folder in LOG_DIRS:
        if not os.path.exists(folder):
            continue
        for root, dirs, files in os.walk(folder):
            for name in files:
                file_path = os.path.join(root, name)
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                if (now - file_time).days > MAX_AGE_DAYS:
                    os.remove(file_path)
                    print(f"🧹 Deleted old file: {file_path}")

if __name__ == "__main__":
    while True:
        clean_old_files()
        time.sleep(3600)
