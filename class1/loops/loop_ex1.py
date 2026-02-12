from rich import print
import ipdb  # noqa

for loop_var in ["hello", "world", "something", "else"]:
    ipdb.set_trace()
    print(loop_var)
