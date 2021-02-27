import pytest

from app import configuration
from app.repository import database_connection


def load_configuration():
    configuration.load(configuration.TEST_CONFIG)


def load_database():
    from app.repository.model.list import List  # noqa
    from app.repository.model.item import Item  # noqa
    database_connection.load()


@pytest.fixture(scope="session", autouse=True)
def register_services():
    load_configuration()
    load_database()
