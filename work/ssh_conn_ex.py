from netmiko import ConnectHandler
from rich import print


def main():

    pod1 = {
        "host": "chkpnt-pod1.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "session_log": "output.log",
    }
    pod99 = {
        "host": "chkpnt-pod99.lasthop.io",
        "device_type": "checkpoint_gaia",
        "username": "admin",
        "use_keys": True,
        "key_file": "/home/kbyers/.ssh/eu-sshkey.pem",
        "session_log": "output.log",
    }

    for device in (pod1, pod99):
        with ConnectHandler(**device) as ssh_conn:
            print(f"Our device is: {device['host']}:")
            cmd = "show interfaces all"
            data = ssh_conn.send_command(cmd)

            intf_dict = {}
            intf_name = ""
            ip_addr = ""
            for line in data.splitlines():
                if line.startswith("Interface"):
                    fields = line.split()
                    intf_name = fields[1]
                if "ipv4-address" in line:
                    fields = line.split()
                    ip_addr = fields[1]

                if intf_name and ip_addr:
                    intf_dict[intf_name] = ip_addr

            print(intf_dict)
            print()


if __name__ == "__main__":
    main()
