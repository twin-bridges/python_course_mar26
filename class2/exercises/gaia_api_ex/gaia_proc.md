### Gaia 'show arp' Exercise

Repeat the Gaia authentication code from the Gaia authentication exercise.

In this script, use your authenticated Gaia session to execute 'show arp'. Retreive the ARP response from the firewall and process the ARP table.

From the ARP response, you should extract both the 'mac-address' and the 'ipv4-address'. You should then print this data to standard output.

Your output should look similar to the following:

```python
$ python gaia_proc.py 

172.31.32.1 -> 0a:61:33:92:44:55
172.31.128.1 -> 0a:15:04:3a:87:eb
172.31.144.1 -> 0a:be:1f:c0:c1:03
172.31.145.1 -> 0a:ce:8f:94:04:c9

```

