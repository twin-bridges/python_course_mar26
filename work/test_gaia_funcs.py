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

    url = base_url + "show-connections" # No
    url = base_url + "show-arp" # Yes
    url = base_url + "show-allowed-clients" # Yes
    url = base_url + "show-nat-pools" # No
    url = base_url + "show-cluster-state" # No
    url = base_url + "show-cluster-members" # No
    url = base_url + "show-param" # No
    # url = base_url + "set-initial-setup" # Looks very interesting
    # url = base_url + "run-reboot" # Looks interesting
    url = base_url + "show-serial-number" # Yes
    url = base_url + "show-asset" # Yes
    url = base_url + "show-diagnostics" # Looks interesting / requires payload
    # add-secheduled-job / set- / show- / Looks very interesting
    # lightshot -- Lightweight snapshot
    # scheduled backups
    # scheduled snapshots
    # custom intelligence feeds
    # user management
    # run-script    / Definitely do this!!!
    # Interfaces
    # Licensing
    

    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
