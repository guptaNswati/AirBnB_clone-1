#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application. And
fetches data from database.
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def display_cities():
    """ display a HTML page containing cities of a state """
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
