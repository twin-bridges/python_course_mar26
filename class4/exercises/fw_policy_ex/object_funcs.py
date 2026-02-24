from chkpt_exceptions import ChkPntConfigError
import ipdb  # noqa


def cfg_host_object(api_client, host_object):

    ipdb.set_trace()
    obj_type = "host"

    # Check if host already exists
    object_exists = False
    payload = {"name": host_object["name"]}
    api_res = api_client.api_call(command=f"show-{obj_type}", payload=payload)

    if api_res.success:
        object_exists = True

    if object_exists:
        # Object already exists, update parameters
        print(f"Updating {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"set-{obj_type}", payload=host_object)
    else:
        print(f"Configuring {obj_type} object: {host_object}")
        api_res = api_client.api_call(command=f"add-{obj_type}", payload=host_object)

    if not api_res.success:
        msg = f"Failed to configure {obj_type} object: {host_object}"
        raise ChkPntConfigError(msg)
