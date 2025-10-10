from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome_page():
    return render_template("webpage.html")

@app.route("/inherited")
def inherited_page():
    return render_template("inherited.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


