import unittest

import numpy as np

from src.huffman import Code
from src.matrix import BinaryMatrix


class TestBinaryMatrix(unittest.TestCase):

    # Doc in: https://en.wikipedia.org/wiki/Hamming_code#Construction_of_G_and_H
    def test1(self):
        print('test')

        code = BinaryMatrix(
            [
                [1, 0, 1, 1],
            ],
        )

        k = 4
        n = 7

        k_identity = BinaryMatrix.identity(k)
        print(k_identity)

        matrix_a = BinaryMatrix(
            [
                [1, 1, 0],
                [1, 0, 1],
                [0, 1, 1],
                [1, 1, 1],
            ],
            'A'
        )
        print(matrix_a)

        matrix_g = k_identity.concatenate(matrix_a, 'G')
        print(matrix_g)
        result = code * matrix_g
        print(result)

        matrix_at = matrix_a.transpose()

        n_k_identity = BinaryMatrix.identity(n - k)

        matrix_h = matrix_at.concatenate(n_k_identity, 'H')

        print(matrix_h)

        # result = code * matrix_h
        result = (code * matrix_g).set_name('R')

        print(result)

        bit_error_index = 3
        result.data[0][bit_error_index] = (result.data[0][bit_error_index] + 1) % 2

        print('result with error')
        print(result)
        print('result transpose with error')
        result_transpose = result.transpose()
        print(result_transpose)

        correction = matrix_h * result_transpose
        print('correction')
        print(correction)

    def test2(self):
        BinaryMatrix.consecutive(4, 3)
        BinaryMatrix.consecutive(8, 8)

    def test3(self):
        code = Code(1, 4)
        m = BinaryMatrix.gen_matrix_from_code(code)
        print('m')
        print(m)

        code = Code(1, 4)
        m = BinaryMatrix.gen_matrix_from_code(code, True)
        print('m')
        print(m)

    def test4(self):
        identity = BinaryMatrix.identity(4)
        print(identity)
        identity_opposite = identity.opposite()
        print(identity_opposite)
        matrix_g = identity.concatenate(identity_opposite, 'G')
        print(matrix_g)



if __name__ == '__main__':
    unittest.main()
