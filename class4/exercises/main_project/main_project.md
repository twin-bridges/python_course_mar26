# Main Project

TODO: Just add in here the 3 managment host objects and the corresponding firewall policy for them (i.e. have the students do this).
TODO: Add a py.test fixture for the 3 management hosts and for the firewall policy containing these 3 hosts.
TODO: push firewall polilcy for Blocked IPs
TODO: add pathlib for blocked IPs file and push this file to a shared location like /tmp

### Gaia Configuration using API

DNS Config (endpoint: set-dns)

```yaml
primary: 172.31.0.2
secondary: 8.8.8.8
tertiary: 8.8.4.4
suffix: lasthop.io
```

Static Route (endpoint: set-static-route)

```yaml
network: 172.31.128.0/21
next_hop_gateway: 172.31.128.1
```

### Gaia Configuration using Netmiko-SSH

```bash
set password-controls complexity 3
set password-controls deny-on-nonuse enable on
set password-controls min-password-length 10
```

Call the Netmiko .save_config() method to ensure that you properly save these changes.

### Mgmt API Object Configuration

Host Objects

```python
smart_console_private = { 
    "name": "Windows SmartConsole",
    "ipv4-address": "172.31.12.101",
    "color": "red",
}
smart_console_public = { 
    "name": "Windows SmartConsole Public",
    "ipv4-address": "3.71.9.240",
    "color": "red",
}
ansible_server = { 
    "name": "Ansible Server",
    "ipv4-address": "3.125.34.232",
    "color": "black",
}
```

### Mgmt API Blocked IP Configuration

Create a Python script that uses the Mgmt API and configures a set of blocked IPs from a "blocked_ips.txt" file.

The script should do the following:
1. Retrieves the current "Blocked IPs" group and extracts all the member hosts. This query must handle the case then the "Blocked IPs" group doesn't exist.
2. Compares the currently configured blocked IPs (the group members) to the new blocked IPs (from the text file).
3. Adds any missing new blocked IPs as host objects.
4. Updates the group membership to match the blocked IPs from the text file.
5. Removes any blocked IP host objects that are no longer used (previous group members, but no longer in the "blocked_ips.txt" file).

Publish your changes.


### Mgmt API FW Policy Configuration

Add the following firewall policy rules via the Mgmt API (publish, but do NOT install them)

```python
fw_rules = [ 
    {   
        "layer": "Network",
        "name": "Blacklisted IPs",
        "source": "Blocked IPs",
        "destination": "Any",
        "service": "Any",
        "action": "Drop",
        "position": 1,
    },
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
```

## Verifications of Current Configuration using Pytest.

### Pytest Fixtures

Create three pytest fixtures:
1. pytest fixture that establishes a "gaia_api" connection.
2. pytest fixture that establishes a "mgmt_api" connection.
3. pytest fixture that establishes a Netmiko-SSH connection.


### Pytest Tests (Gaia API)

1. User checks (uses "show-users" endpont):
    * The only configured users are: admin and monitor
2. Password policy checks (uses "show-password-policy"):
    * Maximum failed login attempts is <= 10.
    * Minimum account lockout duration is >= 600s.
    * Maximum inactive days is <= 365.
    * Lock inactive accounts is set to True.
    * Minimum password character complexity is >= 3.
    * Minimum password length is >= 10.
3. DNS settings match the items you configured earlier in this lab.
4. The static route you configured exists and has the correct next hop.


### Pytest Tests (Mgmt API)
1. All the host objects are properly configured.
2. The "Blocked IPs" group is properly configured and has ten members.
3. The three firewall rules are properly configured.

### Install the Firewall Policy
