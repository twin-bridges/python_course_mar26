### Test object functions

Use the referenced 'conftest.py' file as a test fixture. You will need to change the 'api_server' variable in this file to match your pod.

```python
# Change to your pod
api_server = "chkpnt-pod99.lasthop.io"
```

Create a 'test_object_funcs.py' file. This file should import the three object creation functions.

```python
from object_funcs import cfg_host_object, cfg_network_object, cfg_group_object
```

You should create the following three tests:

```python
def test_host_object_creation(web_api_session):
```

```python
def test_network_object_creation(web_api_session):
```

```python
def test_group_object_creation(web_api_session):
```

Each of these three tests should create a test object of the given type and then verify the following:

```python
assert api_res.success is True
assert status in ["created", "updated"]
```

Use 'pytest' to run these tests and verify your tests properly pass.
