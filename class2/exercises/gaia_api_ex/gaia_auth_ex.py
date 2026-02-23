import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


def login(base_url, user, password, ssl_verify=False):

    url = base_url + "login"
    headers = {"Content-Type": "application/json"}
    login_payload = {"user": user, "password": password}

    response = requests.post(
        url, data=json.dumps(login_payload), headers=headers, verify=ssl_verify
    )
    return response


def api_call(base_url, endpoint, headers, payload=None, ssl_verify=False):

    if payload is None:
        payload = {}
    url = base_url + endpoint
    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(base_url, headers, ssl_verify=False):

    # Call 'logout'
    endpoint = "logout"
    response = api_call(base_url, endpoint, headers, ssl_verify=ssl_verify)
    # If successful, remove the session ID from the headers
    if response.status_code == 200:
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")

    return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/v{api_version}/"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    response = login(base_url, user, admin_pass)
    resp_struct = response.json()
    session_id = resp_struct["sid"]

    headers = {"Content-Type": "application/json"}
    headers["X-chkp-sid"] = session_id

    endpoint = "show-api-versions"
    response = api_call(base_url, endpoint, headers)
    print(response.json())

    logout(base_url, headers)
