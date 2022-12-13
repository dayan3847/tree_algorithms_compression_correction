import numpy as np
from numpy import ndarray

from src.huffman import Code


class BinaryMatrix:
    name: str
    data: ndarray

    def __init__(self, data, name: str = ''):
        self.name = name
        # convert to binary
        data_ndarray = np.array(data)
        for i, row in enumerate(data_ndarray):
            for j, item in enumerate(row):
                data_ndarray[i][j] = int(data_ndarray[i][j]) % 2

        self.data = data_ndarray

    def set_name(self, name: str):
        self.name = name
        return self

    def __mul__(self, other: 'BinaryMatrix') -> 'BinaryMatrix':
        npm_result = np.matmul(self.data, other.data)

        return BinaryMatrix(npm_result)

    def __str__(self):
        to_string = ''
        if '' != self.name:
            to_string += f'{self.name}:'
        to_string += '[\n'
        for row in self.data:
            to_string += f'\t{str(row)}\n'
        to_string += ']'

        return to_string

    def concatenate(self, other: 'BinaryMatrix', name: str = '') -> 'BinaryMatrix':
        npm_result = np.concatenate((self.data, other.data), axis=1)

        return BinaryMatrix(npm_result, name)

    def transpose(self) -> 'BinaryMatrix':
        return BinaryMatrix(self.data.transpose(), f'-{self.name}t' if '' != self.name else '')

    def to_code(self, revert: bool = False) -> Code:
        code_str = ''
        for row in self.data:
            for item in row:
                code_str += str(item)
        if revert:
            code_str = code_str[::-1]
        return Code.get_code_from_string(code_str)

    @staticmethod
    def identity(size: int) -> 'BinaryMatrix':
        return BinaryMatrix(np.identity(size, int), f'I{size}')

    @staticmethod
    def consecutive(rows: int, columns: int, name: str = '') -> 'BinaryMatrix':
        result = np.zeros((rows, columns), int)
        for i in range(rows):
            pivot = i + 1
            for j in range(columns):
                jr = columns - j - 1
                result[i][jr] = pivot % 2
                pivot //= 2

        return BinaryMatrix(result, name)

    @staticmethod
    def gen_matrix_from_code(code: Code, col: bool = False) -> 'BinaryMatrix':
        data = []
        code_str = str(code)
        for i in code_str:
            data.append(int(i))
        result = BinaryMatrix([data])
        if col:
            return result.transpose()

        return result
