'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)

with app.app_context():
    db.create_all()

book_list = list()

@app.route('/', methods=['POST', 'GET'])
def home():
    global book_list
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars()
    book_list = all_books.fetchall()
    return render_template('index.html'
                           , books = book_list)


@app.route("/add", methods=['POST', 'GET'])
def add():
    global book_list
    if request.method == 'POST':
        book_info = request.form.to_dict()
        print(book_info)
        print(1 if len(book_list) == 0 else book_list[-1].id + 1, book_info['name'], book_info['author'], book_info['rating'])
        new_book = Book(
            id = 1 if len(book_list) == 0 else book_list[-1].id + 1
            , title = book_info['name']
            , author = book_info['author']
            , rating = book_info['rating']
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/edit/<id>", methods = ['POST', 'GET'])
def edit(id):
    if request.method == "POST":
        result = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        result.rating = float(request.form['rating'])
        result = db.session.execute(db.select(Book).order_by(Book.id))
        db.session.commit()
        return redirect(url_for('home'))
    result = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    return render_template('edit.html'
                           , title = result.title
                           , rating = result.rating
                           , id = id)

if __name__ == "__main__":
    app.run(debug=True)

