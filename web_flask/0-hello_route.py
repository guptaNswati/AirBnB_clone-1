#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
Usage: python3 -m 0-hello_route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ displays Hello HBNB """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
