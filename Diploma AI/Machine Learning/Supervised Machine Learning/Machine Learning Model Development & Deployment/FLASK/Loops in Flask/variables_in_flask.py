from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def page():
    return "This is home page"

# we are passing a string variable
@app.route("/<myvar>")
def variable(myvar):
    return f"The variable you enter is {myvar}"

# how to pass integer variable
# glob it the page and after mentioning glob we will mention the number
@app.route("/glob/<int:mynumber>")
def integer_variable(mynumber):
    return f"this is the number you passed {mynumber}"

# to pass float variable
# how to use variables, you have to write url /blog/79.5  79.5 is the float value
@app.route("/blog/<float:mynum>")
def float_variable(mynum):
    return f"this is the number you passed {mynum}"



# VARIABLES WITH  A HTML PAGE
# this function is taking two arguemnts
# when we go on url /homepage/ahsan/90   ahsan is name variable value and 90 is marks variable value
# these trigger the execution of mypage function which renders the webpage and two passed variables name and marks
# and these values are passed in the html coding in webpage.html and we see it on web
# first function is executed and then page is displayed with the values
@app.route("/homepage/<name>/<int:marks>")
def mypage(name,marks):
    return render_template("webpage.html",name=name,marks=marks)





if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")