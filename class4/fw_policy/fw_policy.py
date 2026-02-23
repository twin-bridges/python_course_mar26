import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_fw_policy(api_client):
    """Use mgmt API to configure firewall policy rules."""

    fw_name = "chkpnt-pod99"
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

    for fw_rule in management_rules:
        ipdb.set_trace()

        # Check if fw_rule already exists
        obj_exists = False
        payload = {"layer": fw_rule["layer"], "name": fw_rule["name"]}
        api_res = api_client.api_call(command="show-access-rule", payload=payload)
        # api_res = api_client.api_call(command="show-access-rulebase", payload=payload)

        # fw_rules = api_res.data['rulebase']
        # print(fw_rules)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            print(f"Updating firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="set-access-rule", payload=fw_rule)
        else:
            print(f"Configuring firewall rule: {fw_rule}")
            api_res = api_client.api_call(command="add-access-rule", payload=fw_rule)

        if not api_res.success:
            msg = f"Failed to configure firewall rule: {fw_rule}"
            raise ChkPntConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"
    fw_name = "chkpnt-pod99"

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
        cfg_fw_policy(api_client)
        api_client.api_call(command="publish")
        payload = {"policy-package": "Standard", "targets": [fw_name]}
        api_client.api_call(command="install-policy", payload=payload)


if __name__ == "__main__":
    main()
