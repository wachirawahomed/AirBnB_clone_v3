from flask import Blueprint

python_route = Blueprint('python_route', __name__)

@python_route.route('/3-python_route', methods=['GET'], strict_slashes=False)
def python():
    """Route that returns a message indicating Python is cool."""
    return "Python is cool!"
