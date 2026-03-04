
import pytest
from some_funcs import simple_div


def test_exception():
    with pytest.raises(ZeroDivisionError):
        simple_div(10, 0)
