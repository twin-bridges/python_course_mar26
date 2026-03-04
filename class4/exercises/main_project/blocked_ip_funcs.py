import ipdb  # noqa
from rich import print  # noqa


def read_blocked_ips_file():
    # Retrieve the 'new' blocked IPs
    with open("blocked_ips.txt") as f:
        new_blocked_ips = f.readlines()
        # strip trailing newline w/ list comprehension
        new_blocked_ips = [ip.strip() for ip in new_blocked_ips]
        return new_blocked_ips


def gen_host_object(ip_addr):
    return {
        "name": ip_addr,
        "ipv4-address": ip_addr,
        "color": "black",
    }


def get_current_blocked_ips(api_client, group_name):
    """Retrieve current Blocked IPs group membership."""
    current_blocked_ips = []
    api_res = api_client.api_call(command="show-group", payload={"name": group_name})
    if api_res.success:
        current_blocked_ips = api_res.data["members"]

    # Retrieve only names / use list comprehension
    cur_blocked_ip_names = [bl_obj["name"] for bl_obj in current_blocked_ips]
    return cur_blocked_ip_names
