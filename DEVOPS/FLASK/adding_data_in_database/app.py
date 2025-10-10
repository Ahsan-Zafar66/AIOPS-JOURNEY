from flask import Flask,render_template,request
from flask_mysqldb import MySQL
from datetime import *
import time as t

# starting the main function
app = Flask(__name__)

# giving the ip address of server where mysql database is hosted
app.config['MYSQL_HOST'] = "192.168.43.26"

# telling the user throguh which we will login
app.config['MYSQL_USER'] = "root"

# giving the user password
app.config['MYSQL_PASSWORD'] = "AhsanHacker?1133?"

# telling the name of database to use, table will be defined in query not here
app.config['MYSQL_DB'] = "alnafi"

# gving the app as an input in MYSQL
mysql = MySQL(app)




# content of homepage
home_page = "Welcome to database home page"

# associating the homepage function with the main function
@app.get("/home")
def homepage():
    return home_page

# associating the my_template function with main app function, when we run /trainer,
# it will execute the my_template function, as I have loaded an html page in this function, you will see it
@app.get("/trainer") 
def my_template():
    return render_template("trainer_details.html")

# I added this trainer_Create function in actions of form tag in html page which is trainer_details.html
# when the form will be filled and submit button is pressed trainer_create function will be executed
# as trainer_create function is mentioned in actions of form tag.
@app.route("/trainer_create",methods=["POST","GET"]) 
def trainer_create():
    if request.method == "POST":

        # look for name of fields, such as <input type="number" id="t_id" name="t_id" required><br><br>
        # capture name which is t_id
        
        
        # as we filled the form and press submit button, we are fetching what was written in the form in html page
        # then after fetching the information inputed in html page, we store them variables
        # after storing them in variables we put them in our query that save the data which was writeen in form to database
        t_id = request.form["t_id"]
        # fetching fname
        fname = request.form["fname"]
        lname = request.form["lname"]
        designation = request.form["designation"]
        username = request.form["username"]
        password = request.form["password"]
        salary = request.form["salary"]
        join_date = request.form["join_date"]
        email = request.form["email"]

        # mysql query
        sql_query = "INSERT INTO trainer_detail (fname,lname,designation,username,password,salary,join_date,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        
        # values extracted from form which was written in form and submit button was pressed
        values = (fname,lname,designation,username,password,salary,join_date,email)

        # establishing the connection with mysql database
        cursor = mysql.connection.cursor()

        # executing query
        cursor.execute(sql_query,values)

        # commiting change in mysql
        mysql.connection.commit()

        # closing connection
        cursor.close()

        return "Data Has been added succesfully"


# function to fetch and display all trainer data
# when we will go in page /display_data, the function display_data will be executed as it is linked with it
@app.route("/display_data", methods=["GET"])
def display_data():

    # establishing the connection 
    cursor = mysql.connection.cursor()

    # defining the query
    sql_query = "SELECT * FROM trainer_detail"
    
    # executing the query
    cursor.execute(sql_query)

    # storing results of query or output of query in a variable
    trainer_data = cursor.fetchall()

    # closing the connection
    cursor.close()

    # returning a html page and inputting it the output of results of query
    return render_template("display_trainer_data.html", trainers=trainer_data)



# defining the debug True to automaticall detect changes when done and saved
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")


