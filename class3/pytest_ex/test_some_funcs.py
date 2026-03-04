import pytest
from some_funcs import simple_sum, simple_div


def test_sums():
    assert simple_sum(1, 7) == 8
    assert simple_sum(0, 0) == 0


def test_negative_sums():
    assert simple_sum(-1, -1) == -2


@pytest.mark.parametrize(
    "val1, val2, result", [(10, 5, 15), (-1, 1, 0), (0, 0, 0), (100, 200, 300)]
)
def test_addition(val1, val2, result):

    assert simple_sum(val1, val2) == result


@pytest.mark.slow
def test_negative_sums():
    assert simple_sum(100, 1) == 101
    assert simple_sum(1001, 1) == 1002
    assert simple_sum(1, 1) == 2


def test_exception():
    with pytest.raises(ZeroDivisionError):
        simple_div(10, 0)
