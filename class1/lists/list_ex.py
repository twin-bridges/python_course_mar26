#!/usr/bin/env python

import ipdb  # noqa
from rich import print

my_list = ["zzz", "world", "foo", 22, None]
ipdb.set_trace()

print(type(my_list))
print(my_list)
print(my_list[0])
print(my_list[2])
print(my_list[-1])

my_list[0] = "new value"
print(my_list)

some_list = [42, "a string"]
# my_list += some_list
my_list = my_list + some_list
print(my_list)

other_list = []

a_tuple = (42, 22, "hello")
print(type(a_tuple))
print(a_tuple)
