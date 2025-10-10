from flask import Flask

# this is main function
app = Flask(__name__)

#  defining something to display on page
my_data = "My Page"

# we are bindin app with the get_page function.
# /ahsan is website we need to mention after te ip address 127.0.0.1:5000/ahsan like this. you can give anyname 
@app.get("/ahsan")
def get_page():
    return my_data


contact_us = "Contact us at gmail ahsanzafar0501@gmail.com"

# defining a contact us page
# attaching the function with main function, you can access this info using 127.0.0.1:5000/contact
# you can use app.get or app.route both are same
@app.get("/contact")
def contact():
    return contact_us


# so __name__ is main function, then run app.run(). so it will run all functions to which app is attached
# or associated
if __name__ == "__main__":

    # when we make a change we need to stop flask and save the change and run it again
    # but if we want to make changes live and see them, we can use debug=True
    # whatever you change you don't need to stop flask
    # host 0.0.0.0 means any server withing my network range can interact with this page, 
    # it is useful in companies where webpage is hosted in one seerver and other need to interact with it
    # port, you can define you rown port by default it is 5000
    app.run(debug=True,host="0.0.0.0",port=12000)