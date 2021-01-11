class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.n} {self.s}"

    def get_total_income(self):
        return f"Суммарный доход: {sum(self._income.values())}"


worker1 = Position("Ivan", "Petrov", "manager", 3500, 1300)
print(worker1.get_full_name())
print(worker1.get_total_income())
