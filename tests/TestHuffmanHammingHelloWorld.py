import unittest

from tests.TestHuffmanHamming import TestHuffmanHamming


class TestHuffmanHammingHelloWorld(TestHuffmanHamming):

    def setUp(self):
        super().setUp()
        # self.verbose = True
        self.file_list = ['text_hello_world']

    def test_encode(self):
        super().test_encode()

    def test_decode(self):
        super().test_decode()


if __name__ == '__main__':
    unittest.main()
