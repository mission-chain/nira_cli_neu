# app/gpt_suggestor.py

def gpt_suggest_by_role(role):
    """
    Trả về gợi ý nội dung phù hợp dựa trên vai trò người dùng.

    Args:
        role (str): Vai trò người dùng ('creator', 'investor', 'learner')

    Returns:
        str: Gợi ý nội dung phù hợp.
    """
    role = role.lower()

    suggestions = {
        "creator": "- ✨ Creative tools and project templates\n"
                   "- 🎨 Content generation and branding ideas",
        "investor": "- 📊 Tokenomics, Launchpads, DAO rewards\n"
                    "- 📈 Market growth analysis",
        "learner": "- 📚 Learn Python, AI, and Web3 step-by-step\n"
                   "- 🤖 Build with Mission Chain tools"
    }

    return suggestions.get(role, "- 🧭 Let’s explore your path together.")
