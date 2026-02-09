import requests
import json


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
