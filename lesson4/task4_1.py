from sys import argv

name, time, rate, bonus = argv

def my_func():
    try:
        pay = int(time) * int(rate) + int(bonus)
        return pay
    except ValueError:
        return "Задайте целочисленные значения!"


print(my_func())
