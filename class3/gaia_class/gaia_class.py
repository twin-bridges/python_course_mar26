import requests
import os
import json

# from rich import print
from dotenv import load_dotenv
import ipdb  # noqa


class GaiaAPI:
    def __init__(self, host, username, password, api_version="1.8", ssl_verify=False):
        self.host = host
        self.username = username
        self.password = password
        self.base_url = f"https://{host}/gaia_api/v{api_version}/"
        self.ssl_verify = ssl_verify

    def login(self):
        headers = {"Content-Type": "application/json"}
        login_payload = {"user": self.username, "password": self.password}
        url = self.base_url + "login"
        response = requests.post(
            url, data=json.dumps(login_payload), headers=headers, verify=self.ssl_verify
        )
        resp_struct = response.json()
        self.session_id = resp_struct["sid"]


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]


#    headers["X-chkp-sid"] = session_id
#    print(headers)
#
#    #endpoint = "show-version"
#    endpoint = "show-api-versions"
#    url = f"{base_url}{endpoint}"
#    payload = {}
#
#    print(url)
#    response = requests.post(
#        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
#    )
#    print(response.json())
#    ipdb.set_trace()
#
#    endpoint = "logout"
#    url = f"{base_url}{endpoint}"
#    payload = {}
#
#    response = requests.post(
#        url, data=json.dumps(payload), headers=headers, verify=ssl_verify
#    )
#    print(response)
