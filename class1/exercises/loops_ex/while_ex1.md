### While-loop Exercise1

Construct a while loop such that you wait in the while loop for WAIT_TIME seconds (set this to a value of 8).

You should use time.time() to record both the start_time and the cur_time. The amount of seconds waited will be cur_time - start_time.

Inside your while loop use time.sleep(1) to sleep 1 second and also print a message stating "Sleeping 1s".

When WAIT_TIME has elapsed, you should exit your while loop. You should also print the message "All done..."

Your output should look similar to the following:

```bash
$ python while_ex1.py 
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
Sleeping 1s
All done...
```

And your program should take roughly 8 seconds to run (8 seconds and a bit).
