import os
import sys
import ipdb  # noqa
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from chkpt_object_funcs import cfg_host_objects, cfg_group_object, delete_host_objects
from blocked_ip_funcs import (
    read_blocked_ips_file,
    gen_host_object,
    get_current_blocked_ips,
)


def cfg_blocked_ips(api_client):
    """
    Configure 'Blocked IPs' from blocked_ips.txt file.

    Add new blocked IP host objects
    Upgraded 'Blocked IPs' group membership
    Remove obsolete blocked IP host objects
    """

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
    delete_ip_objs = [gen_host_object(ip) for ip in remove_blocked_ips]

    # Configure host objects for blocked IPs
    cfg_host_objects(api_client, blocked_ip_objs)

    # Update group membership
    blocked_ip_group = {
        "name": "Blocked IPs",
        "members": new_blocked_ips,
    }
    cfg_group_object(api_client, blocked_ip_group)

    # Remove unused host objects (must come after group membership update)
    delete_host_objects(api_client, delete_ip_objs)


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

        cfg_blocked_ips(api_client)

        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
