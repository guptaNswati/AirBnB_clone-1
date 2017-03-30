#!/usr/bin/python3
"""
This module contains a script that starts a Flask web application. And
fetches data from database.
"""
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', defaults={'id': 'all'})
@app.route('/states/<id>')
def display_cities(id):
    """ display a HTML page containing cities of a state """
    states = storage.all("State").values()
    if id == 'all':
        return render_template('9-states.html', states=states, get="all")
    else:
        for state in states:
            if id == str(state.id):
                return render_template('9-states.html', states=state, get="1")
        return render_template('9-states.html', states="Not found!",
                               get="None")


@app.teardown_appcontext
def remove_session(exception=None):
    """ remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
