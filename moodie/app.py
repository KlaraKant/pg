from flask import Flask, render_template, request, redirect, url_for, session
from models import User, Moodie, MoodInput, ConversationFlow

app = Flask(__name__)
app.secret_key = "tajny_klic"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session.clear()
        return redirect(url_for("chat"))
    moodie = Moodie(None)
    return render_template("index.html", greeting=moodie.greet())

@app.route("/chat", methods=["GET", "POST"])
def chat():
    username = session.get("username", "kamaráde")
    user = User(username)

    user.mood = session.get("mood")
    user.submood = session.get("submood")
    user.followup = session.get("followup")

    moodie = Moodie(user)
    flow = ConversationFlow()

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

        if not mood and not submood and not followup:
            message = f"Ahoj {username}, jak se dnes cítíš?"
        else:
            message = moodie.get_response()
    next_step = flow.determine_next_step(user.mood, user.submood, user.followup)

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
    app.run(debug=True)