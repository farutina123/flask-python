from flask import render_template, request, redirect, url_for
from HTML_in_flask.app import app
from datetime import datetime

def date(value, format="%H:%M %d-%m-%y"):
    return value.strftime(format)

app.jinja_env.filters["date"] = date

@app.route("/")
def home():
    current_date = datetime.now()
    return render_template("index.html", current_date=current_date)

@app.route("/about")
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'}
    ]
    return render_template("about.html", team_members=team_members)


@app.route("/contact")
def contact():
    manager = {
        'name': 'Alice',
        'phone': '8-920-497-91-66',
        'address': {
            'street': '123 Main St',
            'city': 'Wonderland',
            'index': '249405'
        }
    }
    return render_template("contact.html", manager=manager)

@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        return render_template("contact.html", message='Your message has been sent successfully!')
    else:
        return redirect(url_for("contact"))