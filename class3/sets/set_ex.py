from rich import print

my_list = [1, 1, 3, 4, 7, 6, 7, 8, 3, 10]
my_list2 = [1, 1, 7, 6, 7, 8, 3, 10, 20, 45, 81, 99]

my_set1 = set(my_list)
print(type(my_set1))
print(my_set1)

my_set2 = set(my_list2)
print(my_set2)

union_sets = my_set1 | my_set2
print(union_sets)

intersect_sets = my_set1 & my_set2
print(intersect_sets)

set_diff1 = my_set1 - my_set2
print(f"{my_set1=}")
print(f"{my_set2=}")
print(set_diff1)

set_diff2 = my_set2 - my_set1
print(f"{my_set1=}")
print(f"{my_set2=}")
print(set_diff2)
