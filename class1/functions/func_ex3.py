
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z

ret_val = my_func(x=7, y=2)
print(f"{ret_val=}")


