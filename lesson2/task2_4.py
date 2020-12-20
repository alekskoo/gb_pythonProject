s = input("Введите несколько слов: ")

for i in range(len(s.split())):
    print (f"{i+1}: {s.split()[i][:10]}")

# ---------------ИЛИ------------------

s = input("Введите несколько слов: ")

for ind, el in enumerate(s.split(), 1):
    print(ind, el[:10])
