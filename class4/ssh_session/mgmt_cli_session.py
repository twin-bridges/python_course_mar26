#!/usr/bin/env python
import os
import json
from rich import print
from netmiko import ConnectHandler

from dotenv import load_dotenv


def mgmt_cli_auth(ssh_conn, username, password):
    """Use 'mgmt_cli' to authenticate and return the session_id."""

    cmd = f'mgmt_cli login user "{username}" password "{password}" --format json'
    auth_data = ssh_conn.send_command(cmd)

    auth_dict = json.loads(auth_data)
    return auth_dict["sid"]


def main():

    load_dotenv()
    secret = os.environ["CHKP_EXPERT"]
    admin_pass = os.environ["CHKP_ADMIN"]

    pod99 = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "secret": secret,
    }

    with ConnectHandler(**pod99) as ssh_conn:
        ssh_conn.enable()
        session_id = mgmt_cli_auth(ssh_conn, username="admin", password=admin_pass)

        print(session_id)


if __name__ == "__main__":
    main()
