import unittest

from src import Huffman, Tree, Code, Encode


class TestHuffman(unittest.TestCase):

    def test_code1(self):
        code = Code(0, 3)
        print(f'code: {code} Base10: {code.code} Length: {code.length}')

        code2 = code.extract(1)
        print(f'code2: {code2} Base10: {code2.code} Length: {code2.length}')

        code2 = Code.get_code_from_string('101')
        print(f'code2: {code2} Base10: {code2.code}')

        self.assertTrue(True)

    def test_huffman1(self):
        my_frequency_dict: dict[str, float] = {
            "A": 0.10,
            "B": 0.15,
            "C": 0.30,
            "D": 0.16,
            "E": 0.29,
        }

        huffman: Huffman = Huffman(my_frequency_dict)

        tree: Tree = huffman.generate_tree()
        print('Tree:')
        print(tree)

        code_dict: dict[str, Code] = huffman.generate_code()
        print('Codes:')
        for i in code_dict:
            print(f'{i}: {code_dict[i]}')

        # text = 'B'
        text: str = 'ACABADA'
        encoded: Encode = huffman.encode(text)
        encoded_string: str = str(encoded)
        print(f'Encoded "{text}": {encoded_string}')
        for code in encoded.codes:
            print(f'Base10: {code.code}, Length: {code.length}')

        decoded_text: str = huffman.decode(encoded)
        print(f'Decoded "{encoded_string}": {decoded_text}')

        encoded2: Code = huffman.encode_one_code(text)
        encoded_string2: str = str(encoded2)
        print(f'Encoded2 "{text}": {encoded_string2}, Base10: {encoded2.code}, Length: {encoded2.length}')

        decoded_text2: str = huffman.decode_one_code(encoded2)
        print(f'Decoded "{encoded_string2}": {decoded_text2}')

        self.assertTrue(True)

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        a = 5
        b = a.to_bytes
        print(b)

        #
        # a = ['a', 'b', 'c', 'd', 'e']
        # a.append('t')
        # a.insert(0, 'r')
        # print(a)
        # a[-1] = 'f'
        # print(a)
        # # get last element

        #
        #
        #
        #
        # a = 257
        # for i in range(10):
        #     print(f'a: {a} : {a:b}')
        #     a >>= 1
        #
        # b = 1
        # for i in range(10):
        #     # add 1 to the end
        #     b <<= 1
        #     b |= 1
        #
        #     print(b)
        #
        # # concatenate 2 bynary numbers
        # c = 1
        # d = 5
        # e = c << d.bit_length() | d
        # print(f'e = {e}')
        #
        # # # get count of bits in number
        # # for i in range(10):
        # #     print(f'{i} = {i.bit_length()}')

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
