def create_script(reflection, emotion):
    intro = "Tonight, let’s take a moment just for you."
    outro = "Breathe gently. Let go. You deserve rest."

    if emotion == "anxiety":
        body = "It’s okay to feel uncertain. Your worries are not your identity."
    elif emotion == "hope":
        body = "There’s a light inside you that even the dark cannot dim."
    elif emotion == "sadness":
        body = "Sadness is a quiet companion. But you are not alone tonight."
    elif emotion == "emotional burnout":
        body = "You’ve carried too much today. Rest is strength, not weakness."
    else:
        body = "Peace comes in small moments. Tonight is one of them."

    return f"{intro}\n\n{body}\n\n{outro}"
