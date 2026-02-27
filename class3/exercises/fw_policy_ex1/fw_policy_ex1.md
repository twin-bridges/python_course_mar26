### Firewall Policy Exercise1

### The management rules for the Ansible Server must be installed prior to this exercise.

Connect to the Mgmt API using the Chkpnt SDK. Once again I would read your credentials in using the .env file and load_dotenv().

Re-use or re-implement your function named 'cfg_host_objects' that you previously created in the "./class3/exercise/chkpnt_sdk_ex" exercises. Note, in my reference function I added a second argument, 'host_object'. Consequently, I now pass the 'api_client' and the 'host_object' into the function. The 'host_object' is the host dictionary I am intending on configuring.

```python
def cfg_host_object(api_client, host_object):
```

This function should create the following host object:

```python
corp_web_server = {
    "name": "Corp Web Server",
    "ipv4-address": "172.31.144.220",
    "color": "dark green",
}
```

Next create a 'cfg_fw_rule' function. This function should be essentially similar as your previous 'cfg_host_objects' function.

Once again your function should check if the given firewall rule exists (using 'show-access-rul)e. If the rule does already exist, then your script should update the firewall rule using 'set-access-rule'.

If the firewall rule doesn't exist, then it should add the rule using 'add-access-rule'.

You should use the ".success" attribute of the response object to ensure your firewall rule was created or updated successfully.

You should raise an exception if the 'add-access-rule' or 'set-access-rule' operation was not successful.

Note, for the 'show-access-rule' call you only need to pass the "layer" field and the "name" field in as payload to the API call (see the Mgmt API documentation for additional details).

Your firewall rule should be the following:

```python
    corp_fw_rule = { 
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https"],
        "action": "Accept",
        "position": 1,
    } 
```

After you have pushed both the host object and the new firewall rule, you will to both publish and install the firewall policy. In order to do this, you will need to make the following API call.

In order to publish, you can simply invoke the following:

```python
api_client.api_call(command="publish")
```

And in order to install the firewall policy, you will need to do something similar to this.

```python
    payload = {"policy-package": "Standard", "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
```

Where 'targets' is your firewall name. So for 'pod99' (host = 'chkpnt-pod99.lasthop.io'), the firewall targets will be:

```python
targets = ["chkpnt-pod99"]
```

You can decide whether you want to create a function for 'install_fw_policy' or whether you want to just implement it directly in your main program.

