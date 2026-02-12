#!/usr/bin/env python
import ipdb  # noqa
import json
from rich import print

with open("tcp_services.json") as f:
    services = json.load(f)

service_list = services["objects"]
print(len(service_list))

for service in service_list:
    service_name = service["name"]
    if service_name == "ftp":
        print("Found FTP Service")
    elif service_name == "domain-tcp":
        print("Found DNS (TCP)")
    else:
        print(service_name)



