#!/usr/bin/python3
"""this script Starts a Flask web application
and the application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)



@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this func displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/airbnb-onepage/", strict_slashes=False)
def airbnb_onepage():
    """this displays 'Hello HBNB!'for /airbnb-onepage"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
