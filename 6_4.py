class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"The {self.name} went."

    def stop(self):
        return f"\nThe {self.name} has stopped."

    def turn(self, direction):
        return f"\nThe {self.name} turned {direction}."

    def show_speed(self):
        return f"\nCar speed is {self.speed} km/h."


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"\nSpeed is higher than allowed! Car speed is {self.speed} km/h."
        else:
            return super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"\nSpeed is higher than allowed! Car speed is {self.speed} km/h."
        else:
            return super().show_speed()


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police


t = TownCar("Toyota Aygo", 85, "orange", False)
print("1:\n" + t.go(), t.show_speed(), t.turn("left"), t.turn("right"), t.stop())

s = SportCar("Ferrari 488", 120, "red", False)
print("2:\n" + s.go(), s.show_speed(), s.turn("left"), s.stop())

w = WorkCar("Skoda Octavia", 35, "black", False)
print("3:\n" + w.go(), w.show_speed(), w.turn("right"), w.stop())

p = PoliceCar("Audi A6", 90, "white", True)
print("4:\n" + p.go(), p.show_speed(), p.turn("right"), p.stop())
