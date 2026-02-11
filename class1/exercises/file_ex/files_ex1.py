#!/usr/bin/env python
import json
from rich import print

filename = "network_objects.json"

# Read in file as text
with open(filename) as f:
    data = f.read()

# rich.print is misleading here as it would make it look like a data structure
print(f"\nRead in file({filename}) as a string")
print(f"Type 'data' var: {type(data)}")

# Read in file as JSON
with open(filename) as f:
    data = json.load(f)
print(f"\nRead in file({filename}) as a data structure (dictionary)")
print(f"Type 'data' var: {type(data)}")
print(f"Type data['objects'] field: {type(data['objects'])}")
print()
