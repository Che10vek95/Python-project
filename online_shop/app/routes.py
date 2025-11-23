from flask import Blueprint, render_template

# Define Blueprint
bp = Blueprint('routes', __name__)

# Define route for the home page
@bp.route('/')
def index():
    return render_template('index.html')