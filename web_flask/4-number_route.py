#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
Usage: python3 -m 4-number_route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ dsiplays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route('/c/<text>')
def c_with_text(text):
    """ displays c with text """
    return "C %s" % text.replace("_", " ")


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_with_text(text):
    """ display python is cool or with text  """
    return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """ displays n if its an integer """
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
