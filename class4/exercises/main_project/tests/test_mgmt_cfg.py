import ipdb  # noqa
from rich import print  # noqa
from host_objects import smart_console_private, smart_console_public, ansible_server

def test_host_objects(mgmt_api):

    api_client = mgmt_api
    api_endpoint = "show-host"

    mgmt_host_objects = [smart_console_private, smart_console_public, ansible_server]

    for host_obj in mgmt_host_objects:
        payload = {"name": host_obj["name"]}
        api_res = api_client.api_call(command=api_endpoint, payload=payload)
        assert api_res.success is True
        assert api_res.data["name"] == host_obj["name"]
        assert api_res.data["ipv4-address"] == host_obj["ipv4-address"]

