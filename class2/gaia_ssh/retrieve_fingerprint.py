import os
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# This looks for a .env file and loads it
load_dotenv()

secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]

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
    print(ssh_conn.find_prompt())

    # Enter expert mode
    ssh_conn.enable()
    print(ssh_conn.find_prompt())

    cmd = "fwm fingerprint localhost 443"
    fingerprint = ssh_conn.send_command(cmd)
    # print(f"{fingerprint=}")

    for line in fingerprint.splitlines():
        if "#FINGER" in line:
            print(line)

    data = ssh_conn.exit_enable_mode()
