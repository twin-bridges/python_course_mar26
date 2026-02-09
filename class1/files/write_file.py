#!/usr/bin/env python

import ipdb

ipdb.set_trace()

f = open("new_file.txt", "w")
f.write("hello world\n")
f.write("something else\n")
f.write("one last line\n")
print()

f.close()
