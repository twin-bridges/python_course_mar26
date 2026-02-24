import os
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def check_password_policy(api_client):
    api_endpoint = "show-password-policy"
    api_res = api_client.api_call(command=api_endpoint)

    password_policy = api_res.data
    password_lock = password_policy["lock-settings"]
    password_history = password_policy["password-history"]
    password_strength = password_policy["password-strength"]
    ipdb.set_trace()
    print(password_lock)

    failed_attempts = password_lock["failed-attempts-settings"][
        "failed-attempts-allowed"
    ]
    lockout_duration = password_lock["failed-attempts-settings"][
        "failed-lock-duration-seconds"
    ]
    inactivity_days = password_lock["failed-attempts-settings"]["inactivity-settings"][
        "inactivity-threshold-days"
    ]

    #    'inactivity-settings': {
    #        'inactivity-threshold-days': 365,
    #        'lock-unused-accounts-enabled': False
    #    },
    #    'must-one-time-password-enabled': False,
    #    'password-expiration-days': 'never',
    #    'password-expiration-maximum-days-before-lock': 'never',
    #    'password-expiration-warning-days': 7

    CHECKS_PASSED = True
    MAX_FAILED_ATTEMPTS = 10
    MIN_LOCKOUT_DURATION = 600

    # CHECKS #####
    print()
    print("Password Policy Checks")
    print(f".failed login attempts <= {MAX_FAILED_ATTEMPTS}...", end="")
    if failed_attempts <= MAX_FAILED_ATTEMPTS:
        print("[green]pass[/green]")
    else:
        CHECKS_PASSED = False
        print("[red]fail[/red]")

    print(f".account lockout duration >= {MIN_LOCKOUT_DURATION}...", end="")
    if lockout_duration >= MIN_LOCKOUT_DURATION:
        print("[green]pass[/green]")
    else:
        CHECKS_PASSED = False
        print("[red]fail[/red]")

    return CHECKS_PASSED


# {
#    'failed-attempts-settings': {
#        'failed-attempts-allowed': 10,
#        'failed-lock-duration-seconds': 1200,
#        'failed-lock-enabled': False,
#        'failed-lock-enforced-on-admin': False
#    },
#    'inactivity-settings': {
#        'inactivity-threshold-days': 365,
#        'lock-unused-accounts-enabled': False
#    },
#    'must-one-time-password-enabled': False,
#    'password-expiration-days': 'never',
#    'password-expiration-maximum-days-before-lock': 'never',
#    'password-expiration-warning-days': 7
# }


def check_users(api_client):

    CHECK_USERS = {"admin", "monitor"}
    # Set False if any test fails (and return)
    CHECK_PASSED = True

    api_endpoint = "show-users"
    api_res = api_client.api_call(command=api_endpoint)

    users = api_res.data["objects"]

    audit_users = []
    for user in users:
        username = user["name"]
        # user_roles = user["roles"]
        audit_users.append(username)

    # CHECKS #####
    print()
    print("User checks...", end="")
    audit_users = set(audit_users)
    if audit_users == CHECK_USERS:
        print("[green]pass[/green]")
    else:
        CHECK_PASSED = False
        print("[red]fail[/red]")

    return CHECK_PASSED


def main():
    host = "chkpnt-pod99.lasthop.io"

    # This looks for a .env file and loads it
    load_dotenv()
    username = "admin"
    password = os.environ["CHKP_ADMIN"]

    api_version = "1.8"
    no_ssl_verify = True

    client_args = APIClientArgs(
        server=host, api_version=api_version, unsafe=no_ssl_verify, context="gaia_api"
    )

    with APIClient(client_args) as api_client:
        api_client.login(username, password)

        # Any test fails and will be set to False
        check_status = True
        check_status = check_users(api_client) and check_status
        check_status = check_password_policy(api_client) and check_status


if __name__ == "__main__":
    main()
