#!/usr/bin/env python

# Context manager automatically close the file (when done)
with open("my_file.txt") as f:
    data = f.read()

print(data)
