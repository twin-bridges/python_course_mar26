import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs

def check_users(api_client):
    api_endpoint = "show-users"
    api_res = api_client.api_call(command=api_endpoint)

    users = api_res.data["objects"]

    audit_users = []
    for user in users:
        username = user["name"]
        # user_roles = user["roles"]
        audit_users.append(username)


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

        ipdb.set_trace()
        api_endpoint = "show-password-policy"
        api_res = api_client.api_call(command=api_endpoint)

        # Checks
        check_users = {"admin", "monitor"}

        print()
        print("User checks...", end="")
        audit_users = set(audit_users)
        if audit_users == check_users:
            print("[green]pass[/green]")
        else:
            print("[red]fail[/red]")


if __name__ == "__main__":
    main()
