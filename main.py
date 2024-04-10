from flask import Flask
import random

NUMBER = random.randint(1, 100)

app = Flask(__name__)

@app.route("/")
def hello():
    return (f"<h1>Pick a number from 1 to 100</h1>"
            "<h2>Put in the url /guess, ie http://127.0.0.1:5000/5</h2>")

@app.route("/<int:param>")
def yo(param):
    if param == NUMBER:
        return (f"<h1>YOU GOT IT! The number was {param}</h1>"
                f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>")
    if param > NUMBER:
        return ("<h1>Too High</h1>"
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>")
    elif param < NUMBER:
        return "<h1>Too Low</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"


app.run()