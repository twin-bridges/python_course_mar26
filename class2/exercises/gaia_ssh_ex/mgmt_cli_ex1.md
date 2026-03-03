### mgmt_cli SSH Exercise1

Connect to your lab pod using Netmiko. You will once again need to use an SSH key to connect.

You will also need to provide the Check Point "expert" credentials. I recommend you do this by using .env file and the following pattern.

```python
from dotenv import load_dotenv

# This looks for a .env file and loads it
load_dotenv()
secret = os.environ["CHKP_EXPERT"]
admin_pass = os.environ["CHKP_ADMIN"]
```

You will then use this 'secret' variable in your Netmiko ConnectHandler arguments.

Once connected, call the .enable() method to elevate privileges (this should cause you to enter 'expert' mode).

Now execute the following:

```python
cmd = f'''mgmt_cli login user "admin" password "{admin_pass}" --format json'''
data = ssh_conn.send_command(cmd)
```

This will cause you to login using 'mgmt_cli'.

Now extract the session ID from the reponse.

```
# Requires the 'json' library be imported
d_struct = json.loads(data)
sid = d_struct["sid"]
```

At this point, you should be able to execute mgmt_cli commands using your session ID.

```
cmd = f'mgmt_cli show-objects type "address-range" --session-id "{sid}" --format json'
data = ssh_conn.send_command(cmd)
```

Capture the above address range objects and extract them from the returned data structure. The mgmt_cli is returning a JSON string which can convert to Python data structures using 'json.loads(data)'.

Extract the following fields from each of the address range objects: name, ipv4-address-first, ipv4-address-last. 

Finally, print out these three variables to standard output. Your output should look similar to the following:

```bash
$ python mgmt_cli_ex1.py 
Capture Session ID using 'mgmt_cli'

Address Ranges:
------------------------------
All_Internet -> 0.0.0.0 to 255.255.255.255
LocalMachine_Loopback -> 127.0.0.1 to 127.255.255.255
------------------------------

```
