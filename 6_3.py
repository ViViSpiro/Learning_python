class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


p = Position("Arya", "Stark", "assassin", 1000, 500)
print(f"Full name - {p.get_full_name()}.")
print(f"Position - {p.position}.")
print(f"Total income - {p.get_total_income()}.")
