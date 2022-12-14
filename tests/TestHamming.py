import unittest

from src.hamming import Hamming
from src.huffman import Code


class TestHamming(unittest.TestCase):
    def test_encode(self):
        hamming = Hamming()
        code = Code(1, 4)
        print('code')
        print(code)
        encode = hamming.encode(code)
        print('encode')
        print(encode)

    def test_decode(self):
        hamming = Hamming()
        code = Code.get_code_from_string('0001100')
        code = Code.get_code_from_string('0001101')
        print('code')
        print(code)
        decode = hamming.decode(code)
        print('decode')
        print(decode)

    def test_encode_decode(self):
        print()
        hamming_encode = Hamming(True)
        code = Code(1, 4)
        encode = hamming_encode.encode(code)
        print('encode')
        print(encode)

        print()
        hamming_decode = Hamming(True)
        encode.edit_bit(4)
        print('encode with error')
        print(encode)
        decode = hamming_decode.decode(encode)
        print('decode')
        print(decode)


if __name__ == '__main__':
    unittest.main()
