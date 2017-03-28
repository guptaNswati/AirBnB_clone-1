#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c_with_text(text):
    if "_" in text:
        text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
