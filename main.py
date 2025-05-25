from app.language_selector import select_language
from app.nira_safe import get_name, get_role, get_score_input
from app.gpt_suggestor import gpt_suggest_by_role
from app.file_utils import append_log, display_log
from datetime import datetime

print("\n👋 Welcome to NIRA CLI - All-in-One Assistant")

# 🌐 Step 1: Language Selection
lang, text = select_language()

while True:
    print(f"\n🌐 {text[lang]['menu']}")
    print(f"1. {text[lang]['start']}")
    print(f"2. {text[lang]['view']}")
    print(f"3. {text[lang]['exit']}")
    
    choice = input(f"👉 {text[lang]['choose']} ").strip()

    if choice == "1":
        # 🧑 Name
        name = get_name(lang, text)

        # 💼 Role
        role = get_role(lang, text)

        # 🔮 GPT Suggestion
        suggestion = gpt_suggest_by_role(role)
        print(f"\n🌟 {text[lang]['hello']} {name}, {role.upper()}!")
        print(f"\n📚 Content suggestions:\n{suggestion}")

        # 📈 Score
        score = get_score_input(lang, text)

        print(f"🎯 {text[lang]['motivation']}: {score:.1f}/10")

        # 📝 Log
        append_log(datetime.now(), name, role, score)
        print(f"✅ {text[lang]['saved']}")

    elif choice == "2":
        display_log(lang, text)

    elif choice == "3":
        print(f"👋 {text[lang]['goodbye']}")
        break

    else:
        print(f"❌ {text[lang]['invalid']}")
