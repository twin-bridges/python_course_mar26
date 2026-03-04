from rich import print

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [x**2 for x in my_list]
print(squares)

cubes = [x**3 for x in my_list]
print(cubes)

evens = [x for x in my_list if x % 2 == 0]
print(evens)

odds = [x for x in my_list if x % 2 == 1]
print(odds)

sentence = "This is a test sentence."
words = sentence.split()
print(words)

capital_words = [word.upper() for word in words]
print(capital_words)
