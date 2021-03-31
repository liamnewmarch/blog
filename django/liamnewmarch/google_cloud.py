from google.cloud import datastore, logging


def apply_datastore_env_vars(project):
    """Fetch `env_var` entities from the datastore and apply to the current env.

    Each `env_var` entity should have two string properties, `key` and `value`.
    """
    for entity in datastore.Client(project).query(kind='env_var').fetch():
        key = str(entity['key'])
        value = str(entity['value'])
        os.environ.setdefault(key, value)


def setup_cloud_logging():
    """Attaches Google Cloud Logging to the root logger.

    https://cloud.google.com/logging/docs/setup/python"""
    logging_client = logging.Client()
    logging_client.get_default_handler()
    logging_client.setup_logging()
