import numpy as np
import os


class MixinToFile:
    def obg_to_file(self, file_path):
        with open(file_path, "w") as file:
            file.write(str(self))


class MixinStr:
    def __str__(self):
        return "[" + "\n ".join(
            "[" + (" ".join(str(element) for element in string) + "]") for string in self.data) + "]"


class MixinGetterSetter:
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, new_data):
        new_data = [[element for element in row] for row in new_data]
        assert (type(new_data) is list and
                all(map(lambda x: type(x) is list, new_data)))
        self._data = new_data


class MixinMatrix(MixinToFile, MixinStr, MixinGetterSetter, np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, data):
        self.data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        outputs = kwargs.get("out", None)
        if outputs is not None:
            return NotImplemented
        inputs = [obj.data if isinstance(obj, MixinMatrix) else obj for obj in inputs]
        result = None
        if method == "__call__":
            result = getattr(ufunc, method)(*inputs, **kwargs)
        return MixinMatrix(result.tolist()) if result is not None else None


np.random.seed(0)
matrix1_np = np.random.randint(0, 10, (10, 10))
matrix2_np = np.random.randint(0, 10, (10, 10))
matrix1 = MixinMatrix(matrix1_np)
matrix2 = MixinMatrix(matrix2_np)

result_addition = matrix1 + matrix2
result_element_wise_mul = matrix1 * matrix2
result_matrix_mul = matrix1 @ matrix2

os.mkdir("3.2")

result_addition.obg_to_file(r".\3.2\matrix+.txt")
result_element_wise_mul.obg_to_file(r".\3.2\matrix_element_wise_mul.txt")
result_matrix_mul.obg_to_file(r".\3.2\matrix@.txt")
