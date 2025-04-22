class User:
    def __init__(self, name):
        self.name = name
        self.mood = None
        self.submood = None
        self.followup = None


class MoodInput:
    def __init__(self, form):
        self.mood = form.get("mood")
        self.submood = form.get("submood")
        self.followup = form.get("followup")


class ConversationFlow:
    def determine_next_step(self, mood, submood, followup):
        if not mood:
            return "mood"
        if mood == "neutral" and not submood:
            return "neutral_options"
        if mood == "neutral" and submood:
            return None
        if mood == "sad" and not submood:
            return "sad_options"
        if mood == "sad" and submood == "yes" and not followup:
            return "sad_followup"
        if mood == "sad" and (submood == "no" or followup):
            return None
        return None