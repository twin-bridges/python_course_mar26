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
        query = api_client.gen_api_query(api_endpoint, details_level="standard")

        # Retrieve pages of data
        for chunk in query:
            ipdb.set_trace()
            # print(chunk)

            tcp_services = chunk.data["objects"]
            print(len(tcp_services))

            # tcp_services_total = api_res.data["total"]
            # tcp_services_from = api_res.data["from"]
            # tcp_services_to = api_res.data["to"]

            # print(f"{tcp_services_total=}")
            # print(f"{tcp_services_from=}")
            # print(f"{tcp_services_to=}")


if __name__ == "__main__":
    main()
