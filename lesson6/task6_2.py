class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def full_mass(self):
        mass = 25
        depth = 5
        fm = mass * depth * self._l * self._w / 1000
        return f"Потребуется {fm} тонн асфальта"


road1 = Road(5000, 20)
print(road1.full_mass())
