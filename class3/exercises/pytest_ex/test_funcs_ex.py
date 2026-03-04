import pytest
import sys
from simple_funcs import split_ip_addr


@pytest.mark.parametrize(
    "ip_addr, result",
    [
        ("1.1.1.1", ["1", "1", "1", "1"]),
        ("182.227.100.10", ["182", "227", "100", "10"]),
        ("127.0.0.1", ["127", "0", "0", "1"]),
    ],
)
def test_split_ip(ip_addr, result):
    assert split_ip_addr(ip_addr) == result


@pytest.mark.parametrize(
    "bogus_ip_addr",
    [
        "137.1.1",
        "37.1",
        "198.1.1.10.17",
    ],
)
def test_invalid_ip(bogus_ip_addr):
    with pytest.raises(ValueError):
        split_ip_addr(bogus_ip_addr)


@pytest.mark.skipif(sys.platform == "linux", reason="Skip test on Linux")
def test_skip():
    assert split_ip_addr("1.1.1.1") == ["1", "1", "1", "1"]
