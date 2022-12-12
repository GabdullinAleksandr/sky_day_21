import pytest
from day_21.slice import my_slice


@pytest.fixture
def coll():
    return [1, 2, 3, 4, 5, 6]


def test_slice(coll):
    assert my_slice(coll, 1, 4) == [2, 3, 4]
    assert my_slice([], 1, 4) == []
    assert my_slice(coll, -100) == [1, 2, 3, 4, 5, 6]
    assert my_slice(coll, -4, 4) == [3, 4]