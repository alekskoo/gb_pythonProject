def my_func(a, b):
    try:
        return round(float(a) / float(b), 2)
    except (ZeroDivisionError, ValueError) as err:
        return err


print(my_func(input("Введите число а: "), input("Введите число b: ")))
