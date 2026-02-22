from rich import print
import time

WAIT_TIME = 8

start_time = time.time()
while True:
    cur_time = time.time()
    if cur_time - start_time < WAIT_TIME:
        print("Sleeping 1s")
        time.sleep(1)
    else:
        print("All done...")
        break
