#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
Usage: python3 -m 6-number_odd_or_even
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ displays Hello HBNB """
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


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display a HTML page only if n is an integer """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_even(n):
    """ display a HTML page only if n is an integer """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
