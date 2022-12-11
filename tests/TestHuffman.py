import unittest
import time
from typing import List

from src.huffman import Code
from src.huffman.Huffman import Huffman
from src.file_manager.FileManager import FileManager
from src.file_manager.FrequencyCalculator import FrequencyCalculator


class TestHuffman(unittest.TestCase):
    file_list: List[str]
    file_json_frequency: str
    file_json_codes: str
    verbose: bool

    __path_json__ = '../txt/json/'
    __path_origin__ = '../txt/origin/'
    __path_decode__ = '../txt/decode/'
    __path_bin__ = '../txt/bin/'

    def setUp(self):
        super().setUp()

        self.file_json_frequency = f'{TestHuffman.__path_json__}frequency.json'
        self.file_json_codes = f'{TestHuffman.__path_json__}codes.json'
        self.file_json_tree = f'{TestHuffman.__path_json__}tree.json'
        self.file_list_full_path: List[str] = []
        self.verbose = False

    def get_file_list_full_path(self) -> List[str]:
        if len(self.file_list_full_path) == 0:
            self.file_list_full_path: List[str] = []
            for file in self.file_list:
                self.file_list_full_path.append(f'{TestHuffman.__path_origin__}{file}.txt')

        return self.file_list_full_path

    def test_generate(self):
        if self.verbose:
            print('test_generate')

        frequency_calculator = FrequencyCalculator(self.get_file_list_full_path())

        if self.verbose:
            ts1 = time.time()
            print('Begin: count_symbols')
            frequency_calculator.count_symbols()
            print('End: count_symbols')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

            ts1 = time.time()
            print('Begin: frequency_symbols')
            frequency_calculator.frequency_symbols()
            print('End: frequency_symbols')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

        frequency_json = frequency_calculator.export_json_frequency()
        FileManager.write_txt(self.file_json_frequency, frequency_json)

        frequencies = frequency_calculator.frequency_symbols()
        huffman = Huffman(frequencies)

        if self.verbose:
            ts1 = time.time()
            print('Begin: generate_tree')
            huffman.generate_tree()
            print('End: generate_tree')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

            ts1 = time.time()
            print('Begin: generate_code')
            huffman.generate_code()
            print('End: generate_code')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

        json_codes = huffman.export_json_codes()
        FileManager.write_txt(self.file_json_codes, json_codes)

        json_tree = huffman.export_json_tree()
        FileManager.write_txt(self.file_json_tree, json_tree)

    def test_encode(self):
        if self.verbose:
            print('test_encode')

        frequency_calculator = FrequencyCalculator(self.get_file_list_full_path())

        frequency_json = frequency_calculator.export_json_frequency()
        FileManager.write_txt(self.file_json_frequency, frequency_json)

        frequencies = frequency_calculator.frequency_symbols()
        huffman = Huffman(frequencies)

        codes_json = huffman.export_json_codes()
        FileManager.write_txt(self.file_json_codes, codes_json)

        json_tree = huffman.export_json_tree()
        FileManager.write_txt(self.file_json_tree, json_tree)

        for file in self.file_list:
            text_path = f'{TestHuffman.__path_origin__}{file}.txt'
            text: str = FileManager.read_txt(text_path)

            print()
            ts1 = time.time()
            print(f'Begin: encode file "{file}"')
            encode: Code = huffman.encode(text)
            print(f'End: encode "{file}"')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

            FileManager.write_bin(f'{TestHuffman.__path_bin__}{file}.bin', encode)
            if self.verbose:
                print(f'File: {file}')
                print('Text Read:')
                print('>>>>>>>>>>')
                print(text)
                print('<<<<<<<<<<')
                print(f'Code Write: {encode}\n')

    def test_decode(self):
        if self.verbose:
            print('test_decode')

        frequency_calculator = FrequencyCalculator()

        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)

        huffman = Huffman(frequencies)

        for file in self.file_list:
            encode: Code = FileManager.read_bin(f'{TestHuffman.__path_bin__}{file}.bin')

            print()
            ts1 = time.time()
            print(f'Begin: decode file "{file}"')
            decode: str = huffman.decode(encode)
            print(f'End: decode "{file}"')
            ts2 = time.time()
            print(f'Time: {ts2 - ts1}\n')

            FileManager.write_txt(f'{TestHuffman.__path_decode__}{file}.txt', decode)
            if self.verbose:
                print(f'File: {file}')
                print(f'Code Read: {encode}')
                print('Text Write (Decoded):')
                print('>>>>>>>>>>')
                print(decode)
                print('<<<<<<<<<<')
                print()
