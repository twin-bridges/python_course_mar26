import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"

    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=True, context="web_api"
    )
    with APIClient(client_args) as api_client:
        res = api_client.login(username, password)
        print(res)

        # api_endpoint = "show-hosts"
        api_endpoint = "show-networks"
        api_args = {}
        api_res = api_client.api_call(api_endpoint, api_args)
        print(api_res)


if __name__ == "__main__":
    main()
