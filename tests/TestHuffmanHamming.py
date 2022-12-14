import os
import unittest
import time
from typing import List

from src.hamming import Hamming
from src.huffman import Code
from src.huffman.Huffman import Huffman
from src.file_manager.FileManager import FileManager
from src.file_manager.FrequencyCalculator import FrequencyCalculator


class TestHuffmanHamming(unittest.TestCase):
    file_list: List[str]
    file_json_frequency: str
    file_json_codes: str
    verbose: bool

    # Direcciones donde se van a guardar los ficheros
    __path_json__ = '../txt/json/'
    __path_origin__ = '../txt/origin/'
    __path_decode__ = '../txt/decode/'
    __path_bin__ = '../txt/bin/'

    def setUp(self):
        super().setUp()

        self.file_json_frequency = f'{TestHuffmanHamming.__path_json__}frequency.json'
        self.file_json_codes = f'{TestHuffmanHamming.__path_json__}codes.json'
        self.file_json_tree = f'{TestHuffmanHamming.__path_json__}tree.json'
        self.file_list_full_path: List[str] = []
        self.verbose = True
        self.file_list = []
        self.file = 'text_hello_world'

    def get_file_list_full_path(self) -> List[str]:
        if len(self.file_list_full_path) == 0:
            self.file_list_full_path: List[str] = []
            for file in self.file_list:
                self.file_list_full_path.append(f'{TestHuffmanHamming.__path_origin__}{file}.txt')

        return self.file_list_full_path

    def test_calculate_frequencies(self):
        if self.verbose:
            print('\ntest_calculate_frequencies')

        if len(self.file_list) == 0:
            self.file_list = [self.file]

        frequency_calculator = FrequencyCalculator(self.get_file_list_full_path())
        json_frequency = frequency_calculator.export_json_frequency()

        # Create frequency.json file
        FileManager.write_txt(self.file_json_frequency, json_frequency)
        frequencies = frequency_calculator.frequency_symbols()

        huffman = Huffman(frequencies)

        # Create codes
        json_codes = huffman.export_json_codes()
        FileManager.write_txt(self.file_json_codes, json_codes)

        # Create tree
        json_tree = huffman.export_json_tree()
        FileManager.write_txt(self.file_json_tree, json_tree)

    def test_encode(self):
        if self.verbose:
            print('\ntest_encode')

        frequency_calculator = FrequencyCalculator()
        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)

        huffman = Huffman(frequencies)

        hamming = Hamming(self.verbose)

        text_path = f'{TestHuffmanHamming.__path_origin__}{self.file}.txt'
        text: str = FileManager.read_txt(text_path)

        print()
        ts1 = time.time()
        if self.verbose:
            print(f'Begin: encode file "{self.file}"')

        encode_huffman: Code = huffman.encode(text)

        if self.verbose:
            print(f'End: encode "{self.file}"')
        ts2 = time.time()
        if self.verbose:
            print(f'Time: {ts2 - ts1}\n')

        FileManager.write_bin(f'{TestHuffmanHamming.__path_bin__}{self.file}.huffman.bin', encode_huffman)

        if self.verbose:
            print(f'File: {self.file}')
            print('Text Read:')
            print('>>>>>>>>>>')
            print(text)
            print('<<<<<<<<<<')
            print(f'Code Write: {encode_huffman}\n')

        encode_hamming: Code = hamming.encode(encode_huffman)

        FileManager.write_bin(f'{TestHuffmanHamming.__path_bin__}{self.file}.hamming.bin', encode_hamming)

        FileManager.write_bin(f'{TestHuffmanHamming.__path_bin__}Entrada.bin', encode_hamming)

    def test_generate_errors(self):
        if self.verbose:
            print('\ntest_generate_errors')
        # run bash script
        bash_script = 'bash ../txt/bin/script_generate_errors.sh'
        os.system(bash_script)

    def test_decode(self):
        if self.verbose:
            print('\ntest_decode')

        frequency_calculator = FrequencyCalculator()
        frequency_json: str = FileManager.read_txt(self.file_json_frequency)
        frequencies: dict[str, float] = frequency_calculator.import_json_frequency(frequency_json)

        huffman = Huffman(frequencies)
        hamming = Hamming(self.verbose)

        encode: Code = FileManager.read_bin(f'{TestHuffmanHamming.__path_bin__}Salida.bin')

        hamming_decode: Code = hamming.decode(encode)

        if hamming.report:
            FileManager.write_txt(f'{TestHuffmanHamming.__path_bin__}ReporteCorrecciones.txt', hamming.report_text)
        FileManager.write_bin(f'{TestHuffmanHamming.__path_bin__}{self.file}.corrected.bin', hamming_decode)

        print()
        ts1 = time.time()
        if self.verbose:
            print(f'Begin: decode file "{self.file}"')
        decode: str = huffman.decode(hamming_decode)
        if self.verbose:
            print(f'End: decode "{self.file}"')
        ts2 = time.time()
        if self.verbose:
            print(f'Time: {ts2 - ts1}\n')

        FileManager.write_txt(f'{TestHuffmanHamming.__path_decode__}{self.file}.txt', decode)
        if self.verbose:
            print(f'File: {self.file}')
            print(f'Code Read: {encode}')
            print('Text Write (Decoded):')
            print('>>>>>>>>>>')
            print(decode)
            print('<<<<<<<<<<')
            print()

    def test_complete(self):
        self.test_calculate_frequencies()
        self.test_encode()
        self.test_generate_errors()
        self.test_decode()
