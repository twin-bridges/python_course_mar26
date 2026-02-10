import os
import json
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
    print(ssh_conn.find_prompt())

    # Capture Session ID
    print("Capture Session ID using 'mgmt_cli'")
    cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    # print(d_struct)

    sid = d_struct["sid"]
    cmd = f'mgmt_cli show-sessions details-level "full" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    # print(d_struct)

    sessions = d_struct["objects"]
    for session in sessions:
        # The walrus := (assign and evaluate in one operation)
        session_timeout = session["session-timeout"]
        if meta_info := session.get("meta-info"):
            create_time = meta_info["creation-time"]["iso-8601"]
            session_user = meta_info["creator"]
            session_lock = meta_info["lock"]
            msg = f"""
Session User:   {session_user}
Lock: {session_lock}
Session Create Time: {create_time}
Session Timeout: {session_timeout}
"""
            print(msg)

    cmd = f'mgmt_cli logout --session-id "{sid}" --format json'
    cmd = f'mgmt_cli show-sessions details-level "full" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    print(data)

#    cmd = f'mgmt_cli show-sessions --session-id "{sid}" --format json'
#    data = ssh_conn.send_command(cmd)
#    print(data)
#  #"uid" : "fa9ff9f8-352d-4c28-a69c-6dac18c76f2b",
#  #"sid" : "0LRP4rU6iDlZbLpq9e3v7rEoowMjToaLMVXSUaidx3o",
#
#
#    # cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
#    # mgmt_cli login --context gaia_api
#
## mgmt_cli show hostname --context gaia_api --session-id "983992120485592120101101504392120491021259212056100921201005188959212010155921209997921204997921209999685139"
## name: chkpnt-pod99
#
