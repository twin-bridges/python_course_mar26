import ipdb  # noqa
from rich import print  # noqa


def test_users(gaia_api):

    api_client = gaia_api

    CHECK_USERS = {"admin", "monitor"}

    api_endpoint = "show-users"
    api_res = api_client.api_call(command=api_endpoint)

    users = api_res.data["objects"]
    audit_users = []
    for user in users:
        username = user["name"]
        # user_roles = user["roles"]
        audit_users.append(username)

    # CHECKS #####
    audit_users = set(audit_users)
    assert audit_users == CHECK_USERS


def test_password_policy(gaia_api):

    MAX_FAILED_ATTEMPTS = 10
    MIN_LOCKOUT_DURATION = 600
    MAX_INACTIVE_DAYS = 365
    LOCK_INACTIVE_ACCOUNTS = True
    MIN_PWD_CHAR_COMPLEXITY = 3
    MIN_PWD_LENGTH = 10

    api_client = gaia_api

    api_endpoint = "show-password-policy"
    api_res = api_client.api_call(command=api_endpoint)

    password_policy = api_res.data
    password_lock = password_policy["lock-settings"]
    password_strength = password_policy["password-strength"]

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

    # CHECKS #####
    assert failed_attempts <= MAX_FAILED_ATTEMPTS
    assert lockout_duration >= MIN_LOCKOUT_DURATION
    assert inactivity_days <= MAX_INACTIVE_DAYS
    assert lock_inactive_accounts == LOCK_INACTIVE_ACCOUNTS
    assert password_complexity >= MIN_PWD_CHAR_COMPLEXITY
    assert password_min_length >= MIN_PWD_LENGTH
