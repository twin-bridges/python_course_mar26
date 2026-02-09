import os
from rich import print
from dotenv import load_dotenv
from gaia_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    endpoint = "login"
    base_url = f"https://{host}/gaia_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    url = base_url + "show-version"
    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
