#coding:utf-8

# definition des modules

from flask import Flask, render_template


# definition du routeur à l'aide de decorateurs

app = Flask(__name__)

# we define the router for page
@app.route("/")

# we define the function for our page with its corresponding methods
def index():
    return render_template("index.html", test="number")


# Here we verify if our application is executed by the python interpreter
if __name__ == "__main__":
    app.run(debug=True)    