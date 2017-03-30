#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application. And
fetches data from database.
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb')
def display_cities():
    """ display a HTML page containing states, cities and amenities """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = storage.all("User").values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, places=places, users=users)


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
