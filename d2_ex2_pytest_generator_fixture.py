import pytest


@pytest.fixture
def mygenfixture():
    # this is the fixture set-up area
    print("» setting up the fixture")

    # this is the one and only return value
    yield "this is my value"

    # this is the fixture teardown area
    print("» tearing down the fixture")


def test_my_stuff_1(mygenfixture):
    print("I am stuff 1", mygenfixture)

def test_my_stuff_2(mygenfixture):
    print("I am stuff 2", mygenfixture)

def test_my_stuff_3(mygenfixture):
    print("I am stuff 3", mygenfixture)
