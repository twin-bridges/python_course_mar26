#!/usr/bin/env python
from rich import print

ip_addr = "142.251.141.110"
fields = ip_addr.split(".")
print(fields)

octet1, octet2, octet3, octet4 = fields

# f-string 15-wide columns (left-aligned by default)
print()
print(f"|{octet1:15}|{octet2:15}|{octet3:15}|{octet4:15}|")

# f-string 15-wide columns (right-aligned)
print()
print(f"|{octet1:>15}|{octet2:>15}|{octet3:>15}|{octet4:>15}|")

# f-string 15-wide columns (centered)
print()
print(f"|{octet1:^15}|{octet2:^15}|{octet3:^15}|{octet4:^15}|")

# Variable display trick
print()
print(f"{octet1=}")

# f-string expressions get evaluated
print()
var1 = 22
var2 = 42
print(f"Variable sum: {var1 + var2}")
