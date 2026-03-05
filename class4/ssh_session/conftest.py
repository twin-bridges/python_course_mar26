import pytest
import os
from dotenv import load_dotenv
from netmiko import ConnectHandler


@pytest.fixture(scope="module")
def ssh_conn():

    load_dotenv()
    secret = os.environ["CHKP_EXPERT"]

    test_device = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "secret": secret,
    }

    with ConnectHandler(**test_device) as ssh_conn:
        ssh_conn.enable()

        # Object that is passed to the tests
        yield ssh_conn
