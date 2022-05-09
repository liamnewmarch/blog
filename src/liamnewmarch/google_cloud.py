import os


def apply_datastore_env_vars(project):
    """Fetch `env_var` entities from the datastore and apply to the current env.

    Each `env_var` entity should have two string properties, `key` and `value`.
    """
    from google.cloud.datastore import Client
    for entity in Client(project).query(kind='env_var').fetch():
        key = str(entity['key'])
        value = str(entity['value'])
        os.environ.setdefault(key, value)


def setup_cloud_logging():
    """Attaches Google Cloud Logging to the root logger.

    https://cloud.google.com/logging/docs/setup/python"""
    from google.cloud.logging import Client
    logging = Client()
    logging.get_default_handler()
    logging.setup_logging()
