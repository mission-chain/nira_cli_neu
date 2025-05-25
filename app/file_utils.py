import os
from datetime import datetime
from tabulate import tabulate

LOG_FILE = "data/user_log.csv"

def append_log(timestamp, name, role, score):
    os.makedirs("data", exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}, {name}, {role}, {score}\n")

def display_log(lang="en", text=None):
    if not os.path.exists(LOG_FILE):
        print(text[lang]["lognotfound"] if text else "Log file not found.")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("📭 " + (text[lang].get("log_empty") if text else "Log file is empty."))
        return

    headers = [
        text[lang].get("col_timestamp", "Timestamp"),
        text[lang].get("col_name", "Name"),
        text[lang].get("col_role", "Role"),
        text[lang].get("col_score", "Score")
    ]

    data = []
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 4:
            timestamp, name, role, score = map(str.strip, parts)
            data.append([timestamp, name, role, int(float(score))])

    print(f"\n🧾 {text[lang].get('userlog', 'User Log') if text else 'User Log'}")
    print(tabulate(data, headers=headers, tablefmt="grid"))
