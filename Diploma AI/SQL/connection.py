import mysql.connector
import sys

class dbhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="my_database")
            self.cursor = self.conn.cursor()
        except:
            print("Error occured, could connect to the database")
            sys.exit(0)

        else:
            print("Connected to Database")

    def register(self,name,email,password):
        try:
            self.cursor.execute(""" INSERT INTO `user_login_information` (`id`, `name`, `email`, `password`) VALUES (NULL, '{}', '{}', '{}')""".format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
        
    def search(self,email,password):
        self.cursor.execute("SELECT * FROM  `user_login_information` WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
        data = self.cursor.fetchall()
        

        print(data)
        return data