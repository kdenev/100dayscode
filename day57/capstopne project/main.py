from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"

@app.route('/')
def home():
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("index.html"
                           , posts=all_posts)

@app.route('/post/<blog_id>')
def read_blog(blog_id):
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("post.html"
                           , posts=all_posts
                           , blog_id=int(blog_id)
                           )

if __name__ == "__main__":
    app.run(debug=True)
