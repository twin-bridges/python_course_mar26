from some_funcs import simple_sum


def test_sums():
    assert simple_sum(1, 7) == 8
    assert simple_sum(0, 0) == 0


def test_negative_sums():
    assert simple_sum(-1, -1) == -2
