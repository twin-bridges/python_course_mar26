### Exercise on creating a common object function.

In the Check Point SDK exercises from Wednesday, we created host objects, network objects, and a group object.

This code had a common pattern of use f"show-{obj_type}" to check for the existence of an object (based on the name of the object).

If the object exists, then use f"set-{obj_type}" to update the existing object.

If the object doesn't exist, then use f"add-{obj_type}" to add the existing object.

Given the above, you should be able to create a common function to implement this logic. This common function would support host objects, network objects, and group objects.

Your function signature should look as follows:

```python
def cfg_object(api_client, obj_type, obj_params):
```

If your "set" or "add" operation fails, then you should raise the following exception.

```python
msg = f"Failed to configure {obj_type} object: {obj_params}"
raise ChkPntConfigError(msg)
```

You should return the '(api_resp, status)' from the 'cfg_object' function unless an exception was raised. 'status' will either be 'updated' or 'created' depending on the action the function took.

Once the 'cfg_object' function has been created, you should be able to create the following three wrapper functions.

```python
def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    return cfg_object(api_client, obj_type=obj_type, obj_params=host_object)
```

```python
def cfg_network_object(api_client, network_object):
    """Create/update a network object."""
    obj_type = "network"
    return cfg_object(api_client, obj_type=obj_type, obj_params=network_object)
```

```python
def cfg_group_object(api_client, group_object):
    """Create/update a group object."""
    obj_type = "group"
    return cfg_object(api_client, obj_type=obj_type, obj_params=group_object)
```

