list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list2 = [list1[el] for el in range(1, len(list1)) if list1[el] > list1[el - 1]]

print(list2)
