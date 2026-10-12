from flask import Flask
from flask import render_template as rt
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user ="James Smith")

@app.route("/breweries")
def breweries():
    return "<p>Welcome to Breweries!</p>"

@app.route("/beer_types")
def beer_types():
    return "<p>Welcome to beer types</p>"

@app.route("/about")
def about():
    return "<p>Welcome to about us</p>"


    
if __name__ == "__main__":
    app.run(debug=True)