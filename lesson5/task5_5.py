with open("text5.txt", "w", encoding="utf-8") as my_file:
    nums = input("Введите числа через пробел: ")
    s = 0
    for el in nums.split():
        try:
            s += int(el)
        except ValueError:
            print("Должны быть введены только числа!")
    my_file.write(nums + "\nСумма чисел: " + str(s))

