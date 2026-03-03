### Complex Data Structures Exercise1

Read "show_tasks.json" as JSON and save this data as a variable named 'tasks_ds'.

Use ipdb and ipdb.set_trace() and print 'tasks_ds', print 'type(tasks_ds)', and print 'tasks_ds.keys()'.

Next drill into the 'tasks_ds' data structure one-level and retrieve the "tasks" key; save this as a new variable named 'tasks'. In other words: tasks = tasks_ds["tasks"].

As this point the 'tasks' variable should be a list. Verify this by using 'type(tasks)' and 'len(tasks)'.

Use a for-loop to loop over the 'tasks'. Each entry in the 'tasks' list will be a task-dictionary. From this inner dictionary retrieve the "task-id" and "status" fields.

Your loop code should look similar to the following:

```python
for task in tasks:
    task_id = task["task-id"]
    status = task["status"]
    print(f"{task_id} --> {status}")
```

