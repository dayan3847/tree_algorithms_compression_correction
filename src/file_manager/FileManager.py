import codecs

from src.huffman.Code import Code


class FileManager:

    @staticmethod
    def write_txt(file_name: str, text: str):
        file = codecs.open(file_name, 'w', encoding='utf-8-sig')
        file.write(text)
        file.close()

    @staticmethod
    def read_txt(file_name: str) -> str:
        text: str = ''
        file = codecs.open(file_name, encoding='utf-8-sig')
        for line in file.readlines():
            for x in line:
                text += x
        file.close()

        return text

    @staticmethod
    def write_bin(file_name: str, encode: Code):

        # TODO: try use encode directly
        text: str = str(encode)

        i = 0
        buffer = bytearray()
        while i < len(text):
            buffer.append(int(text[i:i + 8], 2))
            i += 8

        # now write your buffer to a file
        with open(file_name, 'bw') as f:
            f.write(buffer)

    @staticmethod
    def read_bin(file_name: str) -> Code:
        with open(file_name, 'br') as f:
            data = f.read()
            # now convert the data to int array
            int_array = [int.from_bytes(bytes([x]), byteorder='big') for x in data]
            # now convert the data to a string
            # s2 = ''.join(format(x, '08b') for x in data)
        # code = Code.get_code_from_string(s2)
        code: Code = Code()
        for i in reversed(int_array):
            code = code.concat_init(Code(i, 8))

        return code
