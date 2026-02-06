import requests
import os
import ipdb  # noqa
from dotenv import load_dotenv
# from rich import print

awx_host = "54.241.198.61"
port = "32309"
base_url = f"http://{awx_host}:{port}/api/v2/"
url = f"{base_url}tokens/"

# This looks for a .env file and loads it
load_dotenv()
user = "admin"
admin_pass = os.environ["AWX_ADMIN"]
creds = (user, admin_pass)

test_url = f"http://awx_host.lasthop.io:{port}/api/v2/"
print(f"\n{test_url}\n")

res = requests.post(url, auth=creds, json={"description": "Testing auth"}, verify=False)
json_resp = res.json()
token = json_resp["token"]
print(url)
print(res)

# Retrieve some data using existing token
headers = {"Authorization": f"Bearer {token}"}
endpoint = "projects/"
url = f"{base_url}{endpoint}"

res = requests.get(url, headers=headers, verify=False)
print(url)
print(res)

# Delete the token
endpoint = f"tokens/{token}/"
url = f"{base_url}{endpoint}"
requests.delete(url, headers=headers, verify=False)
print(url)
print(res)
