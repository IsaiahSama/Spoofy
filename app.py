from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/auth/")
def auth():
    return "<p>Some nonsense</p>"


if __name__ == "__main__":
    app.run(debug=True)
