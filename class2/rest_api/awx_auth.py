import requests
import os
import ipdb  # noqa
from dotenv import load_dotenv

awx_host = "54.241.198.61:32309/#/login"
port = "32309"
base_url = f"http://{awx_host}:{port}"
token_auth_url = f"{base_url}/api/v2/tokens/"

# This looks for a .env file and loads it
load_dotenv()
user = "admin"
admin_pass = os.environ["CHKP_ADMIN"]
creds = (user, admin_pass)

res = requests.post(
    token_auth_url, auth=creds, json={"description": "Testing auth"}, verify=False
)
ipdb.set_trace()
print(res)
