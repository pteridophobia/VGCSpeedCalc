import webbrowser
import sys
import time
# app.py
from flask import Flask , render_template          # import flask
app = Flask(__name__)             # create an app instance
app.debug = True
@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return render_template("index.html")       # which returns "hello world"

@app.route("/calc")
def calc():
    return render_template("calc.html")
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app