import pytest

from d2_ex3_pytest_useful_generator_fixture import get_books
import tempfile
import os
import json

BOOKS_DATASET = [
    {'title': 'Jungle Book', 'author': 'Rudyard Kipling'},
    {'title': 'Amintiri din copilărie', 'author': 'Ion Creangă'},
    {'title': 'Harap Alb', 'author': 'Ion Creangă'},
]

@pytest.fixture
def jsonfile():
    # set-up: create json file

    filename = "some-file-for-testing.json"
    
    with open(filename, 'w') as f:
        json.dump(BOOKS_DATASET, f)

    yield filename

    # teardown: delete file
    os.unlink(filename)


# TODO: temă pentru acasă:
# se poate implementa acest fixture cu tempfile.TemporaryFile ?
# dacă nu, atunci implementați-l cu tempfile.mkstemp

def test_get_all_books(jsonfile):
    assert get_books(jsonfile) == BOOKS_DATASET

def test_get_books_by_author(jsonfile):
    assert get_books(jsonfile, 'Rudyard Kipling') == [
        {'title': 'Jungle Book', 'author': 'Rudyard Kipling'}
    ]

def test_get_books_by_inexistant_author(jsonfile):
    assert get_books(jsonfile, "!!! not an author !!!") == []
