import numpy as np
import os


class Matrix:
    def __init__(self, data):
        self.data = [list(row) for row in data]

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix shapes don't match for addition")
        return Matrix([[self.data[j][i] + other.data[j][i] for i in range(len(self.data[0]))]
                       for j in range(len(self.data))])

    def __mul__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Matrix shapes don't match for element-wise multiplication")
        return Matrix([[self.data[j][i] * other.data[j][i] for i in range(len(self.data[0]))]
                       for j in range(len(self.data))])

    def __matmul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrix shapes don't match for matrix multiplication")
        return Matrix([[sum([self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))])
                        for j in range(len(other.data[0]))] for i in range(len(self.data))])

    def __str__(self):
        return "[" + "\n ".join("[" + (" ".join(str(element) for element in string) + "]") for string in self.data) + "]"


np.random.seed(0)
matrix1_np = np.random.randint(0, 10, (10, 10))
matrix2_np = np.random.randint(0, 10, (10, 10))
matrix1 = Matrix(matrix1_np)
matrix2 = Matrix(matrix2_np)

result_addition = matrix1 + matrix2
result_element_wise_mul = matrix1 * matrix2
result_matrix_mul = matrix1 @ matrix2

os.mkdir("3.1")

with open(r".\3.1\matrix+.txt", "w") as file:
    file.write(str(result_addition))

with open(r".\3.1\matrix_element_wise_mul.txt", "w") as file:
    file.write(str(result_element_wise_mul))

with open(r".\3.1\matrix@.txt", "w") as file:
    file.write(str(result_matrix_mul))
