list1 = []

list1.append("Name")
list1.append(2)
list1.append(True)
list1.append((1, False))
list1.append([1, 2])
list1.append({"1": "3", "2": "Imagine"})

for i, el in enumerate(list1, 1):
    print(f"{i}: {el} - {type(el)}")
