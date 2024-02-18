# import sqlite3

# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# cursor.execute("""CREATE TABLE books 
#                (id INTEGER PRIMARY KEY
#                , title varchar(250) NOT NULL UNIQUE
#                , author varchar(250) NOT NULL
#                , rating FLOAT NOT NULL)""")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=False, nullable=False)

book = Book(
   id = 1
   , title = "asd"
   , author = "sddas"
   , rating = 5.4
)

with app.app_context():
    db.create_all()
    db.session.add(book)
    db.session.commit()