### Complex Data Structures Exercise1

Read "show_tasks.json" as JSON and save this as a variable named 'tasks_ds'.

Use ipdb and ipdb.set_trace() and print 'tasks_ds', print 'type(tasks_ds)', and print 'tasks_ds.keys()'.

From this drill into the data structure one-level and retrieve the "tasks" key into a new variable named tasks. In other words: tasks = tasks_ds["tasks"].

As this point the "tasks" variable should be a list. Verify this by using 'type(tasks)' and 'len(tasks)'.

Use a for loop to loop over the tasks and from the inner 'task' object (which should be a dictionary) retrieve the "task-id" and "status" fields.

Your loop code should look similar to the following:

```python
for task in tasks:
    task_id = task["task-id"]
    status = task["status"]
    print(f"{task_id} --> {status}")
```

