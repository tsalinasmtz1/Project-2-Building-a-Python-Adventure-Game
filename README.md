# Real Estate Listings Website

A modern, Flask-based web application for browsing and managing real estate property listings.

## Features

- 🏠 Browse property listings with detailed information
- 🔍 Search and filter properties by location, price, and type
- ➕ Add new property listings
- 📱 Responsive design for mobile and desktop
- 💼 Support for various property types (House, Apartment, Condo, Townhouse, Land, Commercial)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tsalinasmtz1/Project-2-Building-a-Python-Adventure-Game.git
cd Project-2-Building-a-Python-Adventure-Game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Browse property listings, search for properties, or add new listings through the web interface.

## Project Structure

```
.
├── app.py                  # Main Flask application
├── properties.json         # Property data storage
├── requirements.txt        # Python dependencies
├── templates/              # HTML templates
│   ├── base.html          # Base template
│   ├── index.html         # Home page
│   ├── property_detail.html  # Property details page
│   ├── add_property.html  # Add property form
│   └── search.html        # Search page
└── static/
    └── css/
        └── style.css      # Stylesheet

```

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Jinja2 templates
- **Data Storage**: JSON file

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the MIT License.