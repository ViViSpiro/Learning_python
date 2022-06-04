class Road:
    def __init__(self, _length, _width, weight, thickness):
        self._length = _length
        self._width = _width
        self.weight = weight
        self.thickness = thickness

    def mass(self):
        result = self._length * self._width * self.weight * self.thickness / 1000
        print(f"The mass of asphalt is equal to "
              f"{self._length} m * {self._width} m * {self.weight} kg * {self.thickness} cm = ", result, "tons")


r = Road(20, 5000, 25, 5)
r.mass()
