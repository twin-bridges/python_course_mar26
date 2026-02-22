#!/usr/bin/env python
from rich import print


def fw_func(name, ipaddr, os_version="R82"):
    print(f"{name=}")
    print(f"{ipaddr=}")
    print(f"{os_version=}")
    return f"{name}-{ipaddr}-{os_version}"


# Positional arguments
ret_val = fw_func("chkpnt-pod99", "3.77.44.109", "R81.20")
print(f"\n{ret_val=}\n")

# Named arguments
ret_val = fw_func(
    os_version="R82",
    ipaddr="3.77.44.100",
    name="chkpnt-pod1",
)
print(f"\n{ret_val=}\n")

# Named arguments use default value
ret_val = fw_func(
    name="chkpnt-pod1",
    ipaddr="3.77.44.100",
)
print(f"\n{ret_val=}\n")

# Both named and positional
ret_val = fw_func(
    "chkpnt-pod2",
    os_version="R82.10",
    ipaddr="3.77.44.9",
)
print(f"\n{ret_val=}\n")
