import unittest

from src.file_manager.FileManager import FileManager


class TestFile(unittest.TestCase):

    def test_read_txt(self):
        text1 = FileManager.read_txt('../src/file_manager/text_hello_world.txt')
        print(text1)
        text2 = FileManager.read_txt('../src/file_manager/text_alejo_carpentier_los_pasos_perdidos.txt')
        print(text2)

    def test_file1(self):
        file_name = 'file.bin'

        # 1 x 8
        s = "10101010"

        i = 0
        buffer = bytearray()
        while i < len(s):
            buffer.append(int(s[i:i + 8], 2))
            i += 8

        # now write your buffer to a file
        with open(file_name, 'bw') as f:
            f.write(buffer)

        # read the file
        with open(file_name, 'br') as f:
            data = f.read()
            print(data)
            # now convert the data to a string
            s2 = ''.join(format(x, '08b') for x in data)
            print(s2)

        self.assertEqual(s, s2)


if __name__ == '__main__':
    unittest.main()
