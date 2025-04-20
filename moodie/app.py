from flask import Flask, render_template, request, redirect, url_for, session
from moodie import User, Moodie, MoodInput, ConversationFlow 

app = Flask(__name__)
app.secret_key = "tajny_klic"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username
        return redirect(url_for("chat"))
    return render_template("index.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    username = session.get("username", "kamaráde")
    
    # Načti stav z session
    mood = session.get("mood")
    submood = session.get("submood")
    followup = session.get("followup")

    user = User(username)
    user.mood = mood
    user.submood = submood
    user.followup = followup

    moodie = Moodie(user)
    flow = ConversationFlow()

    if request.method == "POST":
        # Ulož nové odpovědi
        mood_input = MoodInput(request.form)

        # Pokud je zadán mood, uložíme ho
        if mood_input.mood:
            session["mood"] = mood_input.mood
            user.mood = mood_input.mood

        if mood_input.submood:
            session["submood"] = mood_input.submood
            user.submood = mood_input.submood

        if mood_input.followup:
            session["followup"] = mood_input.followup
            user.followup = mood_input.followup

    # Získáme odpověď a další krok
    message = moodie.get_response()
    next_step = flow.determine_next_step(user.mood, user.submood, user.followup)

    return render_template(
        "chat.html",
        username=username,
        message=message,
        mood=user.mood,
        submood=user.submood,
        followup=user.followup,
        next_step=next_step
    )

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)