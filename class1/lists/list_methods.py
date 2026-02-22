#!/usr/bin/env python

import ipdb  # noqa
from rich import print

my_list = ["zzz", "world", "foo", 22, None]
ipdb.set_trace()

print(my_list)
my_list.append(42)
print(my_list)

some_list = [0, "hello"]
my_list.extend(some_list)
print(my_list)

pop_val = my_list.pop()
print(f"{pop_val=}")
print(f"{my_list=}")

pop_val = my_list.pop(0)
print(f"{pop_val=}")
print(f"{my_list=}")

my_list.insert(0, "first val")
print(f"{my_list=}")

my_list.remove("foo")
print(f"{my_list=}")
