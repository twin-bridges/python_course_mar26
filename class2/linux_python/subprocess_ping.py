#!/usr/bin/env python
import subprocess
import ipdb  # noqa

command = ["ping", "-c", "4", "google.com"]

# run() execute the command; wait to finish
result = subprocess.run(
    command,
    capture_output=True, 
    text=True
)

ipdb.set_trace()
print(result.stdout)
print(result.stderr)
print(result.returncode)
