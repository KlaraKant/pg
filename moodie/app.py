from flask import Flask, render_template, request, redirect, url_for, session
from moodie import Moodie, User, MoodInput, ConversationFlow

app = Flask(__name__)
app.secret_key = 'tajny_klic'

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["mood"] = None
        session["submood"] = None
        session["followup"] = None
        return redirect(url_for("chat"))
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    username = session.get("username", "kamaráde")

    # Načti stav
    user = User(username)
    user.mood = session.get("mood")
    user.submood = session.get("submood")
    user.followup = session.get("followup")

    moodie = Moodie(user)
    flow = ConversationFlow()

    if request.method == "POST":
        mood_input = MoodInput(request.form)

        if mood_input.mood:
            user.mood = mood_input.mood
            session["mood"] = mood_input.mood
        if mood_input.submood:
            user.submood = mood_input.submood
            session["submood"] = mood_input.submood
        if mood_input.followup:
            user.followup = mood_input.followup
            session["followup"] = mood_input.followup

        message = moodie.get_response()
    else:
        # Po přihlášení zobraz jen úvodní zprávu
        message = moodie.greet()

    next_step = flow.determine_next_step(user.mood, user.submood, user.followup)

    return render_template("chat.html",
                           username=username,
                           message=message,
                           mood=user.mood,
                           submood=user.submood,
                           followup=user.followup,
                           next_step=next_step)

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
