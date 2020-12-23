def my_func():
    full_sum = 0
    while True:
        s = input("Введите цифры, разделенные пробелом. \nДля выхода введите q: ")
        subsum = 0
        for el in s.split():
            if el == "q":
                print("Выход по q")
                return f"{subsum} ({full_sum})"
            else:
                try:
                    subsum += int(el)
                    full_sum += int(el)
                except ValueError:
                    print("Для выхода введите q!")
        print(f"{subsum} ({full_sum})")


print(my_func())
