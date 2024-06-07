from flask import Blueprint, jsonify
from models import storage
from models.state import State

states = Blueprint('states', __name__)

@states.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Route that returns a JSON list of all states."""
    all_states = storage.all(State)
    return jsonify([state.to_dict() for state in all_states.values()])
