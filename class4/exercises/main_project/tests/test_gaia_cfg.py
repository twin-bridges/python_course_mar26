import ipdb  # noqa
from rich import print  # noqa


def test_dns_config(gaia_api):

    api_client = gaia_api

    api_endpoint = "show-dns"
    api_res = api_client.api_call(command=api_endpoint)

    assert api_res.success is True
    dns_dict = api_res.data
    pri_dns = dns_dict["primary"]
    sec_dns = dns_dict["secondary"]
    ter_dns = dns_dict["tertiary"]
    suffix = dns_dict["suffix"]

    assert pri_dns == "172.31.0.2"
    assert sec_dns == "8.8.8.8"
    assert ter_dns == "8.8.4.4"
    assert suffix == "lasthop.io"


def test_static_route_cfg(gaia_api):

    api_client = gaia_api

    api_endpoint = "show-static-route"
    payload = {
        "address": "172.31.128.0",
        "mask-length": 21,
    }
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    assert api_res.success is True

    static_route = api_res.data
    network = static_route['address']
    mask = static_route['mask-length']
    next_hop_dict = static_route['next-hop'][0]
    next_hop = next_hop_dict['gateway']
    gw_type = static_route['type']

    assert network == '172.31.128.0'
    assert mask == 21
    assert next_hop == '172.31.128.1'
    assert gw_type == 'gateway'
