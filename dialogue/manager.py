def decide(intent, emotion):
    if intent == "joke":
        return "skill:jokes"
    elif intent == "recommendation":
        return "skill:recommend"
    else:
        return "core_chat"
