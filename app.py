import flask
from classes import csv_reader


app = flask.Flask(__name__)

csv_files = {
    "users" : "csv_files/users.csv",
    "goals" : "csv_files/goals.csv"
    }

@app.route('/')
def hello():
    return csv_reader.login(csv_files["users"], "crazcalm", "pass1234")

@app.route("/dashboard")
def dashboard():
    return flask.render_template("dashboard.html")

@app.route("/dashboardPopup")
def dashboardPopUp():
    return flask.render_template("dashboardPopUp.html")

@app.route("/login")
def login():
    return flask.render_template("splash.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
