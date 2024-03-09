from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a secret'

base_dir = os.path.abspath(os.path.dirname(__name__))
database_dir = os.path.join(base_dir, 'day68\\instance') 

# LOGIN MANAGER 
login_manager = LoginManager()


# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(database_dir, 'users.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
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
        availability_check = db.session.execute(db.select(User).where(form_data['email'] == User.email)).scalar()
        if availability_check:
            flash("Email already register.")
            return redirect(url_for('login'))
        else:
            new_user = User(
                email = form_data['email']
                , name = form_data['name']
                , password = generate_password_hash(form_data['password'], method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form.to_dict()
        user = db.session.execute(db.select(User).where(form_data['email'] == User.email)).scalar()
        if check_password_hash(user.password, form_data['password']):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Wrong credentials.')
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True, port=5013)
