#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application. And
fetches data from database.
"""
from models import *
from flask import Flask
app = Flask(__name__)


@app.route('/states_list')
def display_states():
    """ display a HTML page containing list of states """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
