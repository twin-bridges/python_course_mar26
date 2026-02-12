from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]
for idx, loop_var in enumerate(my_list):
    print(f"{idx} --> {loop_var}")
