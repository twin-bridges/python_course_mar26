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
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # DNS
        payload = {
            "primary": "172.31.0.2",
            "secondary": "8.8.8.8",
            "tertiary": "8.8.4.4",
            "suffix": "lasthop.io",
        }

        api_endpoint = "set-dns"
        api_res = api_client.api_call(command=api_endpoint, payload=payload)
        print(api_res)

        api_res = api_client.api_call(command="show-dns")
        print(api_res)


if __name__ == "__main__":
    main()
