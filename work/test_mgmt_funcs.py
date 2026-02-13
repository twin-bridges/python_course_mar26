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

    url = base_url + "login"
    session_id = login(url=url, username=user, password=admin_pass)
    print(f"{session_id=}")

    headers["X-chkp-sid"] = session_id

    # url = base_url + "show-networks"
    # revert-to-revision
    # show-session
    # show-sessions
    # show-list-published-session
    # assign session ownershipa
    # take over session
    # switch session    # looks interesting
    url = base_url + "show-session"
    # show-login-message
    # set-login-message
    # show-gateway-capabilities
    # Services / Applications
    # Access Rule
    # NAT
    # Threat prevention(?)
    # HTTPS Inspection / Rule
    # Policy / install-policy & verify-policy
    # Multi domain
    # Smart Tasks
    # Repository scripts?
        # You can create python repository scripts | this could be interesting
    # Package deployment -- sounds interesting
    url = base_url + "show-repository-packages"
    #url = base_url + "show-task"
    #payload = {
    #    "task-id": "37b26077-b9bb-40c7-a522-45ad0bee23c3",
    #    "details-level": "full"
    #}
    #res = api_call(url, headers, payload=payload)
    # User
    # High-availability
    # Administrators
    url = base_url + "show-logs"    # Interesting
    # Cloud services    
    # Misc
    #   where-used
    #   show-changes
    #   show-gateways-and-servers
    #   show-unused-objects

    res = api_call(url, headers)
    print(res.json())

    url = base_url + "logout"
    headers = logout(url, headers)
    print(headers)
