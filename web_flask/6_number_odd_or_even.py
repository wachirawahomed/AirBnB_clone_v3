from flask import Blueprint, render_template

number_odd_or_even = Blueprint('number_odd_or_even', __name__)

@number_odd_or_even.route('/6-number_odd_or_even/<int:n>', methods=['GET'], strict_slashes=False)
def number_odd_or_even_route(n):
    """Route that determines if a number is odd or even."""
    return render_template('6-number_odd_or_even.html', number=n)
