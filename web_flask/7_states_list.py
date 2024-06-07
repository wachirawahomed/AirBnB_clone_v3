from flask import Blueprint, render_template
from models import storage
from models.state import State

states_list = Blueprint('states_list', __name__)

@states_list.route('/7-states_list', methods=['GET'], strict_slashes=False)
def states_list_route():
    """Route that renders a list of states."""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)
