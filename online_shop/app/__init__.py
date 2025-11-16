from flask import Flask
import json
import os

# Function to create and configure the Flask application
def create_app():
    base_dir = os.path.abspath(os.path.dirname(__file__) + '/..')
    app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static')) # Set template and static folder paths
    
    
    #Register Blueprints
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)  
    return app