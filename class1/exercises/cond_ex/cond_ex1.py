#!/usr/bin/env python
from rich import print

pod_numb = input("Enter pod number: ")
fw_name = f"chkpnt-pod{pod_numb}"

if fw_name == "chkpnt-pod1":
    print("Found pod1")
elif fw_name == "chkpnt-pod99":
    print("Found pod99")
else:
    print("Not my pod")
