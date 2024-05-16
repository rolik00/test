# DO NOT EDIT
import pytest

#from code import sum
from code import power
'''
@pytest.mark.parametrize(
    ('a', 'b', 'result'), [
        (100, 87, 187),
        (0, 0, 0),
        (324, 2, 326),
    ]
)

def test_sum(a, b, result):
    assert sum(a, b) == result
'''
@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (2, 3, 8),
        (0, 0, 1),
        (8, 3, 512),
    ]
)
def test_power(x, y, result):
    assert power(x, y) == result
