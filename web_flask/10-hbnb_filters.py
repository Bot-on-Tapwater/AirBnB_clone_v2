#!/usr/bin/python3

"""Simple flask app"""

if __name__ == '__main__':
    # import module
    from flask import Flask, render_template
    from models import storage
    from models.state import State
    from models.city import City
    from models.amenity import Amenity

    # create instance of Flask class
    app = Flask(__name__)

    @app.teardown_appcontext
    def cleanup_app_context(random_arg):
        """Remove SQLAlchemy Session"""
        storage.close()

    @app.route("/hbnb_filters", strict_slashes=False)
    def hbnb_filters():
        """Display HTML page"""
        states = storage.all(State)
        cities = storage.all(City)
        amenities = storage.all(Amenity)

        return render_template(
            "10-hbnb_filters.html", states=states, amenities=amenities)

    app.run(host='0.0.0.0', port=5000)
