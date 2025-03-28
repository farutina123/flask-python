from flask import render_template, request, redirect, url_for
from HTML_in_flask.app import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        return render_template("contact.html", message='Your message has been sent successfully!')
    else:
        return redirect(url_for("contact"))