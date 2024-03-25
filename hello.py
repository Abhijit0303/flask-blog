from flask import Flask, render_template

#Create flask instance
app = Flask(__name__)

#Create a route decorator
#www.website.com/about  --- /about is route

# @app.route("/")
# def home():
#     return "<h1>Hello World</h1>"


# '''
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags -- dont use html tags even if they are there
# '''

@app.route("/")
def home():
    first_name = "Abhijit"
    stuff = "This is <strong>Bole</strong> text"

    fav_pizza = ["pepproni", 
                 "CHeese",
                 "Chickken"
                 ]
    return render_template("index.html", first_name = first_name, stuff = stuff, fav_pizza = fav_pizza)

# @app.route("/user/<name>")
# def user(name):
#     return "<h1>Hello {} !!!</h1>".format(name)

@app.route("/user/<name>")
def userName(name):
    return render_template("users.html", user_name = name)


#invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500