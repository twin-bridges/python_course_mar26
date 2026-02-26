### Gaia SSH Exercise1

Connect to your lab pod using Netmiko. You will need to use an SSH key to connect. This will require the following Netmiko arguments:

```python
chkpt_fw = {
    "host": "chkpnt-podN.lasthop.io",       # REPLACE with your pod
    "device_type": "checkpoint_gaia",
    "username": "admin",
    "use_keys": True,       # NEEDED for SSH Key
    "key_file": "/home/studentN/.ssh/eu-sshkey.pem",    # REPLACE with your student
}
```

Using this SSH connection, execute "show arp dynamic all" and print this response out to standard output.

Your output should look similar to the following:

```bash
$ python gaia_ssh_ex1.py 
Dynamic Arp Parameters

IP Address                 Mac Address                
172.31.32.1             0a:61:33:92:44:55
172.31.128.1            0a:15:04:3a:87:eb
172.31.144.1            0a:be:1f:c0:c1:03
172.31.145.1            0a:ce:8f:94:04:c9

```
