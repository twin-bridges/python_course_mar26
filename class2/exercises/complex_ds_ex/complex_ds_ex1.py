import json
from rich import print
import ipdb  # noqa

with open("show_tasks.json") as f:
    tasks_ds = json.load(f)

ipdb.set_trace()
print(tasks_ds)
print(type(tasks_ds))
print(tasks_ds.keys())

# Remove outermost key
tasks = tasks_ds["tasks"]
ipdb.set_trace()
print(type(tasks))
print(len(tasks))

ipdb.set_trace()
for task in tasks:
    task_id = task["task-id"]
    status = task["status"]
    print(f"{task_id} --> {status}")
