import pytest
from day_21.index_of import index_of

def test_index_of():
    assert index_of([2, 7, 3, 2, 4], 2) == 0
    assert index_of([], 2) == -1
    assert index_of([2, 7, 3, 2, 4], 2, 100) == -1
    assert index_of([2, 7, 3, 2, 4], 2, -50) == 0
    assert index_of([2, 7, 3, 2, 4], 3, -1) == -1
    assert index_of([2, 7, 3, 2, 4], 3, -4) == 2