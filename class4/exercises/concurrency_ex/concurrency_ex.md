### Concurrency Exercise

Connect using a thread pool and Netmiko to pods1-5. Your thread pool size should be set to 5.

Using threads execute "show interface eth0" and retreive the output. You should also record your hostname in the thread result (so you know which device the result came from). 

Use the "as_completed" pattern to print out the results as they are returned. However, only display the device hostname and the "ipv4-address" from the "show interface" output.

Record and print the total execution time for your script. 

Change the thread pool size to 2 and see how it changes your execution time.

Optional: Convert from threads over to processes. Use a process pool size of 5 and compare the execution time (threads to processes).

