class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return self.cells + other.cells

    def __sub__(self, other):
        sub = self.cells - other.cells
        return sub if sub > 0 else "The number of cells in a cell cannot be less than zero!"

    def __mul__(self, other):
        return self.cells * other.cells

    def __truediv__(self, other):
        return self.cells // other.cells

    def make_order(self, row):
        result = ""
        for i in range(int(self.cells / row)):
            result += "*" * row + "\n"
        result += "*" * (self.cells % row) + "\n"
        return result


cell_1 = Cell(13)
cell_2 = Cell(7)
print(f"Addition. Number of cells: {cell_1.__add__(cell_2)}.")
print(f"Subtraction. Number of cells: {cell_1.__sub__(cell_2)}.")
print(f"Multiplication. Number of cells: {cell_1.__mul__(cell_2)}.")
print(f"Division. Number of cells: {cell_1.__truediv__(cell_2)}.")
print(cell_1.make_order(6))
