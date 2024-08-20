# Company Search Django Project

This is a Django project that provides functionality to search and retrieve information about companies. It uses Elasticsearch for indexing and searching company data.

## Directory Structure

- `company_searc/`
  - `CompanyExtracted.json`: JSON file containing extracted company data
  - `documents.py`: Django app for defining Elasticsearch document models
  - `manage.py`: Django's command-line utility for administrative tasks
  - `load_data.py`: Script for loading company data from `CompanyExtracted.json` into Elasticsearch
  - `company_searc/`
    - `asgi.py`: Entry point for ASGI-compatible web servers to serve the project
    - `settings.py`: Django project settings
    - `urls.py`: URL declarations for the Django project
    - `wsgi.py`: Entry point for WSGI-compatible web servers to serve the project
  - `app1/`
    - `models.py`: Django models for the application
    - `apps.py`: Django application configuration
    - `admin.py`: Django admin site configuration
    - `tests.py`: Unit tests for the application
    - `urls.py`: URL patterns for the application
    - `views.py`: Django views for the application
    - `templates/`
      - `detailpage.html`: HTML template for the company detail page
      - `homepage.html`: HTML template for the homepage

## Prerequisites

- Python 3.x
- Django
- Elasticsearch (version compatible with the `elasticsearch-dsl` library)

## Installation

1. Clone the repository or download the source code.
2. Install the required Python packages: `pip install django elasticsearch-dsl`
3. Configure the Elasticsearch connection settings in `company_searc/settings.py`.
4. Run Django migrations to create the necessary database tables: `python manage.py migrate`

## Usage

1. Start the Elasticsearch server if it's not already running.
2. Load company data into Elasticsearch by running `python load_data.py`.
3. Run the Django development server: `python manage.py runserver`
4. Access the application through the provided URLs (e.g., `http://localhost:8000/`).

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository
2. Create a new branch for your feature or bug fix
3. Make your changes and commit them with descriptive commit messages
4. Push your changes to your forked repository
5. Submit a pull request to the main repository

## License

This project is licensed under the [MIT License](LICENSE).
