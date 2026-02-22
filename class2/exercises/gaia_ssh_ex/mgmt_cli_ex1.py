import os
import json
import time
import ipdb  # noqa
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
    "session_log": "output.log",
    "secret": secret,
}

with ConnectHandler(**chkpt_fw) as ssh_conn:
    # Enter expert mode
    ssh_conn.enable()

    # Capture Session ID
    print("Capture Session ID using 'mgmt_cli'")
    cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    sid = d_struct["sid"]

    # Capture address range objects
    cmd = f'mgmt_cli show-objects type "address-range" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)

    # Convert JSON-string to data structure
    d_struct = json.loads(data)
    address_ranges = d_struct["objects"]

    print()
    print("Address Ranges:")
    print("-" * 30)
    for addr_range in address_ranges:
        ar_name = addr_range["name"]
        start_ip = addr_range['ipv4-address-first']
        end_ip = addr_range['ipv4-address-last']
        print(f"{ar_name} -> {start_ip} to {end_ip}")
    print("-" * 30)
    print()
