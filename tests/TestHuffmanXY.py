import unittest

from tests import TestHuffman


class TestHuffmanXY(TestHuffman):

    def setUp(self):
        super().setUp()
        self.verbose = True
        self.file_list = [f'../src/file_manager/text_xy.txt']

    def test_generate(self):
        super().test_generate()

    def test_encode(self):
        super().test_encode()

    def test_decode(self):
        super().test_decode()


if __name__ == '__main__':
    unittest.main()
