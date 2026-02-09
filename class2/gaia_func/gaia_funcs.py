import requests
import os
import json
from rich import print

from dotenv import load_dotenv
import ipdb  # noqa

API_VERSION = 1.8
HEADERS = {"Content-Type": "application/json"}


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


def login(url, username, password):
    """Login and return the session_id."""
    headers = {"Content-Type": "application/json"}
    ssl_verify = False
    login_payload = {"user": username, "password": password}

    response = requests.post(
        url,
        data=json.dumps(login_payload),
        headers=headers,
        verify=ssl_verify,
    )
    resp_struct = response.json()
    return resp_struct["sid"]


def api_call(url, headers, payload=None, ssl_verify=False):
    if payload is None:
        payload = {}
    if "X-chkp-sid" not in headers:
        msg = """
Session ID not set, please call '.login()' method and properly
authenticate to the API.
"""
        raise GaiaAuthError(msg)

    response = requests.post(
        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
    )
    return response


def logout(url, headers):
    """Removes 'X-chkp-sid' from headers and returns headers dict."""
    res = api_call(url, headers)
    if res.status_code == 200:
        msg = res.json()["message"]
    if res.status_code == 200 and msg == "OK":
        if "X-chkp-sid" in headers:
            headers.pop("X-chkp-sid")
            return headers
    else:
        msg = "Failed to 'logout' from Gaia API"
        raise GaiaLogoutError(msg)


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"
    base_url = f"https://{host}/gaia_api/v{API_VERSION}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(session_id)

    headers["X-chkp-sid"] = session_id

    url = base_url + "show-version"
    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
