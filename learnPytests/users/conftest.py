import pytest
import requests

from src.conf.api_urls import SERVICE2_URL

@pytest.fixture
def get_users():
    response = requests.get(SERVICE2_URL)
    return response
