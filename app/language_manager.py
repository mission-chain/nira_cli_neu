import json
import os

DEFAULT_LANG = "en"
LANG_FILE = "data/lang_texts.json"

class LanguageManager:
    def __init__(self, lang=DEFAULT_LANG):
        self.lang = lang
        self.text = self._load_texts()

    def _load_texts(self):
        if not os.path.exists(LANG_FILE):
            raise FileNotFoundError(f"Language file '{LANG_FILE}' not found.")
        with open(LANG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def set_language(self, lang):
        lang = lang.lower()
        if lang in self.text:
            self.lang = lang
        else:
            print(f"⚠️ Language '{lang}' not found. Using default: {DEFAULT_LANG}")
            self.lang = DEFAULT_LANG

    def get(self, key):
        return self.text.get(self.lang, {}).get(key, f"[Missing:{key}]")

    def available_languages(self):
        return list(self.text.keys())
