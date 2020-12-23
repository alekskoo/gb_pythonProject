def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Ошибка. Введите положительное число x и целое отрицательное y"
        else:
            return round(x ** y, 5)
    except ValueError:
        return "Ошибка. Введите положительное число x и целое отрицательное y"


print(my_func(input("Введите положительное число x: "), input("Введите целое отрицательное число y: ")))


# ---------------------ИЛИ----------------------------

def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Ошибка. Введите положительное число x и целое отрицательное y"
        else:
            m = 1
            i = 1
            while i <= abs(y):
                m *= x
                i += 1
            return round(1 / m, 5)
    except ValueError:
        return "Ошибка. Введите положительное число x и целое отрицательное y"


print(my_func(input("Введите положительное число x: "), input("Введите целое отрицательное число y: ")))
