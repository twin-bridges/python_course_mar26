import requests
import json
from rich import print  # noqa
import ipdb  # noqa


class ChkptAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class ChkptLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class ChkptAPI:
    def __init__(
        self,
        host,
        username,
        password,
        mode="web_api",
        api_version=None,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password

        if api_version is None:
            if mode == "web_api":
                api_version = "2"
            elif mode == "gaia_api":
                api_version = "1.8"

        self.ssl_verify = ssl_verify
        self.headers = {"Content-Type": "application/json"}
        self.base_url = f"https://{host}/{mode}/v{api_version}/"

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Check Point API"
            raise ChkptLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise ChkptAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response
