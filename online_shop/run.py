from app import create_app
from app.models import db
from flask import Flask
import os

app = create_app()

if __name__ == '__main__':
    #Create DB tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)