from functools import reduce

list1 = [int(el) for el in range(100, 1001, 2)]
print(list1)


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, list1))
