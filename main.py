
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """Render the index page."""

    # Get all services
    services = get_services()

    # Render the index page with the list of services
    return render_template('index.html', services=services)


# Define the filter route
@app.route('/filter', methods=['POST'])
def filter():
    """Filter services based on user input."""

    # Get the user input
    category = request.form.get('category')
    keyword = request.form.get('keyword')

    # Filter the services based on the user input
    services = filter_services(category, keyword)

    # Render the index page with the filtered list of services
    return render_template('index.html', services=services)


# Define the service detail route
@app.route('/service/<service_id>')
def service_detail(service_id):
    """Render the service detail page."""

    # Get the service details
    service = get_service(service_id)

    # Render the service detail page with the service details
    return render_template('service-detail.html', service=service)


# Define the contact us route
@app.route('/contact-us')
def contact_us():
    """Render the contact us page."""

    # Render the contact us page
    return render_template('contact-us.html')


# Main driver function
if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
