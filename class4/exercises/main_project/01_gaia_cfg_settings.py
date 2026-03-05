import os
import ipdb  # noqa
from rich import print  # noqa
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


class GaiaConfigError(Exception):
    pass


def config_dns(api_client):

    # DNS
    payload = {
        "primary": "172.31.0.2",
        "secondary": "8.8.8.8",
        "tertiary": "8.8.4.4",
        "suffix": "lasthop.io",
    }

    api_endpoint = "set-dns"
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    if not api_res.success:
        msg = f"{api_endpoint} configuration failed. "
        if hasattr(api_res, "data"):
            msg += api_res.data["errors"]
        raise GaiaConfigError(msg)


def config_static_route(api_client):

    payload = {
        "address": "172.31.128.0",
        "mask-length": 28,
        "next-hop": [{"gateway": "172.31.128.1", "priority": "default"}],
        "type": "gateway",
    }

    api_endpoint = "set-static-route"
    api_res = api_client.api_call(command=api_endpoint, payload=payload)
    if not api_res.success:
        msg = f"{api_endpoint} configuration failed. "
        if hasattr(api_res, "data"):
            msg += api_res.data["errors"]
        raise GaiaConfigError(msg)


def main():
    host = "chkpnt-pod99.lasthop.io"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)
        print("[green][Gaia Config][/green] Configure DNS Settings")
        config_dns(api_client)
        print("[green][Gaia Config][/green] Configure Static Route")
        config_static_route(api_client)


if __name__ == "__main__":
    main()
