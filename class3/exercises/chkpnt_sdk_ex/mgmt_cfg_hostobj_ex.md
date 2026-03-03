### Chkpnt SDK Exercise1

Connect to the Mgmt API using the Chkpnt SDK. You should read your API credentials in using the .env file and load_dotenv().

Create a function named 'cfg_host_objects'  that takes one argument (api_client). In this function configure the following three host objects:

```python
    smart_console_private = {
        "name": "Windows SmartConsole",
        "ipv4-address": "172.31.12.101",
        "color": "red",
    }
    smart_console_public = {
        "name": "Windows SmartConsole Public",
        "ipv4-address": "3.71.9.240",
        "color": "red",
    }
    ansible_server = {
        "name": "Ansible Server",
        "ipv4-address": "3.125.34.232",
        "color": "black",
    }
```

Your function should do the following:
1. Use the 'show-host' endpoint and the object name to see if the object already exists.
2. If the object already exists, then use the 'set-host' endpoint to update the host object (using the dictionaries provided above).
3. If the object doesn't exist, then use the 'add-host' endpoint to create the given host object.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-host' or 'set-host' operation was not successful.

Once your object has been created, you will need to 'publish' it. You can do this by invoking the following:

```python
api_client.api_call(command="publish")
```
