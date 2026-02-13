
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z

my_dict = {
    "x": 11,
    "y": 22,
    "z": 33,
}
ret_val = my_func(**my_dict)
