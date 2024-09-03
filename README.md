## Flask Application Design for Solution Catalog
### HTML Files
- **index.html**: Landing page that displays a list of services offered by the organization.
  - Includes a form to allow the user to filter the services by category or keyword.
- **service-detail.html**: Page that displays the details of a specific service.
  - Includes a description of the service, its offerings, and pricing information.
- **contact-us.html**: Form for users to contact the organization for any inquiries or to request a consultation.
 
### Routes
- **`/`**: Main route that renders the `index.html` page.
- **`/filter`**: Route that handles the form submission from the `index.html` page.
  - Filters the services based on the user input and displays the filtered results on the `index.html` page.
- **`/service/<service_id>`**: Route that displays the details of a specific service by rendering the `service-detail.html` page.
- **`/contact-us`**: Route that renders the `contact-us.html` page.