import json
from rich import print
import ipdb # noqa

with open("sessions.json") as f:
    sessions = json.load(f)

ipdb.set_trace()
print(sessions)
