### Gaia API Auth Exercise

Create a Python script that authenticates to the Gaia API in your pod.

After you have authenticated extract the session ID and reuse this session ID to execute the following API command: "show-api-versions"

Print the returned JSON from that API command to standard output.

Bonus: Do the above, but create the following functions to assist you: 'login', 'api_call', 'logout'.

The 'login' function should handle the login and return the response (or alternatively return the session ID).

The 'api_call' function should handle API calls to the Gaia API and return the response. My reference function signature looks as follows:

```python
def api_call(base_url, endpoint, headers, payload=None, ssl_verify=False):
```

The 'logout' function should gracefully log you out of the Gaia API.

