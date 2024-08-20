import os
import sys

# Step 1: Set the Django settings module environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_searc.settings')

# Step 2: Add the project root to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Step 3: Initialize Django
import django

django.setup()

# Step 4: Import Django-dependent modules
from company_searc.documents import CompanyDocument
from django.conf import settings


def test_settings():
    print("Django settings loaded successfully")
    print("ELASTICSEARCH_DSL:", settings.ELASTICSEARCH_DSL)

def load_data():
    json_path = os.path.join(os.path.dirname(__file__), 'CompanyExtracted.json')

    with open(json_path, 'r') as f:
        data = json.load(f)
        for company in data:
            doc = CompanyDocument(**company)
            doc.save()

if __name__ == '__main__':
    test_settings()  # Test the settings first
    load_data()      # Load the data after verifying settings
