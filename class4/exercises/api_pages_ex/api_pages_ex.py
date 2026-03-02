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

        udp_services = []
        offset = 0
        while True:
            api_endpoint = "show-services-udp"
            payload = {"offset": offset}
            api_res = api_client.api_call(api_endpoint, payload)

            udp_services = udp_services + api_res.data["objects"]

            udp_services_from = api_res.data["from"]
            udp_services_to = api_res.data["to"]
            udp_services_total = api_res.data["total"]
            print(f"{udp_services_from=}")
            print(f"{udp_services_to=}")
            print(f"{udp_services_total=}")

            offset = udp_services_to
            # Keep retrieving data until all have been retrieved
            if len(udp_services) >= udp_services_total:
                break

        print(len(udp_services))
        # print(udp_services)


if __name__ == "__main__":
    main()
