import json
from rich import print
import ipdb  # noqa

with open("tcp_services.json") as f:
    tcp_services = json.load(f)

ipdb.set_trace()
print(tcp_services)
