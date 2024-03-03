from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import os 
from random import randint

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record

base_dir = os.path.abspath(os.path.dirname(__name__))
database_dir = os.path.join(base_dir, 'day66\\start\\instance') 

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(database_dir, 'cafes.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=['GET'])
def random():
    max_num = db.session.query(Cafe.id).count()
    cafe = db.get_or_404(Cafe, randint(1, max_num))
    cafe_info = dict(list(cafe.__dict__.items())[1:])
    return jsonify(cafe = cafe_info)

@app.route("/all", methods=['GET'])
def all():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars()
    cafe_info = [dict(list(cafe.__dict__.items())[1:]) for cafe in cafes]
    return jsonify(cafes = cafe_info)

@app.route("/search", methods=['GET'])
def search():
    location = request.args.get('loc')
    result = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars()
    error_message = {"Not Found":"Sorrym we don't have a cafe at that location."}
    if result.fetchmany(1):
        cafe_info = [dict(list(cafe.__dict__.items())[1:]) for cafe in result]
        return jsonify(cafe = cafe_info)
    else:
        return jsonify(error = error_message)


if __name__ == '__main__':
    app.run(debug=True)
