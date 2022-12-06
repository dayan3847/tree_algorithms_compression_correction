from typing import List

from src.Tree import Tree, TreeObject


class Code:
    code: int
    length: int

    def __init__(self, code: int = 0, length: int = 0):
        self.code = code
        if length == 0 and code != 0:
            self.length = code.bit_length()
        else:
            self.length = length

    def __str__(self):
        result = f'{self.code:b}'
        if len(result) < self.length:
            result = '0' * (self.length - len(result)) + result
        return result

    def concat_zero(self) -> 'Code':
        new_code_code = self.code << 1
        return Code(new_code_code, self.length + 1)

    def concat_one(self) -> 'Code':
        new_code_code = self.code << 1 | 1
        return Code(new_code_code, self.length + 1)

    def concat_zero_init(self) -> 'Code':
        return Code(self.code, self.length + 1)

    def concat_one_init(self) -> 'Code':
        new_code_code = 1 << self.length | self.code
        return Code(new_code_code, self.length + 1)

    def concat(self, other: 'Code') -> 'Code':
        new_code_code = self.code << other.length | other.code
        return Code(new_code_code, self.length + other.length)

    def concat_init(self, other: 'Code') -> 'Code':
        new_code_code = other.code << self.length | self.code
        return Code(new_code_code, self.length + other.length)

    @staticmethod
    def get_code_from_string(string_code: str):
        code = int(string_code, 2)
        length = len(string_code)
        return Code(code, length)


class Encode:
    codes: List[Code]

    def __init__(self):
        self.codes = []

    def add_code(self, code: Code):
        if 0 == len(self.codes) or 8 == self.codes[0].length:
            self.codes.insert(0, code)
        else:
            if 8 > self.codes[0].length + code.length:
                self.codes[0] = self.codes[0].concat_init(code)


class Huffman:
    # frequency dictionary
    frequency_dict: dict[str, float]
    # tree
    tree: Tree | None
    code_dict: dict[str, Code]

    def __init__(self, frequency_dict: dict[str, float]):
        self.frequency_dict = frequency_dict
        self.tree = None
        self.code_dict = {}

    def generate_tree(self) -> Tree:
        if self.tree is not None:
            return self.tree

        my_dict_tree = {}
        for i in self.frequency_dict:
            my_dict_tree[i] = Tree(TreeObject(str(i), float(self.frequency_dict[i])))

        step: int = 1
        while 1 < len(my_dict_tree):
            print(f'Step {step}')
            for i in my_dict_tree:
                print(my_dict_tree[i])

            left_index: str = min(my_dict_tree, key=my_dict_tree.get)
            left_node: Tree = my_dict_tree.pop(left_index)
            print(f'Left: {left_node.data.name} ({left_node.data.value})')

            right_index: str = min(my_dict_tree, key=my_dict_tree.get)
            right_node: Tree = my_dict_tree.pop(right_index)
            print(f'Right: {right_node.data.name} ({right_node.data.value})')

            new_tree_name: str = ''.join(sorted(f'{left_index}{right_index}'))
            new_tree_value: float = float(round(left_node.data.value + right_node.data.value, 2))
            new_tree = Tree(TreeObject(new_tree_name, new_tree_value), left_node, right_node)
            my_dict_tree[new_tree.data.name] = new_tree

            step += 1

        self.tree = my_dict_tree.popitem()[1]

        return self.tree

    def generate_code(self) -> dict[str, Code]:
        self.generate_tree()
        if 0 == len(self.code_dict):
            self.__generate_code_recursive(self.tree, Code())
        return self.code_dict

    def __generate_code_recursive(self, tree: Tree, code: Code) -> None:
        if tree.left is None and tree.right is None:
            self.code_dict[tree.data.name] = code
            return

        if tree.left is not None:
            self.__generate_code_recursive(tree.left, code.concat_zero_init())
            # self.__generate_code_recursive(tree.left, code.concat_zero())

        if tree.right is not None:
            self.__generate_code_recursive(tree.right, code.concat_one_init())
            # self.__generate_code_recursive(tree.right, code.concat_one())

    def encode(self, text: str) -> Code:
        self.generate_code()
        encoded: Code = Code()
        for i in text:
            new_code: Code = self.code_dict[i]
            encoded = encoded.concat_init(new_code)
            # encoded = encoded.concat(new_code)
        return encoded

    def decode(self, code: Code) -> str:
        self.generate_tree()
        decoded_text: str = ''
        current_node: Tree = self.tree
        current_code: int = code.code
        for _ in range(code.length):
            if current_code & 1:
                current_node = current_node.right
            else:
                current_node = current_node.left

            if current_node.left is None and current_node.right is None:
                decoded_text += current_node.data.name
                current_node = self.tree

            current_code >>= 1

        return decoded_text


def test_huffman():
    code = Code(0, 3)
    print(f'code: {code} Base10: {code.code}')

    code2 = Code.get_code_from_string('101')
    print(f'code2: {code2} Base10: {code2.code}')

    my_frequency_dict: dict[str, float] = {
        "A": 0.10,
        "B": 0.15,
        "C": 0.30,
        "D": 0.16,
        "E": 0.29,
    }

    huffman = Huffman(my_frequency_dict)

    tree: Tree = huffman.generate_tree()
    print('Tree:')
    print(tree)

    code_dict = huffman.generate_code()
    print('Codes:')
    for i in code_dict:
        print(f'{i}: {code_dict[i]}')

    # text = 'B'
    text = 'ACABADA'
    encoded = huffman.encode(text)
    encoded_string = str(encoded)
    print(f'Encoded "{text}": {encoded_string}, Base10: {encoded.code}, Length: {encoded.length}')

    decoded_text = huffman.decode(encoded)
    print(f'Decoded "{encoded_string}": {decoded_text}')


if __name__ == '__main__':
    test_huffman()
