import os
import base64
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def main():
    host = "chkpnt-pod99.lasthop.io"
    fw_name = "chkpnt-pod99"

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

        payload = {
            # "script": "ls -al"
            # "script": "cat None"
            # "script": "fw stat"
            # "script": "cphaprob state"
            # "script": "cpstat os -f memory"
            "script": 'clish -c "show interfaces"',
            "script-name": "Testing Python Automation",
            "targets": [fw_name],
        }

        api_endpoint = "run-script"
        api_res = api_client.api_call(command=api_endpoint, payload=payload)

        if api_res.success:
            tasks = api_res.data["tasks"]
            for task in tasks:
                if task["status"] == "succeeded":
                    b64_result = task["task-details"][0]["responseMessage"]
                    bytes_str = base64.b64decode(b64_result)
                    data_str = bytes_str.decode("utf-8")
                    print(data_str)


if __name__ == "__main__":
    main()
