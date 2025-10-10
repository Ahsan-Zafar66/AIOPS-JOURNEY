# we will set up session management
# user will enter their credentials on a webpage and either they will be logged in or rejected
# we will create a table in mysql on ubuntu linux, then we will check if the entered credentials are present in databae or not
# based on the presence or absence we will either reject or accept 

from flask import Flask, render_template,request,url_for,session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

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

# adding secret key for session
app.secret_key = "ahsanzafarqau"



@app.get("/home")
def first_page():
    return render_template("webpage.html")

# integration of login or submit button with the next function
#action="{{ url_for('login') }}" method="POST"
msg = ""
@app.route("/login",methods=["POST","GET"])
def login():
    msg = ""
    if request.method == "POST":
        
        username_data = request.form["username"]
        password_data = request.form["password"]
        email_data = request.form["email"]

        print(username_data,password_data)
        
        # mysql query
        sql_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        

        
        # # values extracted from form which was written in form and submit button was pressed
        # values = (fname,lname,designation,username,password,salary,join_date,email)

        # establishing the connection with mysql database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # executing query
        cursor.execute(sql_query, (username_data, password_data))

        result = cursor.fetchone()

        print(result)
        print("reached here")

        if result:
            session["loggedin"] = True
            session["id"] = result["id"]
            session["username"] = result["username"]
            session["password"] = result["password"]
            return render_template("after_login.html",username=session["username"])

        else:
            msg ="Incorrect username or password!!!!"

            cursor.close()
    
    return render_template("webpage.html",msg=msg)


        # commiting change in mysql
        #mysql.connection.commit()

        # closing connection
# registration.html register button
@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/registration_complete",methods=["POST","GET"])
def registration_data():
    msg = ""

    if request.method == "POST":
        entered_name = request.form["name"]
        entered_password = request.form["password"]
        entered_email = request.form["email"]


        # MySQL query to insert user data into the database
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Check if email already exists
        cursor.execute("SELECT * FROM users WHERE email = %s", [entered_email])
        existing_user = cursor.fetchone()

        if existing_user:
            msg = "Email already exists! Please choose another."
        else:
            # Insert the new user data into the database
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (entered_name, entered_email, entered_password))
            
            mysql.connection.commit()  # Commit changes to the database
            msg = "Registration successful! Go to login page."

        cursor.close()
    elif request.method == "POST":
        msg = "Please Enter the details first"
    
    return render_template("registration_complete.html")






@app.route("/")
def index():
    if 'loggedin' in session:
        return render_template("after_login.html",username=session["username"])
    else:
        return redirect(url_for("first_page"))


@app.route("/logout")        
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return redirect(url_for("first_page"))





if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

