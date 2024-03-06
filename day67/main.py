from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import os
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

base_dir = os.path.abspath(os.path.dirname(__name__))
database_dir = os.path.join(base_dir, 'day67\\instance') 

ckeditor = CKEditor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a secret'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(database_dir, 'posts.db')}"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

# CONFIGURE FORM
class BlogForm(FlaskForm):
    title = StringField(label="Blog Title", validators=[DataRequired()])
    subtitle = StringField(label="Blog Subtitle", validators=[DataRequired()])
    author = StringField(label="Author", validators=[DataRequired()])
    img_url = StringField(label="Background Image URL", validators=[DataRequired()])
    body = CKEditorField(label="Body", validators=[DataRequired()])

    submit = SubmitField(label="Create New Post")

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/posts/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/add', methods=['POST', 'GET'])
def add():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        data = request.form.to_dict()
        new_blog = BlogPost(
            title = data['title'] # blog_form.title.data
            , subtitle = data['subtitle']
            , author = data['author']
            , img_url = data['img_url']
            , body = data['body']
            , date = datetime.now().date().strftime("%B %d, %Y")
        )
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html"
                           , form = blog_form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    edit_h1 = "Edit Post"
    edit_blog = db.get_or_404(BlogPost, post_id)
    edit_form = BlogForm(
        title = edit_blog.title
        , subtitle = edit_blog.subtitle
        , author = edit_blog.author
        , img_url = edit_blog.img_url
        , body = edit_blog.body
    )
    if edit_form.validate_on_submit():
        edit_blog.title = edit_form.title.data
        edit_blog.subtitle = edit_form.subtitle.data
        edit_blog.author = edit_form.author.data
        edit_blog.img_url = edit_form.img_url.data
        edit_blog.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html'
                    , edit_h1 = edit_h1
                    , form = edit_form)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>", methods=['GET'])
def delete_post(post_id):
    post_to_del = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_del)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)