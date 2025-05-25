def get_name(lang, text):
    return input(f"🧑 {text[lang]['ask_name']} ").strip().title()

def get_role(lang, text):
    while True:
        role = input(f"💼{text[lang]['ask_role']}: ").strip().lower()
        if role in text[lang]['valid_roles']:
            return role
        print(f"❌ {text[lang]['invalid_role']} {' | '.join(r.title() for r in text[lang]['valid_roles'])}")

def get_score_input(lang, text):
    while True:
        score_input = input(f"📈 {text[lang]['ask_score']} ").strip()
        if score_input.replace('.', '', 1).isdigit():
            score = float(score_input)
            if 0 <= score <= 10:
                return score
            else:
                print(f"⚠️ {text[lang]['score_out_of_range']}")
        else:
            print(f"❌ {text[lang]['score_invalid']}")
