import os
import json
import time
import ipdb  # noqa
from rich import print
from dotenv import load_dotenv
from netmiko import ConnectHandler

# mS values for various times
ONE_DAY_MS = 86_400_000
ONE_HOUR_MS = 3_600_000

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
    # cmd = f'''mgmt_cli login -r true --format json'''
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    sid = d_struct["sid"]

    # Capture current session
    cmd = f'mgmt_cli show-session --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)
    my_session_uid = d_struct["uid"]

    cmd = f'mgmt_cli show-sessions details-level "full" --session-id "{sid}" --format json'
    data = ssh_conn.send_command(cmd)
    d_struct = json.loads(data)

    sessions = d_struct["objects"]
    print(f"Sessions: {len(sessions)}")
    ipdb.set_trace()

    # Enable debugger and quit to accumulate stale sessions
    # ipdb.set_trace()

    print(f"Session Count: {len(sessions)}")
    for session in sessions:
        session_timeout = session["session-timeout"]
        session_uid = session["uid"]

        if session_uid == my_session_uid:
            print("Skipping Current Session...")
            continue

        if meta_info := session.get("meta-info"):
            create_time = meta_info["creation-time"]["iso-8601"]
            epoch_create_time = meta_info["creation-time"]["posix"]
            session_user = meta_info["creator"]
            session_lock = meta_info["lock"]
            msg = f"""
Session User:   {session_user}
Lock: {session_lock}
Session Create Time: {create_time}
Session Timeout: {session_timeout}
"""
            print(msg)

            # *1000 to get current_time the same scale as Chkpnt (i.e. mS)
            current_time = int(time.time() * 1000)

            # Check for sessions under a day old (older sessions are probably SmartConsole)
            if current_time - epoch_create_time < ONE_DAY_MS:
                ipdb.set_trace()
                # Take over the session
                cmd = f'''mgmt_cli take-over-session uid "{session_uid}" --session-id "{sid}" disconnect-active-session true --format json'''
                data = ssh_conn.send_command(cmd, read_timeout=30)
                print(data)
                print("\n>>> Discarding Session >>>")
                print(session_uid)
                print(data)
                print(msg)
                # Discard the session
                cmd = 'mgmt_cli discard'
                data = ssh_conn.send_command(cmd, read_timeout=20)
            else:
                print("Session over 24 hours old...retaining")

    # Restore the original session
    cmd = '''mgmt_cli take-over-session uid "{my_session_uid}" --format json'''
    data = ssh_conn.send_command(cmd)
    cmd = f'mgmt_cli logout --session-id "{sid}" --format json'
    data += ssh_conn.send_command(cmd)
    print(data)
