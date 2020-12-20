n = int(input("Cколько товаров вы хотите добавить: "))
my_goods = []
summary = {"название": [], "цена": [], "количество": [], "ед": []}

for i in range(1, n+1):
    name = input(f"Введите название товара {i}: ")
    price = int(input(f"Введите цену товара {i}: "))
    q = int(input(f"Введите кол-во товара {i}: "))
    c = input(f"Введите единицу измерения товара {i}: ")
    position = {"название": name, "цена":price, "количество":q, "ед":c}
    my_goods.append((i, position))
    summary["название"].append(name) if summary["название"].count(name) == 0 else True
    summary["цена"].append(price) if summary["цена"].count(price) == 0 else True
    summary["количество"].append(q) if summary["количество"].count(q) == 0 else True
    summary["ед"].append(c) if summary["ед"].count(c) == 0 else True

print(my_goods)
print(summary)
