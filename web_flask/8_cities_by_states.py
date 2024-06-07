from flask import Blueprint, render_template
from models import storage
from models.state import State

cities_by_states = Blueprint('cities_by_states', __name__)

@cities_by_states.route('/8-cities_by_states', methods=['GET'], strict_slashes=False)
def cities_by_states_route():
    """Route that renders a list of cities grouped by state."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)
