from src.Tree import Tree, TreeObject


class Huffman:
    # frequency dictionary
    frequency_dict: dict[str, float]
    # tree
    tree: Tree | None
    code_dict: dict[str, str]

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

    def generate_code(self) -> dict:
        if 0 == len(self.code_dict):
            self.__generate_code_recursive(self.tree)
        return self.code_dict

    def __generate_code_recursive(self, tree: Tree, code: str = '') -> None:
        if tree.left is None and tree.right is None:
            self.code_dict[tree.data.name] = code
            return

        if tree.left is not None:
            self.__generate_code_recursive(tree.left, code + '1')

        if tree.right is not None:
            self.__generate_code_recursive(tree.right, code + '0')

    def encode_string(self, text: str) -> str:
        code_dict = self.generate_code()
        encoded_text = ''
        for i in text:
            encoded_text += code_dict[i]
        return encoded_text

    def decode_string(self, encoded_text: str) -> str:
        self.generate_tree()
        decoded_text = ''
        current_node = self.tree
        for i in encoded_text:
            if i == '1':
                current_node = current_node.left
            else:  # i == '0'
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:
                decoded_text += current_node.data.name
                current_node = self.tree

        return decoded_text


def test_huffman():
    my_frequency_dict: dict = {
        "A": 0.10,
        "B": 0.15,
        "C": 0.30,
        "D": 0.16,
        "E": 0.29,
    }

    huffman = Huffman(my_frequency_dict)

    tree = huffman.generate_tree()
    print('Tree:')
    print(tree)

    code_dict = huffman.generate_code()
    print('Codes:')
    print(code_dict)

    encoded_text = huffman.encode_string('ACABADA')
    print('Encoded "ACABADA":')
    print(encoded_text)

    decoded_text = huffman.decode_string(encoded_text)
    print(f'Decoded "{encoded_text}":')
    print(decoded_text)


if __name__ == '__main__':
    test_huffman()
