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

        api_endpoint = "show-services-tcp"
        api_res = api_client.api_call(api_endpoint)

        tcp_services = api_res.data["objects"]
        print(len(tcp_services))

        tcp_services_total = api_res.data["total"]
        tcp_services_from = api_res.data["from"]
        tcp_services_to = api_res.data["to"]

        print(f"{tcp_services_total=}")
        print(f"{tcp_services_from=}")
        print(f"{tcp_services_to=}")

        api_res = api_client.api_query(api_endpoint, details_level="standard")
        ipdb.set_trace()
        # print(api_res)

        # No more "objects" / "total" / "from" / "to" keys--just a list.
        tcp_services = api_res.data
        print(f"\nServices returned: {len(tcp_services)}\n")


if __name__ == "__main__":
    main()
