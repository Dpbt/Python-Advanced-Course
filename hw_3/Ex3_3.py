import os


class MixinHash:
    """
    Данная хэш-функция суммирует все элемнты матрицы.
    """
    def __hash__(self):
        hash_value = sum(sum(row) for row in self.data)
        return int(hash_value)


class Matrix(MixinHash):
    cache = {}

    def __init__(self, data):
        self.data = tuple(tuple(row) for row in data)

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
        hash_key = (hash(self), hash(other))
        if hash_key in Matrix.cache.keys():
            return Matrix(Matrix.cache[hash_key])
        else:
            result = [[sum([self.data[i][k] * other.data[k][j] for k in range(len(self.data[0]))])
                       for j in range(len(other.data[0]))] for i in range(len(self.data))]
            Matrix.cache[hash_key] = result
            return Matrix(result)

    def __str__(self):
        return "[" + "\n ".join("[" + (" ".join(str(element) for element in string) + "]") for string in self.data) + "]"


a = Matrix([[1, 2, 1], [3, 4, 1]])
b = Matrix([[1, 0], [0, 2], [4, 6]])
c = Matrix([[1, 2, 1], [3, 3, 2]])
d = Matrix([[1, 0], [0, 2], [4, 6]])

ab = a @ b
cd = c @ d
Matrix.cache.clear()
cd_true = c @ d
ab_hash = hash(ab)
cd_hash = hash(cd_true)

os.mkdir("3.3")

for file_name, objs in [("A.txt", a), ("B.txt", b), ("C.txt", c), ("D.txt", d), ("AB.txt", ab), ("CD.txt", cd_true)]:
    with open(rf".\3.3\{file_name}", "w") as file:
        file.write(str(objs))

with open(r".\3.3\hash.txt", "w") as file:
    file.write(f"{str(ab_hash)}\n{str(cd_hash)}")
