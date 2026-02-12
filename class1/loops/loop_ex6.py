#!/usr/bin/env python
import ipdb  # noqa
from rich import print

ftp_service = {
    "uid": "97aeb3d0-9aea-11d5-bd16-0090272ccb30",
    "name": "ftp",
    "type": "service-tcp",
    "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain",
    },
    "port": "21",
    "icon": "Protocols/FTP",
    "color": "forest green",
}

print("\nLoop over the keys")
print("-" * 10)
for key in ftp_service.keys():
    print(key)

print("\nLoop over the values")
print("-" * 10)
# Loop over the values
for value in ftp_service.values():
    print(value)

print("\nLoop over the key-value")
print("-" * 10)
# Loop over the key-value
for k, v in ftp_service.items():
    print(f"{k} -> {v}")
