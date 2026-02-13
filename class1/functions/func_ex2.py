
def my_func(x, y):
    print(f"{x=}")
    print(f"{y=}")
    return x + y

print()
ret_val = my_func(x=7, y=2)
print(f"{ret_val=}")

print()
ret_val = my_func(y=42, x=0)
print(f"{ret_val=}")
