from flask import Flask

app = Flask(__name__)


@app.route("/something")
def beep():
    return "<h1>Hello there</h1>"


@app.route("/hi")
def boop():
    return "<h1>Hi there</h1>"


if __name__ == "__main__":
    app.run()
