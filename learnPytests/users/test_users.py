import pytest
import requests

from src.conf.api_urls import SERVICE_URL

from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA
from src.schemas.user import User


@pytest.mark.skip
def test_equal():
    assert 1 == 1, "Num is not equal"
@pytest.mark.skip
def test_is_not_equal():
    assert 1 != 2, "Num is equal"    
@pytest.mark.skip('Сломал переделкой на pydantic, нужно выносить из класса')
def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(POST_SCHEMA)

# resp = requests.get(SERVICE2_URL)
#
# print(resp.json())
@pytest.mark.skip
def test_getting_user_list(get_users, make_number):
    Response(get_users).assert_status_code(200).validatepydantic(User)
    print(make_number)





  ##[{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]