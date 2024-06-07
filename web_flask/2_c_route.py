from flask import Blueprint

c_route = Blueprint('c_route', __name__)

@c_route.route('/2-c_route', methods=['GET'], strict_slashes=False)
def c():
    """Route that returns a message indicating C is fun."""
    return "C is fun!"
