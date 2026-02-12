from rich import print
import ipdb  # noqa

my_list = ["hello", "world", "something", "else"]
for loop_var in my_list:
    print(loop_var)
    # Print the first letter
    print(loop_var[0])
    # Print the last letter
    print(loop_var[-1])
