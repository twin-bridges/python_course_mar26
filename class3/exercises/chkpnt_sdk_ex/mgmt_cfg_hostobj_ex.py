import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb # noqa

class ChkPntConfigError(Exception):
    pass

def cfg_host_objects(api_client):
    """Use mgmt API to configure Ansible and SmartConsole host objects."""
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
    for host_params in (smart_console_private, smart_console_public, ansible_server):

        # Check if host already exists
        # ipdb.set_trace()
        host_exists = False
        host_name = host_params["name"]
        payload = {"name": host_name}
        api_res = api_client.api_call(command="show-host", payload=payload)

        if api_res.success:
            host_exists = True
        if host_exists:
            # Host already exists, update parameters
            print(f"Updating host object: {host_params}")
            api_res = api_client.api_call(command="set-host", payload=host_params)
        else:
            print(f"Configuring host object: {host_params}")
            api_res = api_client.api_call(command="add-host", payload=host_params)

        if not api_res.success:
            msg = f"Failed to configure host object: {host_params}"
            raise ChkPntConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

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
        cfg_host_objects(api_client)
        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
