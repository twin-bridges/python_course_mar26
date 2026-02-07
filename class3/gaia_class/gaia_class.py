import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class GaiaAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class GaiaLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class GaiaAPI:
    def __init__(self, host, username, password, api_version="1.8", ssl_verify=False):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/gaia_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.ssl_verify = ssl_verify

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
            msg = "Failed to 'logout' from Gaia API"
            raise GaiaLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise GaiaAuthError(msg)

        response = requests.post(
            url, data=json.dumps(payload), headers=self.headers, verify=self.ssl_verify
        )
        return response


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    api_client = GaiaAPI(host=host, username=user, password=admin_pass)
    api_client.login()

    res = api_client.call(endpoint="show-version")
    print(res.json())

    api_client.logout()
