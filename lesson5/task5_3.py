with open("text3.txt", "w", encoding="utf-8") as my_file:
    list1 = []
    while True:
        n = input("Введите фамилию и оклад через пробел: ")
        if len(n) == 0:
            print("Ввод данных завершен")
            break
        elif n.split()[0].isalpha() == False or n.split()[1].replace('.','',1).isdigit() == False:
            print("Ввод данных некорректный!")
            continue
        else:
            list1.append(n + "\n")
    my_file.writelines(list1)
    print("\n\n", "Работники с окладом меньше 20 000 Р: ", sep="", file=my_file)
    for el in list1:
        if float(el.split()[1]) < 20000:
            print(el.split()[0], file=my_file)
    average_value = sum([float(el.split()[1]) for el in list1]) / len(list1)
    print(f"\nСредний оклад по всем работникам: {average_value}", file=my_file)