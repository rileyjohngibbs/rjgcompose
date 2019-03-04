import pytest


@pytest.fixture
def add_one():
    def add_one_(num):
        return num + 1
    return add_one_


@pytest.fixture
def square():
    def square_(num):
        return num**2
    return square_


@pytest.fixture
def triple():
    def triple_(num):
        return num * 3
    return triple_
