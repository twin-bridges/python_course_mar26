### pytest exercise1

You will need to use pip to install pytest into your Python virtual environment.

```bash
pip install pytest==9.0.2
```

Create a Python file named 'simple_funcs.py'. Inside this file, define the following function:

```python
def split_ip_addr(ip_addr):
    octets = ip_addr.split(".")
    if len(octets) != 4:
        raise ValueError("Invalid ip_addr, split('.') didn't return 4 octets")

    return octets
```

In the same directory, create a "test_funcs_ex.py". This file will import the "split_ip_addr" function and then use pytest to test it.

Construct the following test case:

```python
def test_split_ip(ip_addr, result):
    assert split_ip_addr(ip_addr) == result
```

Use the `parametrize` decorator and then test the following IP addresses:

```python
"1.1.1.1"
"182.227.100.10"
"127.0.0.1"
```

Verify each one of the above IP addresses passes the test properly.


Next construct a test that verifies each of the following three invalid IP addresses properly raises a ValueError exception: "137.1.1", "37.1", "198.1.1.10.17".

Finally construct the following test:

```python
def test_skip():
    assert split_ip_addr("1.1.1.1") == ["1", "1", "1", "1"]
```

This test should be skipped if 'sys.platform == "linux"'.

Run py.test to make sure all of the above tests pass or are skipped.

Your output should look similar to the following:

```shell
$ py.test -s -v test_funcs_ex.py 
============== test session starts =======================
platform linux -- Python 3.13.12, pytest-9.0.2
cachedir: .pytest_cache
rootdir: /home/kbyers/python_course_mar26/class3/exercises/pytest_ex
collected 7 items

test_funcs_ex.py::test_split_ip[1.1.1.1-result0] PASSED
test_funcs_ex.py::test_split_ip[182.227.100.10-result1] PASSED
test_funcs_ex.py::test_split_ip[127.0.0.1-result2] PASSED
test_funcs_ex.py::test_invalid_ip[137.1.1] PASSED
test_funcs_ex.py::test_invalid_ip[37.1] PASSED
test_funcs_ex.py::test_invalid_ip[198.1.1.10.17] PASSED
test_funcs_ex.py::test_skip SKIPPED (Skip test on Linux)

========== 6 passed, 1 skipped in 0.02s ==================
```

