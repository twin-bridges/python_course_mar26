import os
from dotenv import load_dotenv


# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

chkpt_fw99 = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "secret": secret,
}

device_list = [chkpt_fw99]
