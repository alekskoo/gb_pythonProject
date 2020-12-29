with open("text1.txt", "a", encoding="utf-8") as my_file:
    while True:
        n = input("Введите строку: ")
        if len(n) == 0:
            print("Ввод завершен")
            break
        else:
            print(n, file=my_file)


