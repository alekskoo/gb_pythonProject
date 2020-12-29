with open("text_4.txt", "r", encoding="utf-8") as my_file:
    content = [line.rstrip('\n') for line in my_file]
    for el in content:
        print(el)

    new_file = open("text_4_new.txt", "w", encoding="utf-8")
    my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

    for el in content:
        try:
            el = el.title()
            new_el = el.replace(el.split()[0], my_dict.setdefault(el.split()[0]))
            new_file.write(new_el + "\n")
        except TypeError:
            new_file.write(el + " — в словаре нет подходящего значения!\n")
    new_file.close()