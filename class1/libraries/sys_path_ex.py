"""Can't use ipdb for this since it alters sys.path."""
import sys
from rich import print

print("\nsys.path:")
print("-" * 30)
print(sys.path)
print()
