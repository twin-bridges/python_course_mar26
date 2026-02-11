import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


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

        # DNS
        payload = {
            "name": "hq_net_128",
            "subnet": "172.31.128.0",
            "mask-length": 24,
            "color": "green",
        }
        api_res = api_client.api_call(command="add-network", payload=payload)
        print(api_res)
        api_res = api_client.api_call(command="publish")
        print(api_res)
        api_res = api_client.api_call(command="show-networks")
        print(api_res)


if __name__ == "__main__":
    main()
