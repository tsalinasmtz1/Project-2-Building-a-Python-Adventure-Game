"""
Real Estate Listings Website
A Flask-based web application for browsing and managing real estate property listings.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'real-estate-secret-key-2026-dev-only')

# Path to the JSON file storing property data
DATA_FILE = 'properties.json'


@app.template_filter('format_price')
def format_price(value):
    """Format price with thousand separators"""
    try:
        return "{:,.0f}".format(float(value))
    except (ValueError, TypeError):
        return value


def load_properties():
    """Load properties from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []


def save_properties(properties):
    """Save properties to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(properties, f, indent=2)


@app.route('/')
def index():
    """Display all property listings on the home page"""
    properties = load_properties()
    return render_template('index.html', properties=properties)


@app.route('/property/<int:property_id>')
def property_detail(property_id):
    """Display detailed information about a specific property"""
    properties = load_properties()
    property_data = None
    
    for prop in properties:
        if prop['id'] == property_id:
            property_data = prop
            break
    
    if property_data is None:
        flash('Property not found', 'error')
        return redirect(url_for('index'))
    
    return render_template('property_detail.html', property=property_data)


@app.route('/add', methods=['GET', 'POST'])
def add_property():
    """Add a new property listing"""
    if request.method == 'POST':
        properties = load_properties()
        
        # Generate new ID
        new_id = max([p['id'] for p in properties], default=0) + 1
        
        # Create new property object
        new_property = {
            'id': new_id,
            'title': request.form.get('title'),
            'price': request.form.get('price'),
            'location': request.form.get('location'),
            'bedrooms': request.form.get('bedrooms'),
            'bathrooms': request.form.get('bathrooms'),
            'sqft': request.form.get('sqft'),
            'description': request.form.get('description'),
            'property_type': request.form.get('property_type'),
            'status': request.form.get('status', 'For Sale')
        }
        
        properties.append(new_property)
        save_properties(properties)
        
        flash('Property added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_property.html')


@app.route('/search')
def search():
    """Search for properties based on criteria"""
    properties = load_properties()
    query = request.args.get('q', '').lower()
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    property_type = request.args.get('type', '')
    
    filtered_properties = properties
    
    # Filter by search query (title, location, description)
    if query:
        filtered_properties = [
            p for p in filtered_properties
            if query in p['title'].lower() 
            or query in p['location'].lower()
            or query in p['description'].lower()
        ]
    
    # Filter by price range
    if min_price is not None:
        filtered_properties = [
            p for p in filtered_properties
            if float(p['price']) >= min_price
        ]
    
    if max_price is not None:
        filtered_properties = [
            p for p in filtered_properties
            if float(p['price']) <= max_price
        ]
    
    # Filter by property type
    if property_type:
        filtered_properties = [
            p for p in filtered_properties
            if p['property_type'] == property_type
        ]
    
    return render_template('search.html', properties=filtered_properties, query=query,
                         min_price=min_price, max_price=max_price, selected_type=property_type)


if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
