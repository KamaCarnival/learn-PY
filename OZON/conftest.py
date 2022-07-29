import pytest
from OZON.persons import Person

@pytest.fixture
def clear_names():
    Person.name=None