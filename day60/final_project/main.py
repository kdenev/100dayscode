from flask import Flask, render_template, request
import requests
import smtplib
from email.message import EmailMessage
import os
import sys

# Import api script
sys.path.append(r"D:\Desktop\code\python\api_key_creator")
import api_key_creator

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

def send_letter(body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Website New Message"
    msg["From"] = os.environ['GMAIL_EMAIL']
    msg["To"] = os.environ['GMAIL_EMAIL']

    try:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=os.environ['GMAIL_EMAIL'], password=os.environ['GMAIL_API_PASS'])
        connection.send_message(msg)
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        change_form = True
        data = request.form
        user_name = data['name']
        user_email = data['email']
        user_phone = data['phone']
        user_message = data['message']
        email_body = f"""
        Name: {user_name}
        Email: {user_email}
        Phone: {user_phone}
        Message: {user_message}
        """
        send_letter(email_body)
        return render_template("contact.html"
                               ,change_form = change_form)
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    data = request.form
    user_name = data['name']
    user_email = data['email']
    user_phone = data['phone']
    user_message = data['message']
    return "<h1>Success!!!</h1>"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
