from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    email  = StringField(label='Email', validators=[DataRequired(), Email()])
    password  = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "a secret"
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print(form.email.data, form.password.data)
            if form.email.data == "admin@email.com" and form.password.data == "12345678":
                return render_template('success.html')
            else:
                return render_template('denied.html')
            
    return render_template('login.html'
                           , form = form)


if __name__ == '__main__':
    app.run(debug=True)
