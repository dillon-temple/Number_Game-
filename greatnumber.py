from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "bobby"

import random

@app.route('/')
def store_number():
    if 'counter' in session:
        session["counter"] += 1
    else:
        session["counter"] = 1
        session["attempts"] = 0
        session["game_number"] = random.randint(1, 100)
        session["player_number"] = 0

        print(f"The random number is {session['game_number']}!")

    
    return render_template("greatnumber.html")

@app.route('/guess', methods=["POST"])
def guess():
    session["attempts"] += 1
    session["player_number"] = int(request.form["num"])
    return redirect("/")


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
