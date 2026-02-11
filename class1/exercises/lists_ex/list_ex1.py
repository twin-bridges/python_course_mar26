#!/usr/bin/env python
import yaml
from rich import print

filename = "locations.yml"

# Read in file as YAML
with open(filename) as f:
    locations = yaml.safe_load(f)

print()

# Print the list
print(locations)

# Print first element of list
print(f"First element: {locations[0]}")

# Print last element of list
print(f"Last element: {locations[-1]}")

# Print length of the list
print(f"List length: {len(locations)}")

# Add element to the list
locations.append("Leipzig")

# Change the fourth element of the list to be 'Stuttgart'
locations[3] = "Stuttgart"

# Print the current list
print(locations)

# Use list concatentation to add the following list ["Dortmund", "Essen"]
# Could also do: locations += ["Dortmund", "Essen"]
locations = locations + ["Dortmund", "Essen"]

# Print the current list
print(locations)

# Pop the first element of the list into a variable
city1 = locations.pop(0)

# Pop the last element of the list into a variable
city_n = locations.pop()

# Print 'city1', 'city_n', and current 'locations' list
print(f"{city1=}")
print(f"{city_n=}")
print(f"{locations=}")

