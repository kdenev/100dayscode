from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

base_dir = os.path.abspath(os.path.dirname(__name__))
database_dir = os.path.join(base_dir, 'day67\\instance') 

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(database_dir, 'users.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        new_user = User(
            email = form_data['email']
            , name = form_data['name']
            , password = form_data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('secrets', name = form_data['name']))
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        user = db.session.execute(db.select(User).where(form_data['email'] == User.email)).scalar()
        if user:
            return redirect(url_for('secrets', name = user.name))
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True, port=5033)