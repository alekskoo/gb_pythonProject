def my_func(a, b, c):
    try:
        my_list = [float(a), float(b), float(c)]
        my_list.remove(min(my_list))
        return sum(my_list)
    except ValueError:
        return "Введите число!"


print(my_func(input("Введите число а: "), input("Введите число b: "), input("Введите число c: ")))
