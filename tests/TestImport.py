import unittest

from src.file_manager import FrequencyCalculator, FileManager
from tests import TestHuffman


class TestImport(TestHuffman):

    def setUp(self):
        super().setUp()
        self.verbose = True
        self.file_list = [f'../src/file_manager/text_xy.txt']

    def test_decode(self):
        super().test_decode()

    def test_import(self):
        if self.verbose:
            print('test_decode')

        frequency_calculator = FrequencyCalculator(self.file_list)

        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)


if __name__ == '__main__':
    unittest.main()
