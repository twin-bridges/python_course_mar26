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

for k, v in ftp_service.items():
    if k == "domain":
        print()
        for inner_k, inner_v in v.items():
            print(f"{inner_k} -> {inner_v}")
        print()
