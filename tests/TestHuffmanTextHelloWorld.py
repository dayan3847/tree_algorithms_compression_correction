import unittest

from src.huffman import Encode
from src.huffman.Huffman import Huffman
from src.file_manager.FileManager import FileManager
from src.file_manager.FrequencyCalculator import FrequencyCalculator


class TestHuffmanTextHelloWorld(unittest.TestCase):
    file_txt: str
    file_json_frequency: str
    file_json_codes: str

    def setUp(self):
        super().setUp()
        self.file_txt = f'../src/file_manager/text_hello_world.txt'
        self.file_json_frequency = f'../src/file_manager/frequency.json'
        self.file_json_codes = f'../src/file_manager/codes.json'

    def test_encode(self):
        frequency_calculator = FrequencyCalculator([self.file_txt])

        frequency_json = frequency_calculator.export_json_frequency()
        FileManager.write_txt(self.file_json_frequency, frequency_json)

        frequencies = frequency_calculator.frequency_symbols()
        huffman = Huffman(frequencies)

        codes_json = huffman.export_json_codes()
        FileManager.write_txt(self.file_json_codes, codes_json)

        text: str = FileManager.read_txt(self.file_txt)
        encode: Encode = huffman.encode(text)
        FileManager.write_bin(f'{self.file_txt}.bin', encode)
        print(f'Text Read: {text}')
        print(f'Code Write: {encode}')

    def test_decode(self):
        frequency_calculator = FrequencyCalculator([self.file_txt])

        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)

        huffman = Huffman(frequencies)

        encode: Encode = FileManager.read_bin(f'{self.file_txt}.bin')
        decode: str = huffman.decode(encode)
        FileManager.write_txt(f'{self.file_txt}.bin.txt', decode)
        print(f'Code Read: {encode}')
        print(f'Text Write (Decoded): {decode}')


if __name__ == '__main__':
    unittest.main()
