def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "I'm glad you're happy!"
    elif mood == "sad":
        return "I'm sorry you're sad."
    elif mood == "excited":
        return "I'm glad to hear you're excited!"
    elif mood == "angry":
        return "I'm sorry you're angry."
    elif mood == "confused":
        return "I'm sorry you're confused."
    else:
        return "I'm sorry, I don't understand that mood."