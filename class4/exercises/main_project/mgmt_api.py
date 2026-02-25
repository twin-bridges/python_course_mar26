import os
import sys
import ipdb  # noqa
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from chkpt_object_funcs import cfg_host_objects, cfg_group_object


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


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        group_name = "Blocked IPs"
        current_blocked_ips = get_current_blocked_ips(api_client, group_name)
        new_blocked_ips = read_blocked_ips_file()

        # Compare new versus currently configured blocked IPs
        if set(current_blocked_ips) == set(new_blocked_ips):
            # Nothing to do, current and new already match.
            sys.exit(0)
        else:
            add_blocked_ips = set(new_blocked_ips) - set(current_blocked_ips)
            remove_blocked_ips = set(current_blocked_ips) - set(new_blocked_ips)
            print(f"{add_blocked_ips=}")
            print(f"{remove_blocked_ips=}")

        # Convert to host object dict using list comprehension
        blocked_ip_objs = [gen_host_object(ip) for ip in add_blocked_ips]

        # Configure host objects for blocked IPs
        cfg_host_objects(api_client, blocked_ip_objs)

        # Update group membership
        blocked_ip_group = {
            "name": "Blocked IPs",
            "members": new_blocked_ips,
        }
        cfg_group_object(api_client, blocked_ip_group)

        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
