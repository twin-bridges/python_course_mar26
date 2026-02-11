#!/usr/bin/env python
from rich import print

ip_address = "198.51.100.0/24"
ipv6_address = "2001:db8:1:1::/64"

# Divide the network from the mask
ipv4_network, ipv4_mask = ip_address.split("/")

# Obtain the octets
octet1, octet2, octet3, octet4 = ipv4_network.split(".")

divider = "-" * 15
print("\nString Exercise1, part-a (IPv4 .split())")
print(f"IPv4 Network: {ipv4_network}")
print(f"IPv4 Mask: {ipv4_mask}\n")
print(f"{'octet1':15} {'octet2':15} {'octet3':15} {'octet4':15}")
print(f"{divider:15} {divider:15} {divider:15} {divider:15}")
print(f"{octet1:15} {octet2:15} {octet3:15} {octet4:15}")

# Divide the network from the mask (IPv6)
ipv6_network, ipv6_mask = ipv6_address.split("/")

# Obtain the hextets
# _ indicates a junk variable (i.e. just discarded)
start_ipv6_network, _ = ipv6_network.split("::")
# Hard-coded length, in practice would (probably) use a list
hextet1, hextet2, hextet3, hextet4 = start_ipv6_network.split(":")

print(ipv6_network)
print(ipv6_mask)

print("\nString Exercise1, part-b (IPv6 .split())")
print(f"IPv6 Network: {ipv6_network}")
print(f"IPv6 Mask: {ipv6_mask}\n")
print(f"{'hextet1':15} {'hextet2':15} {'hextet3':15} {'hextet4':15}")
print(f"{divider:15} {divider:15} {divider:15} {divider:15}")
print(f"{hextet1:15} {hextet2:15} {hextet3:15} {hextet4:15}")
