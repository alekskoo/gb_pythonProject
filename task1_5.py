revenue = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

profit = revenue - costs

if profit < 0:
    print("По итогам периода у вас убыток")
elif profit == 0:
    print("По итогам периода нет ни прибыли, ни убытка")
else:
    profitability = profit / revenue * 100
    print(f"Рентабельность составляет {profitability:.2f}%")
    persons = int(input("Веедите численность сотрудников: "))
    pr_to_person = profit / persons
    print(f"Прибыль на 1 сотрудника = {pr_to_person:.2f} Р")




