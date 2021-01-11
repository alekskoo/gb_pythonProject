import time
from colorama import Fore


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        self.__color = self.__color.title()
        if self.__color == "Красный":
            while True:
                print(Fore.RED + "Красный")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                print(Fore.GREEN + "Зеленый")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
        elif self.__color == "Желтый":
            while True:
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                print(Fore.GREEN + "Зеленый")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                print(Fore.RED + "Красный")
                time.sleep(7)
        elif self.__color == "Зеленый":
            while True:
                print(Fore.GREEN + "Зеленый")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
                print(Fore.RED + "Красный")
                time.sleep(7)
                print(Fore.YELLOW + "Желтый")
                time.sleep(2)
        else:
            print("Нет такого цвета в светофоре.")


tl1 = TrafficLight("красный")
tl1.running()
