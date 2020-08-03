from functools import reduce

my_list = [1, 2, 3, 4, 5]

prod = reduce((lambda x, y: x * y), my_list)
print(prod)

greatest = reduce((lambda x, y: y if (y > x) else x), my_list)
print(greatest)
