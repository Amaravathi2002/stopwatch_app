from flask import Flask, render_template, redirect, request, session
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/", methods=["GET", "POST"])
def index():
    if "start_time" not in session:
        session["start_time"] = None
        session["elapsed"] = 0

    if request.method == "POST":
        if request.form.get("action") == "Start":
            if not session["start_time"]:
                session["start_time"] = time.time()
        elif request.form.get("action") == "Stop":
            if session["start_time"]:
                session["elapsed"] += time.time() - session["start_time"]
                session["start_time"] = None
        elif request.form.get("action") == "Reset":
            session["start_time"] = None
            session["elapsed"] = 0

    elapsed = session["elapsed"]
    if session["start_time"]:
        elapsed += time.time() - session["start_time"]

    hrs = int(elapsed) // 3600
    mins = (int(elapsed) % 3600) // 60
    secs = int(elapsed) % 60
    formatted_time = f"{hrs:02}:{mins:02}:{secs:02}"

    return render_template("index.html", time=formatted_time)

if __name__ == "__main__":
    app.run(debug=True)
