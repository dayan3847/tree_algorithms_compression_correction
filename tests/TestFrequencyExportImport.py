import unittest

from src.huffman.Huffman import Huffman
from src.file_manager.FileManager import FileManager
from src.file_manager.FrequencyCalculator import FrequencyCalculator


class TestFrequencyExportImport(unittest.TestCase):
    file_txt: str

    def setUp(self):
        super().setUp()
        self.file_txt = f'../src/file_manager/text_hello_world.txt'
        self.file_frequency_json = f'../src/file_manager/frequency.json'
        # create a frequency calculator
        self.frequency_calculator = FrequencyCalculator([self.file_txt])
        frequencies = self.frequency_calculator.frequency_symbols()
        self.huffman = Huffman(frequencies)

    def test_export_frequency_json(self):
        frequency_json = self.frequency_calculator.export_json_frequency()
        FileManager.write_txt(self.file_frequency_json, frequency_json)
        print('Frequency:')
        print(frequency_json)

    def test_import_frequency_json(self):
        frequency_json: str = FileManager.read_txt(self.file_frequency_json)
        frequencies: dict[str, float] = self.frequency_calculator.import_json_frequency(frequency_json)
        print('Frequency:')
        print(frequencies)


if __name__ == '__main__':
    unittest.main()
