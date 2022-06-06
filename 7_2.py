from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def fabric_consumption(self):
        return 2 * self.growth + 0.3


coat = Coat(42, 0)
costume = Costume(0, 1.64)
print(f"To sew a coat, you need {coat.fabric_consumption :.2f} m of fabric.")
print(f"To sew a costume, you need {costume.fabric_consumption() :.2f} m of fabric.")
print(f"Total fabric consumption: {coat.fabric_consumption + costume.fabric_consumption() :.2f}.")
