import pytest

from d2_ex3_pytest_useful_generator_fixture import get_books
import os
import json

BOOKS_DATASET = [
    {'title': 'Jungle Book', 'author': 'Rudyard Kipling'},
    {'title': 'Amintiri din copilărie', 'author': 'Ion Creangă'},
    {'title': 'Harap Alb', 'author': 'Ion Creangă'},
]


# this is the same as before,
# but we __auto__-generate the file only once,
# and cleanup afterwards.

# so this is a module-level fixture, with auto-teardown


jsonfile = "some-file-for-testing.json"

# this will be run regardless of using it as a fixture
@pytest.fixture(scope="module", autouse=True)
def _populate_json_file():
    # set-up: create json file

    with open(jsonfile, 'w') as f:
        json.dump(BOOKS_DATASET, f)

    yield

    # teardown: delete file
    os.unlink(jsonfile)


# TODO: temă pentru acasă:
# se poate implementa acest fixture cu tempfile.TemporaryFile ?
# dacă nu, atunci implementați-l cu tempfile.mkstemp

def test_get_all_books():
    assert get_books(jsonfile) == BOOKS_DATASET

def test_get_books_by_author():
    assert get_books(jsonfile, 'Rudyard Kipling') == [
        {'title': 'Jungle Book', 'author': 'Rudyard Kipling'}
    ]

def test_get_books_by_inexistant_author():
    assert get_books(jsonfile, "!!! not an author !!!") == []
