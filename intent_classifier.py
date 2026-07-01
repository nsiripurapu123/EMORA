def get_intent(text):
    text = text.lower()
    if "joke" in text:
        return "joke"
    elif "recommend" in text:
        return "recommendation"
    else:
        return "chat"