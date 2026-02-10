from netmiko import ConnectHandler

chkpt_fw = {
    "host": "chkpnt-pod99.lasthop.io",
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,
    "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
    "session_log": "output.log",
}

with ConnectHandler(**chkpt_fw) as nc:
    print(nc.find_prompt())

    cmd = "api status"
    data = nc.send_command(cmd)
    print(data)
