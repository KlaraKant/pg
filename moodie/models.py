# models.py

class Person:
    def __init__(self, name):
        self.name = name

class User(Person):
    def __init__(self, name):
        super().__init__(name)
        self.mood = None
        self.submood = None
        self.followup = None

class MoodInput:
    def __init__(self, form_data):
        self.mood = form_data.get("mood")
        self.submood = form_data.get("submood")
        self.followup = form_data.get("followup")

class Moodie:
    def __init__(self, user):
        self.user = user

    def greet(self):
        return "Ahoj! Já jsem Moodie, tvůj průvodce psychickou pohodou. Jak se jmenuješ ty?"

    def get_response(self):
        mood = self.user.mood
        sub = self.user.submood
        fol = self.user.followup

        if mood == "happy":
            return "Paráda! Jsem rád, že se cítíš skvěle! Udělej pro sebe dnes něco hezkého."
        elif mood == "neutral":
            if not sub:
                return "Mohu udělat něco pro to, aby ses cítil/a lépe?"
            return "V pořádku. Kdybys cokoli potřeboval/a, jsem tady pro Tebe!"
        elif mood == "sad":
            if not sub:
                return "Mrzí mě, že se takto cítíš. Máš náladu s tím něco dělat?"
            if sub == "yes" and not fol:
                return "A máš náladu spíš na něco pohodového, nebo energičtějšího?"
            if fol == "calm":
                return "Zkus si přečíst knížku, pustit si oblíbený film nebo se zaposlouchat do hudby."
            if fol == "active":
                return "Být tebou, zacvičil bych si nebo zašel na procházku. Příroda léčí!"
            return "V pořádku. Kdyby cokoli, jsem tu vždy pro Tebe!"
        return "Něco se pokazilo, zkus to prosím znovu."

class ConversationFlow:
    def determine_next_step(self, mood, submood, followup):
        if not mood:
            return "mood"
        if mood == "neutral" and not submood:
            return "neutral_options"
        if mood == "sad" and not submood:
            return "sad_options"
        if mood == "sad" and submood == "yes" and not followup:
            return "sad_followup"
        return None