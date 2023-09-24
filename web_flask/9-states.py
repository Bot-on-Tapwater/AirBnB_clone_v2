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

    @app.route('/states', strict_slashes=False)
    @app.route('/states/<id>', strict_slashes=False)
    def states(id=None):
        """List all states"""
        states = storage.all(State)
        return render_template("9-states.html", states=states, id=id)

    app.run(host='0.0.0.0', port=5000)
