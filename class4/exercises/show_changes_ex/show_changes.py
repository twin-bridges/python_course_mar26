import os
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs
from datetime import datetime, timedelta, timezone
import ipdb  # noqa


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

        now = datetime.now(timezone.utc)
        two_days_ago = now - timedelta(hours=48)

        # ISO 8601
        from_date = two_days_ago.strftime('%Y-%m-%dT%H:%M:%S')
        to_date = now.strftime('%Y-%m-%dT%H:%M:%S')

        payload = {"from-date": from_date, "to-date": to_date}

        api_res = api_client.api_call(command="show-changes", payload=payload)
        print(api_res)

        changes = api_res.data['tasks'][0]['task-details'][0]['changes']
        for change in changes:
            operations = change['operations']
            added = operations['added-objects']
            modified = operations['modified-objects']
            deleted = operations['deleted-objects']
            if added:
                print(added)
            if modified:
                print(modified)
            if deleted:
                print(deleted)
            ipdb.set_trace()

        print(changes)


if __name__ == "__main__":
    main()
