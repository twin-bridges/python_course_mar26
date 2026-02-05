import requests
import os
from dotenv import load_dotenv

if __name__ == "__main__":

    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/"
    endpoint = "login"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = f"{base_url}/{endpoint}"
    headers = {"Content-Type": "application/json"}
    login_payload = {"user": user, "password": admin_pass}
    ssl_verify = False

    # CheckPoint uses POST even for information retrieval operations
    response = requests.post(
        url, data=json.dumps(login_payload), headers=headers, verify=ssl_verify
    )

