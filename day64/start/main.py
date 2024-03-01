from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
from tmdb import TMDBMovie

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

tmdb = TMDBMovie()

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
    year: Mapped[str] = mapped_column(Integer, unique=False, nullable=True)
    description: Mapped[str] = mapped_column(String(), unique=False, nullable=True)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=True)
    ranking: Mapped[float] = mapped_column(Float, unique=False, nullable=True)
    review: Mapped[str] = mapped_column(String(250), unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), unique=False, nullable=True)
    
with app.app_context():
    db.create_all()

class ChangeRating(FlaskForm):
    rating  = StringField(label='Your Rating Out of 10 e.g 7.5', validators=[DataRequired()])
    review  = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')

class AddMovie(FlaskForm):
    title  = StringField(label='Movie Title', validators=[DataRequired()], name="title")
    submit = SubmitField(label='Add Movie')

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating)).all()
    for i in range(len(result)):
        result[i][0].ranking = i+1
    return render_template("index.html"
                            , movie_list = result)

@app.route("/edit", methods=['POST', 'GET'])
def edit():

    id = request.args.get('id')
    edit_form = ChangeRating()

    if edit_form.validate_on_submit():
        form_data = request.form.to_dict()
        movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == id)).scalar()
        movie_to_update.rating = float(form_data['rating'])
        movie_to_update.review = form_data['review']
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html"
                    , form = edit_form)

@app.route("/delete")
def delete():
    movie_to_delete = db.get_or_404(Movie, request.args.get('del_movie'))
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['POST', 'GET'])
def add():
    add_form = AddMovie()
    if request.method == 'POST':
        if add_form.validate_on_submit:
            title = request.form['title']
            if title:
                data = tmdb.fetch_movie_list(title)
                return render_template('select.html'
                                        ,data = data)
    return render_template('add.html'
                           , form = add_form)

@app.route("/add_record")
def add_record():
    response = tmdb.fetch_movie_info(request.args.get('id'))
    movie_info = response.json()
    new_movie = Movie(
        title = request.args.get('title')
        , year = int(request.args.get('year'))
        , description = movie_info['overview']
        , img_url = "https://image.tmdb.org/t/p/w500" + movie_info['poster_path']
        , rating = 0
        , ranking = 0
        , review = ""
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))

# on each anchor tag add the url_for id = movie.id
# create a separate route for the update
# new api url https://developer.themoviedb.org/reference/movie-details
# old api url https://developer.themoviedb.org/reference/search-movie

if __name__ == '__main__':
    app.run(debug=True)
