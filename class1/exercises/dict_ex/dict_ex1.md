#!/usr/bin/env python
import json
from rich import print

with open("net_object_net128.json") as f:
    network_obj = json.load(f)

# Print the dictionary
print(network_obj)

# Retrieve the 'name', 'subnet4' and 'mask-length4' fields (store into variables)
name = network_obj['name']
network = network_obj['subnet4']
netmask = network_obj['mask-length4']

# Print these three variables out.
print(f"Network Object: {name} ({network}/{netmask})")

# Retrieve the network_obj['domain']['uid'] field (nested dictionary) and save to a variable.
domain_uid = network_obj['domain']['uid']
print(f"Domain UID: {domain_uid}")

# Add a new key 'location' to the dictionary (set the value to "Munich").
network_obj["location"] = "Munich"

# Change the 'location' key to "Cologne"
network_obj["location"] = "Cologne"

# Delete the 'color' key
network_obj.pop('color')

# Print your dictionary
print(network_obj)

"""
    'uid': '6796b2f5-d449-44dc-9cf8-75b33c4ca493',
    'name': 'hq_net_128',
    'type': 'network',
    'domain': {
        'uid': '41e821a0-3720-11e3-aa6e-0800200c9fde',
        'name': 'SMC User',
        'domain-type': 'domain'
    },
    'subnet4': '172.31.128.0',
    'mask-length4': 24,
"""
