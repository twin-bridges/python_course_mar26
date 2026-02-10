from rich import print
import ipdb

my_list = ['hello', 'world', "something", "else"]

for loop_var in my_list:
    if loop_var == "something":
        print("<skip>")
        continue
    print(loop_var)
    print("...still in the loop")


