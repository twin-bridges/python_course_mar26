#!/usr/bin/env python
import ipdb  # noqa
import json
from rich import print


def check_service(service):
    """Just placeholder function."""
    pass


with open("tcp_services.json") as f:
    services = json.load(f)

service_list = services["objects"]
print(len(service_list))

for service in service_list:
    service_name = service["name"]
    if service_name == "ftp":
        print("Found FTP Service")
        check = check_service(service)
        if check:
            print("FTP service check passed")
    elif service_name == "domain-tcp":
        print("Found DNS (TCP)")
        check_service(service)
    else:
        print("Service not found")
        print("Nothing else to do")
