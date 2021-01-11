from drawing import make_red, make_yellow, make_green


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        self.__color = self.__color.title()
        if self.__color == "Красный":
            while True:
                make_red(7)
                make_yellow(2)
                make_green(7)
                make_yellow(2)
        elif self.__color == "Желтый":
            while True:
                make_yellow(2)
                make_green(7)
                make_yellow(2)
                make_red(7)
        elif self.__color == "Зеленый":
            while True:
                make_green(7)
                make_yellow(2)
                make_red(7)
                make_yellow(2)
        else:
            print("Нет такого цвета в светофоре.")


tl1 = TrafficLight("желтый")
tl1.running()
