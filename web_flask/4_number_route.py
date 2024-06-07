from flask import Blueprint

number_route = Blueprint('number_route', __name__)

@number_route.route('/4-number_route', methods=['GET'], strict_slashes=False)
def number():
    """Route that returns a message with a number."""
    return "{} is a number".format(1234)
