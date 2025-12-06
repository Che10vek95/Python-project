from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Model name: Products
class Product(db.Model):
    __tablename__ = 'products'

# Making columns for the Products table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
    status = db.Column(db.Boolean, nullable=True, default=True)
    category = db.Column(db.String(50), nullable=True)
    rating = db.Column(db.Float, nullable=True, default=0.0)
    sale = db.Column(db.Boolean, nullable=True, default=False)