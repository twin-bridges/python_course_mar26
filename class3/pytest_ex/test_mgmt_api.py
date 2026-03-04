import ipdb  # noqa
from rich import print  # noqa


def test_blocked_ips_group(web_api_session):
    # api_session is the logged-in client object from the fixture
    endpoint = "show-group"
    payload = {"name": "Blocked IPs"}
    response = web_api_session.api_call(endpoint, payload=payload)

    assert response.success is True

    group_name = response.data["name"]
    assert "Blocked IPs" == group_name

    # Membership check
    members = response.data["members"]
    assert len(members) == 10


def test_host_objects(web_api_session):
    minimum_host_objects = 10
    endpoint = "show-hosts"
    response = web_api_session.api_call(endpoint)

    host_objects = response.data["objects"]
    assert len(host_objects) >= minimum_host_objects


def test_ansible_host(web_api_session):
    host_name = "Ansible Server"
    ip_addr = "3.125.34.232"

    endpoint = "show-host"
    payload = {"name": host_name}
    response = web_api_session.api_call(endpoint, payload=payload)

    host_obj = response.data
    ipv4_addr = host_obj["ipv4-address"]

    assert host_name == host_obj["name"]
    assert ip_addr == ipv4_addr
