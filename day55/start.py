from flask import Flask


def make_bold(function):
    def wrapper(*args, **kwargs):
        output = function()
        return f"<b>{output}</b>"
    return wrapper

def make_empahsis(function):
    def wrapper(*args, **kwargs):
        output = function()
        return f"<em>{output}</em>"
    return wrapper

def make_underline(function):
    def wrapper(*args, **kwargs):
        output = function()
        return f"<u>{output}</u>"
    return wrapper


app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h1>Hello World!</h1>"


@app.route("/bye")
@make_bold
@make_empahsis
@make_underline
def bye():
    return "Bye!"

@app.route("/username/<name>/<num>")
def greet(name, num):
    return f"Hello {name}{num}!"

if __name__ == "__main__":
    app.run(debug=True, port=5033)