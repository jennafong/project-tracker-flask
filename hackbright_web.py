"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def greeting():
    greeting = "Hello! This is not the page you are looking for. Go to /student-search."
    return greeting

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    firstname, lastname, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           firstname=firstname,
                           lastname=lastname,
                           github=github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add-form")
def show_student_add_form():
    """Show form for adding a student."""

    return render_template("student_add.html")

@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student."""

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    github = request.form["github"]
    
    hackbright.make_new_student(firstname, lastname, github)

    return render_template("student_add_confirmation.html",
                            firstname=firstname,
                            lastname=lastname,
                            github=github)
    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")
