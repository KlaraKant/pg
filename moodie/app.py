from flask import Flask, render_template, request, redirect, url_for, session
from moodie import Moodie
from models import User, MoodInput, ConversationFlow

app = Flask(__name__)
app.secret_key = 'tajny_klic'  # pro session

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        if username:
            session["username"] = username
            session["mood"] = None
            session["submood"] = None
            session["followup"] = None
            return redirect(url_for("chat"))
    return render_template("index.html", greeting=moodie.greet())

@app.route("/chat", methods=["GET", "POST"])
def chat():
    username = session.get("username", "kamaráde")
    mood = session.get("mood")
    submood = session.get("submood")
    followup = session.get("followup")

    user = User(username)
    user.mood = mood
    user.submood = submood
    user.followup = followup

    if request.method == "POST":
        mood_input = MoodInput(request.form)

        if mood_input.mood:
            session["mood"] = mood_input.mood
            user.mood = mood_input.mood

        if mood_input.submood:
            session["submood"] = mood_input.submood
            user.submood = mood_input.submood

        if mood_input.followup:
            session["followup"] = mood_input.followup
            user.followup = mood_input.followup

    flow = ConversationFlow()
    moodie = Moodie(user)

    # Získáme další krok
    next_step = flow.determine_next_step(user.mood, user.submood, user.followup)

    # Získáme zprávu
    if not user.mood and not user.submood and not user.followup:
        message = f"Ahoj {username}, jak se dnes cítíš?"
    else:
        message = moodie.get_response()

    return render_template(
        "chat.html",
        username=username,
        message=message,
        next_step=next_step
    )

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)