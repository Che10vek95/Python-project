from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Product

# Define Blueprint
bp = Blueprint('routes', __name__)

# Define route for the home page
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/products')
def products():
    products = Product.query.all()
    return render_template('product_list.html', products=products)

@bp.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        # description = request.form['description']
        price = request.form['price']
        qantity = request.form['quantity']
        product = Product(name=name, author=author, price=float(price), quantity=int(qantity))
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!')
        return redirect(url_for('routes.products'))
    
    return render_template('product_form.html', action ='Add', product=None)