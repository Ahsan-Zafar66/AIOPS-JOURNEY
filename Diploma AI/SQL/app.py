import sys
import pandas as pd1
from connection import dbhelper

class flipkart:
    def __init__(self):
        self.db = dbhelper()

        self.menu()

    def menu(self):

        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave""")

        if user_input == "1":
            self.register()

        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
    
    def register(self):
        name = input("Enter Your Name")
        email = input("Enter Your Email")
        password = input("Enter Your Password")
        response = self.db.register(name,email,password)

        if response:
            print("Registration Succesful")
        else:
            print("Resgistration Unsuccesful")

        self.menu()

    def login(self):
        email = input("Enter Your Email")
        password = input("Enter Your Password")

        data = self.db.search(email,password)

        if len(data) == 0:
            print("Incorrect Email/Password")
            self.login()
        else:
            print("Hello",data[0][1])
obj = flipkart()