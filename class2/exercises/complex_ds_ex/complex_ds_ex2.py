import json
from rich import print
import ipdb  # noqa


def read_json(filename):
    data = None
    with open(filename) as f:
        data = json.load(f)

    return data


def extract_fields(task):
    task_id = task["task-id"]
    status = task["status"]
    lock = task["meta-info"]["lock"]

    return (task_id, status, lock)


if __name__ == "__main__":
    filename = "show_tasks.json"
    tasks_ds = read_json(filename)

    # Remove outermost key
    tasks = tasks_ds["tasks"]

    print()
    for task in tasks:
        task_id, status, lock = extract_fields(task)
        print(f"{task_id} --> {status} {lock=}")
    print()
