import unittest

from src.file_manager import FileManager
from src.huffman.Code import Code


class TestBin(unittest.TestCase):

    def test_bin1(self):
        code: Code = Code(8, 5)
        code.concat_init(Code(3, 11))

        code_str: str = str(code)
        FileManager.write_bin('./../src/file_manager/test.bin', code)

        code2: Code = FileManager.read_bin('./../src/file_manager/test.bin')
        code_str2: str = str(code2)
        print()
        print(f'Code: {code_str}')
        print(f'Code2: {code_str2}')

        self.assertEqual(code_str, code_str2)


if __name__ == '__main__':
    unittest.main()
