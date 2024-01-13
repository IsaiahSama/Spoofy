from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello world</h1>"


@app.route("/auth/")
def auth():
    return "<p>Some nonsense</p>"


if __name__ == "__main__":
    app.run()
