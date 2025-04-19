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
    user = User(username)
    moodie = Moodie(user)
    flow = ConversationFlow()

    if request.method == "POST":
        mood_input = MoodInput(request.form)
        user.mood = mood_input.mood
        user.submood = mood_input.submood
        user.followup = mood_input.followup

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

    greeting = moodie.greet()
    return render_template("chat.html", username=username, message=greeting, next_step="mood")

if __name__ == "__main__":
    app.run(debug=True)