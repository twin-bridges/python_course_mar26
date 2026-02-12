#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
start_time = time.time()
while time.time() - start_time < WAIT_TIME:
    print(time.time() - start_time)
    time.sleep(1)
    print("In loop...")

print("\nLoop over")
