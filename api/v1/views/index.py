#!/usr/bin/python3
"""
        index view
        methods:
                Status: Return the status of the api request
                Stats: Retrieves the number of each objects by type
"""
import json
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status', strict_slashes=False)
def status():
    """Returns the status"""
    return ({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ gives somes Stats"""
    objects = storage.count()
    return ({"amenities": storage.count(Amenity),
             "cities": storage.count(City),
             "places": storage.count(Place),
             "reviews": storage.count(Review),
             "states": storage.count(State),
             "users": storage.count(User)})
