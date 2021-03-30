import os

from google.cloud import datastore, logging

from liamnewmarch.wsgi import application

# Set up Cloud Logging
logging_client = logging.Client()
logging_client.get_default_handler()
logging_client.setup_logging()

# Apply env vars from the datastore
datastore_client = datastore.Client(os.environ.get('CLOUDSDK_CORE_PROJECT'))
for entity in datastore_client.query(kind='env_var').fetch():
    key = str(entity['key'])
    value = str(entity['value'])
    os.environ.setdefault(key, str(value))

app = application
