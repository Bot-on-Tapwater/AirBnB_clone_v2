#!/usr/bin/python3

"""Simple flask app"""

if __name__ == '__main__':
    # import module
    from flask import Flask, render_template
    from models import storage
    from models.state import State

    # create instance of Flask class
    app = Flask(__name__)

    @app.teardown_appcontext
    def cleanup_app_context(random_arg):
        """Remove SQLAlchemy Session"""
        storage.close()

    @app.route('/cities_by_states', strict_slashes=False)
    def cities_by_states():
        """List all cities in a state"""
        states = storage.all(State)
        return render_template("8-cities_by_states.html", states=states)

    app.run(host='0.0.0.0', port=5000)
