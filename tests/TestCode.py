import unittest

from src.huffman import Code


class TestCode(unittest.TestCase):

    def test1(self):
        print('test1')
        code = Code(1, 4)
        for i in range(code.length):
            code_cloned = code.clone()
            code_cloned.edit_bit(i)
            print(f'Origin: {code} Error: {code_cloned} Bit: {i}')

    def test2(self):
        print('test2')
        code = Code.get_code_from_string('110')
        print(code)
        code.length = 8
        print(code)


if __name__ == '__main__':
    unittest.main()
