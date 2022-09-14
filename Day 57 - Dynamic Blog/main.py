from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    return f"<a href='blog'>blog</a>"


@app.route("/blog")
def blog():
    all_posts = requests.get("https://api.npoint.io/d40443d6d0fe848f01fa").json()
    return render_template("index.html", all_posts=all_posts)


@app.route("/blog/<int:post_id>")
def post(post_id):
    all_posts = requests.get("https://api.npoint.io/d40443d6d0fe848f01fa").json()

    return render_template("post.html", id=post_id, all_posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
