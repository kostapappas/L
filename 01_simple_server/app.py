#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Flask Web Server Example
Greek Municipal Website - Δήμος Άρτας (Municipality of Arta)

This is a basic example for teaching web server fundamentals
"""

from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    """Serve the main page of the municipality website"""
    return render_template('index.html')

# Route for services page
@app.route('/services')
def services():
    """Serve the services page"""
    services_list = [
        "Έκδοση Πιστοποιητικών", # Certificate Issuance
        "Αδειοδότηση Επιχειρήσεων", # Business Licensing
        "Πολεοδομικές Άδειες", # Urban Planning Permits
        "Καθαριότητα & Ανακύκλωση", # Cleanliness & Recycling
        "Κοινωνικές Υπηρεσίες" # Social Services
    ]
    return render_template('services.html', services=services_list)

# Route for contact page
@app.route('/contact')
def contact():
    """Serve the contact information page"""
    contact_info = {
        'address': 'Πλατεία Εθνικής Αντίστασης 1, Άρτα 47100',
        'phone': '+30 26810 35000',
        'email': 'info@arta.gr',
        'hours': 'Δευτέρα - Παρασκευή: 08:00 - 15:00'
    }
    return render_template('contact.html', contact=contact_info)

if __name__ == '__main__':
    # Run the development server
    print("Starting Δήμος Άρτας Web Server...")
    print("Visit: http://localhost:5001")
    app.run(debug=True, host='0.0.0.0', port=5001) 