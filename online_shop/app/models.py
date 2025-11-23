from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Model name: Products
class Product(db.Model):
    __tablename__ = 'products'

# Define columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    