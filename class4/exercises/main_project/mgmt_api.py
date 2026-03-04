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
from chkpt_policy_funcs import cfg_fw_rules, install_fw_policy, extract_fw_name


def cfg_mgmt_fw_rules(api_client, fw_name):
    management_rules = [
        {
            "layer": "Network",
            "name": "Ansible Management Access",
            "source": [
                "Ansible Server",
                "Windows SmartConsole",
                "Windows SmartConsole Public",
            ],
            "destination": fw_name,
            "service": "Any",
            "action": "Accept",
            "position": 1,
        },
        {
            "layer": "Network",
            "name": "SSH Access",
            "source": "Any",
            "destination": fw_name,
            "service": "SSH",
            "action": "Accept",
            "position": 2,
        },
    ]
    cfg_fw_rules(api_client, fw_rules=management_rules)


def cfg_std_mgmt_hosts(api_client):
    smart_console_private = {
        "name": "Windows SmartConsole",
        "ipv4-address": "172.31.12.101",
        "color": "red",
    }
    smart_console_public = {
        "name": "Windows SmartConsole Public",
        "ipv4-address": "3.71.9.240",
        "color": "red",
    }
    ansible_server = {
        "name": "Ansible Server",
        "ipv4-address": "3.125.34.232",
        "color": "black",
    }

    mgmt_host_objects = [smart_console_private, smart_console_public, ansible_server]
    cfg_host_objects(api_client, host_objects=mgmt_host_objects)


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
    fw_name = extract_fw_name(host)

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
        cfg_std_mgmt_hosts(api_client)
        cfg_mgmt_fw_rules(api_client, fw_name)

        api_client.api_call(command="publish")

        install_fw_policy(api_client, targets=fw_name)


if __name__ == "__main__":
    main()
