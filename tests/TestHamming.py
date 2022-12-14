import unittest

from src.hamming import Hamming
from src.huffman import Code


class TestHamming(unittest.TestCase):
    def test_encode(self):
        hamming = Hamming()
        code = Code(1, 4)
        print('code')
        print(code)
        encode = hamming.encode(code, True)
        print('encode')
        print(encode)

    def test_decode(self):
        hamming = Hamming()
        code = Code.get_code_from_string('0001100')
        code = Code.get_code_from_string('0001101')
        print('code')
        print(code)
        decode = hamming.decode(code, True)
        print('decode')
        print(decode)

    def test_encode_decode(self):
        print()
        hamming = Hamming()
        code = Code(1, 4)
        encode = hamming.encode(code, True)
        print('encode')
        print(encode)

        print()
        hamming = Hamming()
        encode.edit_bit(1)
        print('encode with error')
        print(encode)
        decode = hamming.decode(encode, True)
        print('decode')
        print(decode)


if __name__ == '__main__':
    unittest.main()
