import requests
import os
import json
from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class MgmtAuthError(Exception):
    """Exception raised when the session ID is missing or expired."""

    pass


class MgmtLogoutError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class MgmtPublishError(Exception):
    """Raised when the API returns a failure during the logout process."""

    pass


class MgmtAPI:
    def __init__(
        self,
        host,
        username,
        password,
        api_version="2",
        read_only=False,
        ssl_verify=False,
    ):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/web_api/v{api_version}/"
        self.headers = {"Content-Type": "application/json"}
        self.read_only = False
        self.ssl_verify = ssl_verify

    def login(self):
        login_payload = {"user": self.username, "password": self.password}
        if self.read_only:
            # Less overhead if read-only
            login_payload["enter-last-published-session"] = True
        url = self.base_url + "login"
        response = requests.post(
            url,
            data=json.dumps(login_payload),
            headers=self.headers,
            verify=self.ssl_verify,
        )
        resp_struct = response.json()
        print(resp_struct)
        self.headers["X-chkp-sid"] = resp_struct["sid"]

    def publish(self):
        endpoint = "publish"
        res = self.call(endpoint)
        if res.status_code != 200:
            msg = "Publish operation failed!"
            raise MgmtPublishError(msg)

    def logout(self):
        endpoint = "logout"
        res = self.call(endpoint)
        if res.status_code == 200:
            msg = res.json()["message"]
        if res.status_code == 200 and msg == "OK":
            if "X-chkp-sid" in self.headers:
                self.headers.pop("X-chkp-sid")
        else:
            msg = "Failed to 'logout' from Mgmt API"
            raise MgmtLogoutError(msg)

    def call(self, endpoint, payload=None):
        url = self.base_url + endpoint
        if payload is None:
            payload = {}
        if "X-chkp-sid" not in self.headers:
            msg = """
Session ID not set, please call '.login()' method and properly 
authenticate to the API.
"""
            raise MgmtAuthError(msg)

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

    api_client = MgmtAPI(host=host, username=user, password=admin_pass, read_only=True)
    api_client.login()

    payload = {
        "name": "hq_net_128",
        "subnet": "172.31.128.0",
        "mask-length": 24,
        "color": "green",
    }
    api_client.call(endpoint="add-network", payload=payload)
    api_client.publish()
    res = api_client.call(endpoint="show-networks")
    print(res.json())

    api_client.logout()
