# work functions
# Dario Androsevic
# October 10 2025
def create_mood_message(name, mood="neutral"):
    if mood == "happy":
        return f"Hey {name}. great to see you smiling"
    elif mood == "sad":
        return f"I hope you feel better {name}"
    elif mood == "neutral":
        return f"Sometimes you have average days, {name}"
    else:
        return f"Hi {name}, hope you are having a good day."
