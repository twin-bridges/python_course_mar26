### Complex Data Structures Exercise2

Convert your code from Complex Data Structures Exercise1 into a Python script.

The script should have a function named 'read_json' which takes a 'filename' argument and returns the JSON data from the file.

The script should also have a function named 'extract_fields' which takes a task dictionary as an argument. The function should extract the "task-id", "status", and "lock" fields (note, "lock" is embedded inside "meta-info"). This 'task' dictionary is the final dictionary that we were extracting "task-id" and "status" from in Exercise1. The function should return: '(task_id, status, lock)'.

Your main program should read the "show_tasks.json" file using your function, do the initial data processing to retrieve the "tasks" list and loop over the "tasks" list to obtain the "task" dictionary.

Finally, your main program should call the "extract_fields" function and print out the returned data.

Your output should look similar to the following:

```bash
$ python complex_ds_ex2.py 

d1313671-7c40-4c95-be76-a2ac451705e7 --> succeeded lock='unlocked'
37b26077-b9bb-40c7-a522-45ad0bee23c3 --> succeeded lock='unlocked'
ffb1b55b-1436-40e1-9076-83ebe54b5c68 --> succeeded lock='unlocked'
```
