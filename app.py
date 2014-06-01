import flask

app = flask.Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route("/test")
def test():
    return flask.render_template("dashboard.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
