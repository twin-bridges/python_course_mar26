import requests
import os
import ipdb  # noqa
from dotenv import load_dotenv

awx_host = "54.241.198.61"
port = "32309"
base_url = f"http://{awx_host}:{port}/api/v2/"
token_auth_url = f"{base_url}tokens/"

# This looks for a .env file and loads it
load_dotenv()
user = "admin"
admin_pass = os.environ["AWX_ADMIN"]
creds = (user, admin_pass)

res = requests.post(
    token_auth_url, auth=creds, json={"description": "Testing auth"}, verify=False
)
json_resp = res.json()
token = json_resp["token"]

headers = {"Authorization": f"Bearer {token}"}
base_url = f"http://{awx_host}:{port}/api/v2/"
endpoint = "projects/"
url = f"{base_url}{endpoint}"

res = requests.get(url, headers=headers, verify=False)
ipdb.set_trace()
print(res)
print(res.json())
