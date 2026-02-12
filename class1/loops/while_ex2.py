#!/usr/bin/env python
import ipdb  # noqa
import time
from rich import print

WAIT_TIME = 6

print()
start_time = time.time()
while True:
    print("In loop...")
    time.sleep(1)
    cur_time = time.time()
    if (cur_time - start_time) > WAIT_TIME:
        break

print("\nLoop over")
