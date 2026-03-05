import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    # "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    cfg_commands = [
        "set password-controls complexity 3",
        "set password-controls deny-on-nonuse enable on",
        "set password-controls min-password-length 10",
    ]

    print("[green][Gaia Config SSH][/green] Configure Password Policy")
    data = ssh_conn.send_config_set(cfg_commands)
    data += ssh_conn.save_config()
    # print(data)
