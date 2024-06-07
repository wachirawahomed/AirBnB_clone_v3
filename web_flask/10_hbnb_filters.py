from flask import Blueprint, render_template
from models import storage

hbnb_filters = Blueprint('hbnb_filters', __name__)

@hbnb_filters.route('/hbnb_filters', methods=['GET'], strict_slashes=False)
def hbnb_filters_route():
    """Route that renders a template with available amenities."""
    return render_template('10-hbnb_filters.html',
                           amenities=storage.all('Amenity').values())
