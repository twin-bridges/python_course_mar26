#!/usr/bin/env python
from rich import print

# Open file
f = open("my_file.txt", "r")

# Read entire file contents
data = f.read()
print(data)

# Go back to start of the file
f.seek(0)

# Read the entire file, but as a list of lines
data = f.readlines()
print(type(data))
print(data)

# Go back to start of the file
f.seek(0)

# Loop over the file (haven't covered loops yet)
print("Looping over file")
for line in f:
    # Eliminate double enter
    line = line.strip()
    print(repr(line))

# Cloes file
f.close()
