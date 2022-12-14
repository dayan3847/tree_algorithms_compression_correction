import unittest

from src.file_manager import FileManager
from src.huffman.Code import Code


class TestBin(unittest.TestCase):

    def test_concat(self):
        c1 = Code.get_code_from_string('1001')
        print()
        print(f'c1: {c1}')
        c2 = Code.get_code_from_string('1010')
        print(f'c2: {c2}')
        c3 = c1.concat_init(c2)
        print(f'c3: {c3}')

    def test_bin1(self):
        code1: Code = Code(8, 5)
        code1.concat_init(Code(3, 11))

        code_str1: str = str(code1)
        FileManager.write_bin('./../src/file_manager/test.bin', code1)

        code2: Code = FileManager.read_bin('./../src/file_manager/test.bin')
        code_str2: str = str(code2)
        print()
        print(f'Code1: {code_str1}')
        print(f'Code2: {code_str2}')

        self.assertEqual(code_str1, code_str2)


if __name__ == '__main__':
    unittest.main()
