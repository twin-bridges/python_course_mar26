import yaml
from rich import print

with open("gaia_api.yaml") as f:
    data = yaml.safe_load(f)

print(data)
