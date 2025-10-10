from flask import Flask, render_template


app = Flask(__name__)

@app.get("/myweb")
def first_page():
    return render_template("myweb.html")

# when i will go for /about page it will run about_data function
# when i click on about in page, in that button html i have linked the button with FUNCTION about_data
# so when you click on about button about_data function will be executed
# the other two buttons are not linked with function, they are linked with url, when you click on contact,
# it goes to /contact page which then runs the function linked with /contact page
# GOOD PRACTICE: It is to link buttons with functions using {{url_for(function)}}. 
# for example "{{url_for(about_data)}}" in href of about button
# About page route
@app.route("/about")
def about_data():
    return "<h1>About Flask</h1><p>Flask is a micro web framework written in Python.</p>"

# Contact page route
@app.route("/contact")
def contact():
    return "<h1>Contact Us</h1><p>Contact us at info@flaskdevops.com.</p>"

@app.route("/details")
def my_details():
    return "I am ahsan and I am learning flask"

@app.route("/movies_info")
def movies_data():
    return render_template("movies.html")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")