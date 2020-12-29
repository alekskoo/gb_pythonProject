with open("text_6.txt", "r+", encoding="utf-8") as my_file:
    full_dict = {}
    for line in my_file:
        line_list = [int(''.join(filter(lambda x : x.isdigit(), el))) for el in line.split() if el[0].isdigit() == True]
        line_dict = {line.split()[0].rstrip(":"):sum(line_list)}
        full_dict.update(line_dict)
    print(f"\n\nСводка по предметам: \n{full_dict}", file=my_file)
