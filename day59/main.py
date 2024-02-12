from flask import Flask, render_template
import requests

blog_posts_url = "https://api.npoint.io/b10f4fe1f3fecef396db"
response = requests.get(blog_posts_url)
data = response.json()

app = Flask(__name__)

@app.route("/")
def index():
    global data
    return render_template('index.html'
                           , data=data)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/post/<num>")
def post(num):
    global data
    return render_template('post.html'
                           , num=int(num)
                           , data=data)

if __name__ == "__main__":
    app.run(debug=True, port=5033)