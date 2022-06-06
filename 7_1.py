class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for i_2 in range(len(other.matrix[i])):
                self.matrix[i][i_2] = self.matrix[i][i_2] + other.matrix[i][i_2]
        return Matrix.__str__(self)

    def __str__(self):
        return str("\n".join(["\t".join([str(el) for el in i]) for i in self.matrix]))


matrix_1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix_2 = Matrix([[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]])
print(f"Old matrix: \n{matrix_1}")
print(f"New matrix: \n{matrix_1.__add__(matrix_2)}")
