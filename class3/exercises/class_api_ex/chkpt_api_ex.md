### Check Point Class Exercise

Create a class named 'ChkptAPI'.

The class should only have one method (dunder-init).

The dunder-init method should have the following signature:

```python
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
```

The 'mode' variable can either be 'web_api' or 'gaia_api'.

Inside your dunder-init method, initialize the following attribites: self.host, self.username, self.password, and self.ssl_verify.

Your dunder-init method should also set the following:

```python
self.headers = {"Content-Type": "application/json"}
```

Your dunder-init method should also create a 'base_url' attribute (self.base_url) and base_url should be constructed using the 'mode' variable (i.e. 'web_api' or 'gaia_api' and should also properly specify the API version.

If 'web_api', then api_version should be '2'. If 'gaia_api', then api_version should be '1.8'.

The base_url should be the proper url to use with the Gaia API or Mgmt API.

You should test your class using the following two test cases.

Test case1 (gaia_api):

```python
host = "chkpnt-pod99.lasthop.io"
user = "admin"
admin_pass = "testpass"

api_client = ChkptAPI(
    host=host, username=user, password=admin_pass, mode="gaia_api"
)
print("Testing ChkptAPI Class (Gaia API)")
print(api_client.base_url)
print()
```

Test case2 (web_api):

```python
host = "chkpnt-pod99.lasthop.io"
user = "admin"
admin_pass = "testpass"

api_client = ChkptAPI(
    host=host, username=user, password=admin_pass, mode="web_api"
)
print("Testing ChkptAPI Class (Mgmt API)")
print(api_client.base_url)
print()
```

Executing your test code should produce results similar to the following:

```bash
$ python chkpt_api_ex.py 
Testing ChkptAPI Class (Gaia API)
https://chkpnt-pod99.lasthop.io/gaia_api/v1.8/

Testing ChkptAPI Class (Mgmt API)
https://chkpnt-pod99.lasthop.io/web_api/v2/
```

You should verify that your 'base_url' is correct.
