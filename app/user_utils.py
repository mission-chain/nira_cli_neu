import os
import json
from datetime import datetime

USER_FOLDER = "data/users"
os.makedirs(USER_FOLDER, exist_ok=True)

def get_user_file(name):
    return os.path.join(USER_FOLDER, f"{name.lower()}.json")

def user_exists(name):
    return os.path.exists(get_user_file(name))

def save_user_profile(profile):
    name = profile.get("name", "").lower()
    if not name:
        raise ValueError("Name is required to save profile.")
    profile["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(get_user_file(name), "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2, ensure_ascii=False)

def load_profile(name):
    with open(get_user_file(name), "r", encoding="utf-8") as f:
        return json.load(f)

def update_profile_field(name, key, value):
    profile = load_profile(name)
    profile[key] = value
    save_user_profile(profile)
    return profile
