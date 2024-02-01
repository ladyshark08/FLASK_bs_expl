from flask import Flask, render_template, url_for, request
import requests
import smtplib
import os

app = Flask(__name__)

API_URL = "https://api.npoint.io/fec9dce85d355bdc9d52"


@app.route('/')
def home():
    response = requests.get(API_URL).json()
    return render_template("index.html", blog_posts=response)
    # return render_template("index.html")


@app.route("/post/<int:num>")
def get_blog(num):
    response = requests.get(API_URL).json()[num - 1]
    return render_template("post.html", message=response)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/form_entry', methods=['post'])
def receive_data():
    my_email = "m43217438@gmail.com"
    password = os.environ.get("PASSWORD")
    email = request.form.get("email")
    name = request.form.get("name")
    phone = request.form.get("phone")
    message = request.form.get("message")
    with smtplib.SMTP("smtp.gmail.com", port=587) as new_connect:
        new_connect.starttls()
        new_connect.login(user=my_email, password=password)
        new_connect.sendmail(from_addr=my_email, to_addrs=my_email,
                             msg=f"Subject:New Message\n\nHello\n\nName:{name}\nPhone:{phone}\nEMail:{email}\nMessage:{message}")

    return render_template("success.html")


app.run(debug=True)
