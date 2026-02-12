#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
check_var1 = "some string"
check_var2 = ""
while check_var1:
    print("In loop...")
    time.sleep(1)
    if not check_var2:
        break

print("\nLoop over")
