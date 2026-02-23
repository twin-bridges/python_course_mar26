import os
from rich import print
from dotenv import load_dotenv
from mgmt_funcs import login, api_call, logout


if __name__ == "__main__":
    host = "chkpnt-pod99.lasthop.io"
    api_version = "2"
    endpoint = "login"
    base_url = f"https://{host}/web_api/v{api_version}/"
    headers = {"Content-Type": "application/json"}

    # This looks for a .env file and loads it
    load_dotenv()
    user = "admin"
    admin_pass = os.environ["CHKP_ADMIN"]

    # Login
    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    headers["X-chkp-sid"] = session_id

    endpoint = "show-gateway-capabilities"
    url = base_url + endpoint
    res = api_call(url, headers)
    capabilities = res.json()

    supported_os_versions = capabilities["supported-versions"]["versions"]
    r81_supported_versions = []
    for os_version in supported_os_versions:
        if "R81" in os_version:
            r81_supported_versions.append(os_version)

    supported_hw = capabilities["supported-hardware"]["hardware"]
    supported_hw_lightspeed = []
    for hardware in supported_hw:
        if "lightspeed" in hardware.lower():
            supported_hw_lightspeed.append(hardware)

    print("\nR81 Supported OS Versions: ")
    print("-" * 20)
    print(r81_supported_versions)
    print()

    print("\nLightSpeed Supported Hardware: ")
    print("-" * 20)
    print(supported_hw_lightspeed)
    print()

    # Logout
    url = base_url + "logout"
    headers = logout(url, headers)
