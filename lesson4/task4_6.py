# ------------------------ A ----------------------------

from itertools import count

a = int(input("Введите стартовое число: "))
b = int(input("Введите конечное число: "))

for el in count(a):
    if el > b:
        break
    else:
        print(el)

# ------------------------ Б ----------------------------

from itertools import cycle

list1 = [n for n in input("Введите элементы списка через пробел: ").split()]
print(list1)
с = 1
for el in cycle(list1):
    if с > 3 * len(list1):
        break
    print(el)
    с += 1
