import ipdb  # noqa
from rich import print  # noqa
from host_objects import smart_console_private, smart_console_public, ansible_server
from chkpt_policy_funcs import extract_fw_name
from gen_fw_rules import gen_blockedip_fw_rules, gen_mgmt_fw_rules

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

def test_blocked_ips_group(mgmt_api):

    api_client = mgmt_api
    api_endpoint = "show-group"

    group_name = "Blocked IPs"
    payload = {"name": group_name}
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    assert api_res.success is True
    assert group_name == api_res.data["name"]
    members = api_res.data["members"]
    assert len(members) == 10

def test_firewall_rules(mgmt_api):
    api_client = mgmt_api
    fw_name = extract_fw_name(api_client.server)

    fw_rules = gen_mgmt_fw_rules(fw_name) + gen_blockedip_fw_rules()
    print(fw_rules)
