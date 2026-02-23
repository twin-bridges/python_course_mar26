#
# show physical interface.py
# version 1.0
#
# The purpose of this script is to show a server's physical interfaces
#
# written by: Check Point software technologies inc.
# April 2019
# modified by: Kirk Byers (Feb 2026)

import os
import sys
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs



def main():
    api_server = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"

    client_args = APIClientArgs(
        server="chkpnt-pod99.lasthop.io", 
        api_version="1.8", 
        unsafe=True, 
        context="gaia_api"
    )

    with APIClient(client_args) as client:
        login_res = client.login(username, password)
        if login_res.success is False:
            print(f"Login failed: {login_res.error_message}")
            sys.exit(1)

        interface_name = input("Enter interface name: ")
        api_endpoint = "show-physical-interface"
        api_args = {"name": interface_name}
        api_res = client.api_call(api_endpoint, api_args)
        if api_res.success:
            intf_name = api_res.data["name"]
            ip_addr = (api_res.data["ipv4-address"],)
            mtu = (api_res.data["mtu"],)
            resp = f"""
Physical interface name is '{intf_name}' , ipv4 address is '{ip_addr}', 
interface mtu is '{mtu}' 
"""
            print(resp)
        else:
            print(f"Failed to get physical interface data '{api_res.data}'")


if __name__ == "__main__":
    main()
