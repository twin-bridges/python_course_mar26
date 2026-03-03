### Strings Exercise

Use the .split() method to divide the following:

1. 198.51.100.0/24 (divide the network from the mask and create a separate variable for each).
    * Further subdivide the IPv4 address into octets.
    * Print out the ipv4_network, ipv4_mask, and all four octets.
    * Use f-strings and 4 x 15-character columns to print out each octet.
    * Center the octets in their column.
2. 2001:db8:1:1::/64 (divide the network from the mask and create a separate variable for each).
    a. Further subdivide the IPv6 address into hextets.
    b. Print out the ipv6_network, ipv6_mask, and all four hextets.
    c. Use f-strings and 4 x 15-character columns to print out each hextet.
    d. Center the hextets in their column.

Example output
```shell
$ python strings_ex1.py 

String Exercise1, part-1 (IPv4 .split())
----------------------------------------
IPv4 Network: 198.51.100.0
IPv4 Mask: 24

    octet1          octet2          octet3          octet4     
--------------- --------------- --------------- ---------------
      198             51              100              0       


String Exercise1, part-2 (IPv6 .split())
----------------------------------------
IPv6 Network: 2001:db8:1:1::
IPv6 Mask: 64

    hextet1         hextet2         hextet3         hextet4    
--------------- --------------- --------------- ---------------
     2001             db8              1               1       

```

