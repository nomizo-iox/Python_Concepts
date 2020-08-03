"""
In Python, functional programming is done like this:
    lambda arguments : expression
"""

power = lambda a, b: a ** b
print(power(3, 5))


def power(a, b):
    return a ** b


print(power(49, 58))

my_list = [1, 2, 3, 4, 5]
avg = lambda L: sum(L) / len(L)
print(avg(my_list))

