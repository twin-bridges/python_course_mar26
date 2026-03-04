from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa


def cfg_object(api_client, obj_type, obj_params, delete_obj=False):

    # Check if object already exists
    object_exists = False
    payload = {"name": obj_params["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if delete_obj:
        if object_exists:
            payload = {"name": obj_params["name"]}
            api_res = api_client.api_call(command=f"delete-{obj_type}", payload=payload)
        else:
            # Nothing to do, object to delete doesn't exist
            pass
        return

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=obj_params)
    else:
        print(f"Configuring {obj_type} object: {obj_params}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=obj_params)

    if not api_res.success:
        # Ternary operator (could just use conditional)
        action = "delete" if delete_obj else "configure"
        msg = f"Failed to {action} {obj_type} object: {obj_params}"
        raise ChkPntConfigError(msg)


def cfg_host_object(api_client, host_object):
    """Create/update a host object."""
    obj_type = "host"
    cfg_object(api_client, obj_type=obj_type, obj_params=host_object)


def delete_host_object(api_client, host_object):
    """Wrapper for better naming."""
    obj_type = "host"
    cfg_object(api_client, obj_type=obj_type, obj_params=host_object, delete_obj=True)


def delete_host_objects(api_client, host_objects):
    """Delete a list/interable of host objects."""
    for host_obj in host_objects:
        delete_host_object(api_client, host_obj)


def cfg_group_object(api_client, group_object):
    """Create/update a host object."""
    obj_type = "group"
    cfg_object(api_client, obj_type=obj_type, obj_params=group_object)


def cfg_host_objects(api_client, host_objects):
    """Takes a list / iterator of host_objects and create/update them."""

    for host_obj in host_objects:
        cfg_host_object(api_client, host_obj)
