import os
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from chkpt_object_funcs import cfg_host_objects
from chkpt_policy_funcs import cfg_fw_rules, install_fw_policy, extract_fw_name
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"
    fw_name = extract_fw_name(host)

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "2"
    no_ssl_verify = True

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

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        cfg_host_objects(api_client, host_objects=mgmt_host_objects)
        cfg_fw_rules(api_client, fw_rules=management_rules)

        api_client.api_call(command="publish")
        install_fw_policy(api_client, targets=fw_name)


if __name__ == "__main__":
    main()
