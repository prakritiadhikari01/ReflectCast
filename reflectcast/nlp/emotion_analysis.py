def analyze_emotion(text):
    # Simple keyword-based demo
    if "anxious" in text or "worried" in text:
        return "anxiety"
    elif "tired" in text or "burned out" in text:
        return "emotional burnout"
    elif "grateful" in text or "hopeful" in text:
        return "hope"
    elif "sad" in text or "lonely" in text:
        return "sadness"
    else:
        return "peace"
