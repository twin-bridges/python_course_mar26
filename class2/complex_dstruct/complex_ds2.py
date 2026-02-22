import json
from rich import print
import ipdb  # noqa

with open("network_objects.json") as f:
    net_objects = json.load(f)

ipdb.set_trace()
print(net_objects)
