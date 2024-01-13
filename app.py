from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<a href='/beep/'>Beep</a><a href='/bop/'>Bop</a><a href='/boop/'>Boop</a>"


@app.route("/beep/")
def beep():
    return "<h1>Beep</h1>"


@app.route("/bop/")
def bop():
    return "<h1>Bop</h1>"


@app.route("/boop/")
def boop():
    return "<h1>Boop</h1>"


if __name__ == "__main__":
    app.run()
