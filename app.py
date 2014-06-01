import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

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
