class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки."


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Рисую ручкой."


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Рисую карандашом."


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f"Рисую маркером."


pen1 = Pen("Parker")
print(pen1.draw())

pencil1 = Pencil("Koh-i-Noor")
print(pencil1.draw())

handle1 = Handle("Super")
print(handle1.draw())