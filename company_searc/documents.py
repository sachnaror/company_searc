from django.conf import settings
from elasticsearch_dsl import Date, Document, Keyword, Text, connections

# Create a connection to the Elasticsearch server
connections.create_connection(hosts=[settings.ELASTICSEARCH_DSL['default']['hosts']])

class CompanyDocument(Document):
    ID = Keyword()
    URL = Text()
    RegisteredName = Text()
    RegistrationNumber = Keyword()
    UENIssueDate = Date()
    UENStatus = Text()
    LegalEntityType = Text()
    LegalEntityTypeSuffix = Text()
    Town = Text()
    CreatedAt = Date()
    UpdatedAt = Date()

    class Index:
        name = 'companies'

# Initialize the index
CompanyDocument.init()
