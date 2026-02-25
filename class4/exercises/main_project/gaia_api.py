import os
import ipdb  # noqa
import operator
from rich import print
from dotenv import load_dotenv
from cpapi import APIClient, APIClientArgs


def condition_check(cond1, cond2, comparator):
    """Function to consolidate the condition check code."""

    CHECK_PASSED = True
    operations = {
        "==": operator.eq,
        "!=": operator.ne,
        "<=": operator.le,
        ">=": operator.ge,
        "<": operator.lt,
        ">": operator.gt,
    }

    if comparator not in operations:
        raise ValueError(f"Invalid comparator: {comparator}")

    if operations[comparator](cond1, cond2):
        print("[green]pass[/green]")
    else:
        CHECK_PASSED = False
        print("[red]fail[/red]")

    return CHECK_PASSED


def check_password_policy(api_client):
    api_endpoint = "show-password-policy"
    api_res = api_client.api_call(command=api_endpoint)

    password_policy = api_res.data
    password_lock = password_policy["lock-settings"]
    password_strength = password_policy["password-strength"]
    print(password_strength)

    failed_attempts = password_lock["failed-attempts-settings"][
        "failed-attempts-allowed"
    ]
    lockout_duration = password_lock["failed-attempts-settings"][
        "failed-lock-duration-seconds"
    ]
    inactivity_days = password_lock["inactivity-settings"]["inactivity-threshold-days"]
    lock_inactive_accounts = password_lock["inactivity-settings"][
        "lock-unused-accounts-enabled"
    ]
    password_complexity = password_strength["complexity"]
    password_min_length = password_strength["minimum-length"]

    MAX_FAILED_ATTEMPTS = 10
    MIN_LOCKOUT_DURATION = 600
    MAX_INACTIVE_DAYS = 365
    LOCK_INACTIVE_ACCOUNTS = True
    MIN_PWD_CHAR_COMPLEXITY = 3
    MIN_PWD_LENGTH = 10

    # CHECKS #####
    print()
    print("Password Policy Checks")

    print(f".failed login attempts <= {MAX_FAILED_ATTEMPTS}...", end="")
    condition_check(failed_attempts, MAX_FAILED_ATTEMPTS, comparator="<=")

    print(f".account lockout duration >= {MIN_LOCKOUT_DURATION}...", end="")
    condition_check(lockout_duration, MIN_LOCKOUT_DURATION, comparator=">=")

    print(f".max inactive days <= {MAX_INACTIVE_DAYS}...", end="")
    condition_check(inactivity_days, MAX_INACTIVE_DAYS, comparator="<=")

    print(f".lock inactive accounts is {LOCK_INACTIVE_ACCOUNTS}...", end="")
    condition_check(lock_inactive_accounts, LOCK_INACTIVE_ACCOUNTS, comparator="==")


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
    print("User checks:")
    print(f".only allowed users configured: {CHECK_USERS}...", end="")
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

        check_users(api_client)
        check_password_policy(api_client)


if __name__ == "__main__":
    main()
