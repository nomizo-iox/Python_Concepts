my_list = [1, 2, 3, 4, 5]

odds = [*filter((lambda X: X % 2), my_list)]
print(odds)
