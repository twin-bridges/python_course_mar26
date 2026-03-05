def gen_blockedip_fw_rules():
    blacklisted_ips = [
        {
            "layer": "Network",
            "name": "Blacklisted IPs",
            "source": "Blocked IPs",
            "destination": "Any",
            "service": "Any",
            "action": "Drop",
            "position": 1,
        },
    ]

    return blacklisted_ips


def gen_mgmt_fw_rules(fw_name):
    management_rules = [
        {
            "layer": "Network",
            "name": "Ansible Management Access",
            "source": [
                "Ansible Server",
                "Windows SmartConsole",
                "Windows SmartConsole Public",
            ],
            "destination": fw_name,
            "service": "Any",
            "action": "Accept",
            "position": 2,
        },
        {
            "layer": "Network",
            "name": "SSH Access",
            "source": "Any",
            "destination": fw_name,
            "service": "SSH",
            "action": "Accept",
            "position": 3,
        },
    ]

    return management_rules
