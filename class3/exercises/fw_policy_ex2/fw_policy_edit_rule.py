# Edit an existing firewall rule
import os
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from fw_policy_funcs import (
    cfg_fw_rule,
    install_fw_policy,
    display_fw_policy,
)
from object_funcs import cfg_host_object
from rich import print  # noqa
import ipdb  # noqa


def main():
    host = "chkpnt-pod99.lasthop.io"

    corp_web_server = {
        "name": "Corp Web Server",
        "ipv4-address": "172.31.144.220",
        "color": "dark green",
    }

    corp_fw_rule = {
        "layer": "Network",
        "name": "Corp Web Server Access",
        "source": "Any",
        "destination": "Corp Web Server",
        "service": ["http", "https", "ssh"],
        "action": "Accept",
        "position": 1,
        "comments": "Test rule for Python training session",
    }

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
        cfg_host_object(api_client, corp_web_server)
        cfg_fw_rule(api_client, fw_rule=corp_fw_rule)
        api_client.api_call(command="publish")
        install_fw_policy(api_client)
        display_fw_policy(api_client)


if __name__ == "__main__":
    main()
