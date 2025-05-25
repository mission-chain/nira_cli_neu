import json

LANG_FILE = "data/lang_texts.json"

def select_language():
    languages = {
        "1": ("en", "🇺🇸 English"),
        "2": ("fr", "🇫🇷 Français"),
        "3": ("es", "🇪🇸 Español"),
        "4": ("jp", "🇯🇵 日本語"),
        "5": ("kr", "🇰🇷 한국어"),
        "6": ("vi", "🇻🇳 Tiếng Việt")
    }

    print("\n🌐 Choose your language:")
    for key, (code, label) in languages.items():
        print(f"{key}. {label}")

    while True:
        choice = input("👉 Type 1-6: ").strip()
        if choice in languages:
            lang = languages[choice][0]
            break
        print("❌ Invalid choice. Please enter a number from 1 to 6.")

    with open(LANG_FILE, "r", encoding="utf-8") as f:
        text = json.load(f)

    return lang, text
