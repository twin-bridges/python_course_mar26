from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa


def cfg_object(api_client, obj_type, obj_params):

    # Check if object already exists
    object_exists = False
    payload = {"name": obj_params["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=obj_params)
    else:
        print(f"Configuring {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=obj_params)

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {obj_params}"
        raise ChkPntConfigError(msg)


def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    cfg_object(api_client, obj_type=obj_type, obj_params=host_object)


def cfg_host_objects(api_client, host_objects):
    """Takes a list / iterator of host_objects and create/update them."""

    for host_obj in host_objects:
        cfg_host_object(api_client, host_obj)
