
def my_func(x, y, z=100):
    print(f"{x=}")
    print(f"{y=}")
    print(f"{z=}")
    return x + y + z

my_list = [1, 7, 99]
ret_val = my_func(*my_list)
