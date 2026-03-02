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
        api_client.login(username, password)

        api_endpoint = "show-services-udp"
        api_res = api_client.api_query(api_endpoint, details_level="standard")

        # No more "objects" / "total" / "from" / "to" keys--just a list.
        # Retrieve all 96 services using api_query
        udp_services = api_res.data
        print(f"\nServices returned: {len(udp_services)}\n")


if __name__ == "__main__":
    main()
