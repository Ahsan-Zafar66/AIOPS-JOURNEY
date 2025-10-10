from flask import Flask, render_template


app = Flask(__name__)

@app.route("/myloop")
def forloop():
    data = {"math":100,"data science":75,"Deep learning":30}
    return render_template("for_loop.html",data=data)




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")