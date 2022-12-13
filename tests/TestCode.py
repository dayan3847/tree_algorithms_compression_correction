import unittest

from src.huffman import Code


class TestCode(unittest.TestCase):

    def test1(self):
        print('test1')
        code = Code(1, 4)
        print(code)
        code.edit_bit(2)
        print(code)

    def test2(self):
        print('test2')
        code = Code.get_code_from_string('110')
        print(code)
        code.length = 8
        print(code)



if __name__ == '__main__':
    unittest.main()
