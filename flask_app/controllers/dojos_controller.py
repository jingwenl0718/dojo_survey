from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo_model import Dojo

# DISPLAY SURVEY FORM
@app.route("/")
def display_survey():
    return render_template("index.html")

# CREATE A NEW DOJO
# the action route
@app.route("/process", methods=["POST"])
def process_data():
    if not Dojo.validate(request.form):
        return redirect('/')
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/result")

@app.route("/result")
def show_result():
    return render_template("result.html")