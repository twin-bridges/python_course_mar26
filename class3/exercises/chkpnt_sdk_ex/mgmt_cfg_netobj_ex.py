import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
import ipdb  # noqa


class ChkPntConfigError(Exception):
    pass


def cfg_net_objects(api_client):
    """Use mgmt API to configure network objects."""
    hq_net_128 = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
    }
    hq_net_129 = {
        "name": "hq_net_129",
        "subnet": "172.31.129.0",
    }
    hq_net_130 = {
        "name": "hq_net_130",
        "subnet": "172.31.130.0",
    }
    hq_net_131 = {
        "name": "hq_net_131",
        "subnet": "172.31.131.0",
    }
    hq_net_132 = {
        "name": "hq_net_132",
        "subnet": "172.31.132.0",
    }
    hq_net_133 = {
        "name": "hq_net_133",
        "subnet": "172.31.133.0",
    }
    hq_net_134 = {
        "name": "hq_net_134",
        "subnet": "172.31.134.0",
    }
    hq_net_135 = {
        "name": "hq_net_135",
        "subnet": "172.31.135.0",
    }

    for params in (
        hq_net_128,
        hq_net_129,
        hq_net_130,
        hq_net_131,
        hq_net_132,
        hq_net_133,
        hq_net_134,
        hq_net_135,
    ):
        # Set common params
        params["mask-length"] = 24
        params["color"] = "green"

        ipdb.set_trace()
        # Check if object already exists
        obj_exists = False
        payload = {"name": params["name"]}
        api_res = api_client.api_call(command="show-network", payload=payload)

        if api_res.success:
            obj_exists = True
        if obj_exists:
            # object already exists, update parameters
            print(f"Updating object: {params}")
            api_res = api_client.api_call(command="set-network", payload=params)
        else:
            print(f"Configuring object: {params}")
            api_res = api_client.api_call(command="add-network", payload=params)

        if not api_res.success:
            msg = f"Failed to configure object: {params}"
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
        cfg_net_objects(api_client)
        api_client.api_call(command="publish")


if __name__ == "__main__":
    main()
