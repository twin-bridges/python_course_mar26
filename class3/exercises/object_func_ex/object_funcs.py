import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_object(api_client, obj_type, obj_params):

    # Check if object already exists
    object_exists = False
    status = ""
    payload = {"name": obj_params["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=obj_params)
        status = "updated"
    else:
        print(f"Configuring {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=obj_params)
        status = "created"

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {obj_params}"
        raise ChkPntConfigError(msg)

    return (api_res, status)


def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    return cfg_object(api_client, obj_type=obj_type, obj_params=host_object)


def cfg_network_object(api_client, network_object):
    """Create/update a network object."""
    obj_type = "network"
    return cfg_object(api_client, obj_type=obj_type, obj_params=network_object)


def cfg_group_object(api_client, group_object):
    """Create/update a group object."""
    obj_type = "group"
    return cfg_object(api_client, obj_type=obj_type, obj_params=group_object)
