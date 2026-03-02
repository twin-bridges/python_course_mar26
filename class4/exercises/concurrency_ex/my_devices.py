import os
from dotenv import load_dotenv


# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw1 = {
    "host": "chkpnt-pod1.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}
chkpt_fw2 = {
    "host": "chkpnt-pod2.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw3 = {
    "host": "chkpnt-pod3.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw4 = {
    "host": "chkpnt-pod4.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

chkpt_fw5 = {
    "host": "chkpnt-pod5.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}


device_list = [chkpt_fw1, chkpt_fw2, chkpt_fw3, chkpt_fw4, chkpt_fw5]
