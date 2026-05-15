from unittest.mock import patch, MagicMock, Mock
from d2_ex6_testing_and_mocking import get_todos, URL

import json


TODOS = [
  {
    "userId": 10,
    "id": 101,
    "title": "My pending todo",
    "completed": False
  },
  {
    "userId": 10,
    "id": 102,
    "title": "My completed todo",
    "completed": True
  },
]

# first, we tell mock about the method that will be patched
@patch("requests.get")
def test_response_ok(patched_get):
    # we need to pretend this is a response object
    patched_get.return_value = Mock(
        status_code = 200,
        text = json.dumps(TODOS)
    )

    assert get_todos(URL) == [TODOS[0]]

    # we also want to make sure
    # that our patched method was the one really called
    patched_get.assert_called_with(URL)

@patch("requests.get")
def test_malformed_json(patched_get):
    patched_get.return_value = Mock(
        status_code = 200,
        text = "i am not json"
    )

    assert get_todos(URL) == []

@patch("requests.get")
def test_http_error(patched_get):
    patched_get.return_value = Mock(
        status_code = 404,
    )

    assert get_todos(URL) == []