### Chkpnt SDK Exercise1

Connect to the Mgmt API using the Chkpnt SDK. Once again I would read your credentials in using the .env file and load_dotenv().

Create a new function named 'cfg_net_objects' that is based upon your previously created 'cfg_host_objects' function.

This function should create the following network objects:

```python
    hq_net_128 = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
    }
    hq_net_129 = {
        "name": "hq_net_129",
        "subnet": "172.31.129.0",
    }
    hq_net_130 = {
        "name": "hq_net_130",
        "subnet": "172.31.130.0",
    }
    hq_net_131 = {
        "name": "hq_net_131",
        "subnet": "172.31.131.0",
    }
    hq_net_132 = {
        "name": "hq_net_132",
        "subnet": "172.31.132.0",
    }
    hq_net_133 = {
        "name": "hq_net_133",
        "subnet": "172.31.133.0",
    }
    hq_net_134 = {
        "name": "hq_net_134",
        "subnet": "172.31.134.0",
    }
    hq_net_135 = {
        "name": "hq_net_135",
        "subnet": "172.31.135.0",
    }
```

For each of these networks you should also specify the following (i.e. the mask-length is always /24 and the object color is always green.

```python
        network_obj["mask-length"] = 24
        network_obj["color"] = "green"
```

Once again your function should check if the given network object exists (using 'show-network). If it does already exist, then it should update the network object using 'set-network'.

If the network object doesn't exist, then it should add it using 'add-network'.

You should use the ".success" attribute of the response object to ensure your object was created or updated successfully.

You should raise an exception if the 'add-network' or 'set-network' operation was not successful.

