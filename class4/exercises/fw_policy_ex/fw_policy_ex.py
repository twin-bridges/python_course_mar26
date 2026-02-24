import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from fw_policy_funcs import (
    cfg_fw_policy,
    install_fw_policy,
    display_fw_policy,
    extract_fw_name,
)
from rich import print  # noqa
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    #  8     - name: Add Corp Web Server
    #  9       check_point.mgmt.cp_mgmt_host:
    # 10         name: Corp Web Server
    # 11         ipv4_address: 172.31.144.220
    # 12         color: dark green
    # 13       notify: Publish

    fw_name = extract_fw_name(host)
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

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="web_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        ipdb.set_trace()
        cfg_fw_policy(api_client, fw_rules=management_rules)
        api_client.api_call(command="publish")

        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
