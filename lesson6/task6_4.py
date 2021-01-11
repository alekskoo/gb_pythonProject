class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Машина {self.name} поехала"

    def stop(self):
        return f"Машина {self.name} остановилась"

    def turn(self, direction):
        return f"Машина {self.name} повернула {direction}"

    def show_speed(self):
        return f"Текущая скорость {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Превышение скорости! Текущая скорость {self.speed}"
        else:
            return f"Текущая скорость {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Превышение скорости! Текущая скорость {self.speed}"
        else:
            return f"Текущая скорость {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


town_car1 = TownCar(55, "Brown", "Mazda")
print(f"Это автомобиль {town_car1.name} цвета {town_car1.color}")
print(town_car1.go())
print(town_car1.turn("направо"))
print(town_car1.show_speed())
print(town_car1.stop())

work_car1 = WorkCar(50, "Red", "Gazelle")
print(f"Это автомобиль {work_car1.name} цвета {work_car1.color}")
print(work_car1.go())
print(work_car1.turn("налево"))
print(work_car1.show_speed())


police_car1 = PoliceCar(150, "Black", "Ford")
print(f"Экипаж на {police_car1.name} со скоростью {police_car1.speed} преследует нарушителя на автомобиле {work_car1.name}")
print(work_car1.stop())