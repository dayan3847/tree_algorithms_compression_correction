import unittest
import time
from typing import List

import pytest as pytest

from src.huffman import Encode
from src.huffman.Huffman import Huffman
from src.file_manager.FileManager import FileManager
from src.file_manager.FrequencyCalculator import FrequencyCalculator


class TestHuffman(unittest.TestCase):
    file_list: List[str]
    file_json_frequency: str
    file_json_codes: str
    verbose: bool

    def setUp(self):
        super().setUp()
        self.file_json_frequency = f'../src/file_manager/frequency.json'
        self.file_json_codes = f'../src/file_manager/codes.json'
        self.file_json_tree = f'../src/file_manager/tree.json'
        self.verbose = False

    def test_generate(self):
        if self.verbose:
            print('test_generate')

        frequency_calculator = FrequencyCalculator(self.file_list)
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

        frequency_calculator = FrequencyCalculator(self.file_list)

        frequency_json = frequency_calculator.export_json_frequency()
        FileManager.write_txt(self.file_json_frequency, frequency_json)

        frequencies = frequency_calculator.frequency_symbols()
        huffman = Huffman(frequencies)

        codes_json = huffman.export_json_codes()
        FileManager.write_txt(self.file_json_codes, codes_json)

        json_tree = huffman.export_json_tree()
        FileManager.write_txt(self.file_json_tree, json_tree)

        for file in self.file_list:
            text: str = FileManager.read_txt(file)
            encode: Encode = huffman.encode(text)
            FileManager.write_bin(f'{file}.bin', encode)
            if self.verbose:
                print(f'File: {file}')
                print('Text Read:')
                print(text)
                print(f'Code Write: {encode}\n')

    def test_decode(self):
        if self.verbose:
            print('test_decode')

        frequency_calculator = FrequencyCalculator(self.file_list)

        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)

        huffman = Huffman(frequencies)

        for file in self.file_list:
            encode: Encode = FileManager.read_bin(f'{file}.bin')
            decode: str = huffman.decode(encode)
            FileManager.write_txt(f'{file}.bin.txt', decode)
            if self.verbose:
                print(f'File: {file}')
                print(f'Code Read: {encode}')
                print('Text Write (Decoded):')
                print(decode)
                print()
