import os
from rich import print
from dotenv import load_dotenv
from gaia_auth_ex import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "1.8"
    base_url = f"https://{host}/gaia_api/v{api_version}/"

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    response = login(base_url, user, admin_pass)
    resp_struct = response.json()
    session_id = resp_struct["sid"]

    headers = {"Content-Type": "application/json"}
    headers["X-chkp-sid"] = session_id

    # Gather and display dynamic ARP data
    endpoint = "show-arp"
    arp_response = api_call(base_url, endpoint, headers)
    arp_table = arp_response.json()
    dynamic_arp = arp_table["dynamic"]

    print()
    for arp_entry in dynamic_arp:
        ip_addr = arp_entry['ipv4-address']
        mac_addr = arp_entry['mac-address']
        print(f"{ip_addr} -> {mac_addr}")
    print()

    logout(base_url, headers)
