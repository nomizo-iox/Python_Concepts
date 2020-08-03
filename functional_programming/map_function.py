my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list = [*map(float, my_list)]
print(my_list)

my_list = [*map(lambda X: X ** 2, my_list)]
print(my_list)

