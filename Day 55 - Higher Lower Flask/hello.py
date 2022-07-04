from flask import Flask
from random import randint

app = Flask(__name__)

# $env:FLASK_APP = "hello"

# def make_bold(func):
#     def inner():
#         text = func()
#         return "<i>" + text + "</i>"
#     return inner

answer = randint(0, 9)


@app.route("/")
def home_page():
    global answer
    answer = randint(0, 9)
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route("/<int:num>")
def guesses(num):
    global answer

    if num > answer:
        return "<h1 style='color:red;'>Too high</h1>" \
           "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num < answer:
        return "<h1 style='color:purple;'>Too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:green;'>You found me</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>" \
               "<h2>To play again, go to the home page"


if __name__ == "__main__":
    app.run(debug=True)
