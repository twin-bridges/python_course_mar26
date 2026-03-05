### Part1: Mgmt CLI Exercise

Using your pod and Netmiko SSH connect to your pod and enter expert mode.

Create a function named 'mgmt_cli_auth' with the following function signature:

```python
def mgmt_cli_auth(ssh_conn, username, password):
```

This function should execute the following to login to the mgmt_cli:

```bash
cmd = f'mgmt_cli login user "{username}" password "{password}" --format json'
```

Use Netmiko to send this command to the remote pod. Retrieve the response and process it as JSON.

From the returned data structure extract the session ID ("sid" key).

Your function should return this session ID.


### Part2: py.test testing of the 'mgmt_cli_auth' function.

Create a conftest.py file and a fixture named 'ssh_conn'. Your fixture should establish a Netmiko SSH connection to your pod and then "yield" that connection.

Next create pytest test file named "test_mgmt_cli_auth.py". In this test file you should test the 'mgmt_cli_auth' function.

You should test the following test cases:
1. If you provide an invalid username and password, then you should receive a KeyError exception.
2. If you provide valid credentials, then you should receive a session_id that is 43 characters long.

You should ensure your tests pass successfully.

