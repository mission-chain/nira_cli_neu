# app/nira_chat_gpt.py

def gpt_chat_response(prompt):
    # Dummy GPT response simulator for CLI testing
    response_map = {
        "creator": "🛠️ Let's build something amazing together! Here are some project ideas...",
        "investor": "📊 Here's today's market insight and tools to evaluate opportunities.",
        "learner": "📚 Here's a curated learning path for you to explore."
    }
    role = prompt.lower()
    return response_map.get(role, "🤖 GPT is thinking... (no exact match found)")

