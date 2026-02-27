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

Next create an 'install_fw_policy' function. This function should take at least one argument, the 'api_client'.

Here is what the function signature looks like for my reference implementation:

```python
def install_fw_policy(api_client, policy_package="Standard", targets=None):
```

For the Mgmt API 'install-policy' operation, you will need to provide a payload that specifies the following:

```python
    payload = {"policy-package": "Standard", "targets": targets}
    api_res = api_client.api_call(command="install-policy", payload=payload)
```

'targets' will be your firewall name which will be host part of your pod's FQDN. So for 'chkpnt-pod99.lasthop.io', the firewall targets will be:

```python
targets = ["chkpnt-pod99"]
```

You can decide how you want to implement this targets variable. In other words, you can hard-code it or you can extract it from the FQDN. Similarly, you can decide if you pass it into the function or if it is hard-coded in the function.

##### HERE ######


    management_rules = [
        {
            "layer": "Network",
            "name": "Corp Web Server Access",
            "source": "Any",
            "destination": "Corp Web Server",
            "service": ["http", "https"],
            "action": "Accept",
            "position": 1,
        },
    ]

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        cfg_host_object(api_client, corp_web_server)
        cfg_fw_policy(api_client, fw_rules=management_rules)
        api_client.api_call(command="publish")
        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
