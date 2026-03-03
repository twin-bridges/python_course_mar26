### Chkpnt SDK Exercise3

Connect to the Mgmt API using the Chkpnt SDK. Read your credentials in using the .env file and load_dotenv().

Create a new function named 'cfg_group' that is based upon your previously created 'cfg_net_objects' function.

This function should create the following group object:

```python
    group_params = {
        "name": "hq_net",
        "members": [
            "hq_net_128",
            "hq_net_129",
            "hq_net_130",
            "hq_net_131",
            "hq_net_132",
            "hq_net_133",
            "hq_net_134",
            "hq_net_135",
        ],
        "color": "blue",
    }

```

Once again your function should check if the group object exists (using the 'show-group' endpoint). If the object does already exist, then you should update the group using the 'set-group' endpoint.

If the object doesn't exist, then you should add it using the 'add-group' endpoint.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-group' or 'set-group' operation was not successful.

Once your object has been created, you will need to 'publish' it. You can do this by invoking the following:

```python
api_client.api_call(command="publish")
```

