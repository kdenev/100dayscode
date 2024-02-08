from flask import Flask
from random import randint

RANDOM_NUMBER = randint(0,9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>Guess a number between 0 and 9</h1>
              <img src= "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">            
    """
@app.route("/<int:i>")
def guess_the_number(i):
    if i > RANDOM_NUMBER:
        return """<h1 style="color:red">You guessed too high!</h1>
                  <img src= "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">            
    """
    elif i < RANDOM_NUMBER:
        return """<h1 style="color:red">You guessed too low!</h1>
                  <img src= "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">            
    """
    else:
        return """<h1 style="color:green">You guessed the number!</h1>
                  <img src= "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">            
    """



if __name__ == "__main__":
    app.run(debug=True, port=5033)