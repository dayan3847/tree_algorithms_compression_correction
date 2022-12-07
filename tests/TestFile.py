import unittest


class TestFile(unittest.TestCase):

    def test_file1(self):
        file_name = 'file.bin'

        # 1 x 8
        s = "10101010"

        'text_fernando_del_paso_palinuro_de_mexico'

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
