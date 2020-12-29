with open("text2.txt", "w", encoding="utf-8") as my_file:
    count = 0
    while True:
        n = input("Введите строку: ")
        if len(n) == 0:
            print("Ввод завершен")
            break
        else:
            print(f"{n} — {len(n.split())} слов", file=my_file)
            count += 1
    print(f"\nКоличество строк: {count}", file=my_file)



