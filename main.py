from flask import Flask, render_template, url_for
import requests

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


app.run(debug=True)
