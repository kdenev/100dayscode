from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

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
app.config['SECRET_KEY'] = 'a secret'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

base_dir = os.path.abspath(os.path.dirname(__name__))
database_dir = os.path.join(base_dir, 'day64\\start\\instance') 

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(database_dir, 'movies.db')}"
# initialize the app with the extension
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(Integer, unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)
    ranking: Mapped[float] = mapped_column(Float, unique=False, nullable=False)
    review: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)


    
with app.app_context():
    db.create_all()
    # db.session.add(second_movie)
    # db.session.commit()

class MyForm(FlaskForm):
    rating  = StringField(label='Your Rating Out of 10 e.g 7.5', validators=[DataRequired()])
    review  = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.id))
    all_movies = result.scalars()
    movie_list = all_movies.fetchall()
    return render_template("index.html"
                           , movie_list = movie_list)

@app.route("/edit", methods=['POST', 'GET'])
def edit():

    id = request.args.get('id')
    form = MyForm()

    if form.validate_on_submit():
        form_data = request.form.to_dict()
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update.rating = float(form_data['rating'])
        movie_to_update.review = form_data['review']
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html"
                    , form = form)

@app.route("/delete")
def delete():
    movie_to_delete = db.get_or_404(Movie, request.args.get('del_movie'))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
