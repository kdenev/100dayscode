from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)
age_api = "https://api.agify.io"
gender_api = "https://api.genderize.io"

@app.route("/")
def hello_world():
    random_number = random.randint(1,10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, year=year)

@app.route("/guess/<name>")
def guess(name):
    params = {
        "name": name.title()
    }
    age_response = requests.get(url=age_api, params=params).json()
    gender_response = requests.get(url=gender_api, params=params).json()
    return render_template('name.html'
                        , name=params['name']
                        , gender=gender_response['gender']
                        , age=age_response['age'])

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True, port=5033)