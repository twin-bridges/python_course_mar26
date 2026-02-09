import json
from rich import print

with open("gaia_api.json") as f:
    data = json.load(f)

print(data)
