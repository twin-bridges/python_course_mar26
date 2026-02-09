#!/usr/bin/env python
from rich import print

# and: if the first condition is False, we are done.
check_cond = False
if check_cond and my_func():  # noqa
    print("Never printed")

# or: if the first condition is True, we are done.
skip_func = True
if skip_func or my_func():  # noqa
    print("Always printed")
