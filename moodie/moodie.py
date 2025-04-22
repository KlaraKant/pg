# moodie.py

class User:
    def __init__(self, name):
        self.name = name
        self.mood = None
        self.submood = None
        self.followup = None

class MoodRecommendation:
    def get_recommendation(self, mood, submood=None, followup=None):
        if mood == "happy":
            return "Paráda! Jsem rád, že se cítíš skvěle! Udělej pro sebe dnes něco hezkého."

        if mood == "neutral":
            if submood == "yes":
                return "Pokud máš energii, zkus si zacvičit, nebo se pořádně protáhnout. V těle se vyplaví hormony štěstí a zvedne ti to náladu!"
            elif submood == "no":
                return "V pořádku. Kdybys cokoli potřeboval/a, jsem tady pro Tebe!"
            else:
                return "Mohu udělat něco pro to, aby ses cítil/a lépe?"

        if mood == "sad":
            if submood == "yes":
                if followup == "calm":
                    return "Zkus si přečíst knížku, pustit si svůj oblíbený film, nebo se jen zaposlouchat do tvé oblíbené muziky. To by ti mohlo pomoci k lepší náladě!"
                elif followup == "active":
                    return "Být Tebou, zacvičil bych si, nebo si alespoň dál jógu. Pokud máš prostor, zajdi i na procházku, příroda léčí!"
                else:
                    return "A máš náladu spíš na něco pohodového, nebo energičtějšího?"
            elif submood == "no":
                return "V pořádku. Kdyby cokoli, jsem tu vždy pro Tebe!"
            else:
                return "Mrzí mě, že se takto cítíš. Máš náladu s tím něco dělat?"

        return "Něco se pokazilo, zkus to prosím znovu."

class MoodInput:
    def __init__(self, form_data):
        self.mood = form_data.get("mood")
        self.submood = form_data.get("submood")
        self.followup = form_data.get("followup")

class ConversationFlow:
    def determine_next_step(self, mood, submood, followup):
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

class Moodie:
    def __init__(self, user):
        self.user = user

    def get_response(self):
        if not self.user.mood:
            return "Ahoj, jak se dnes cítíš?"
        if self.user.mood == "happy":
            return "To je skvělé! Uděláš dnes něco, co tě baví?"
        if self.user.mood == "neutral":
            if not self.user.submood:
                return "Máš chuť si popovídat nebo nechat být?"
            if self.user.submood == "yes":
                return "Jsem tu pro tebe! Co tě dnes potěšilo?"
            else:
                return "Rozumím, někdy je fajn jen tak být. 🍃"
        if self.user.mood == "sad":
            if not self.user.submood:
                return "Mrzí mě, že se necítíš dobře. Chceš si o tom promluvit?"
            if self.user.submood == "yes":
                if not self.user.followup:
                    return "Jaký druh konverzace by ti teď pomohl – klidný nebo aktivní?"
                else:
                    return "Jsem tady pro tebe. 💙"
            else:
                return "Rozumím. Kdybys změnil/a názor, jsem tu."
        return "Něco se pokazilo, zkus to prosím znovu."