from src.huffman.Code import Code
from src.huffman.Encode import Encode
from src.tree import Tree, TreeObject


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

    def generate_tree(self, verbose: bool = False) -> Tree:
        if self.tree is not None:
            return self.tree

        my_dict_tree = {}
        for i in self.frequency_dict:
            my_dict_tree[i] = Tree(TreeObject(str(i), float(self.frequency_dict[i])))

        step: int = 1
        while 1 < len(my_dict_tree):
            if verbose:
                print(f'Step {step}')
                for i in my_dict_tree:
                    print(my_dict_tree[i])

            left_index: str = min(my_dict_tree, key=my_dict_tree.get)
            left_node: Tree = my_dict_tree.pop(left_index)
            verbose and print(f'Left: {left_node.data.name} ({left_node.data.value})')

            right_index: str = min(my_dict_tree, key=my_dict_tree.get)
            right_node: Tree = my_dict_tree.pop(right_index)
            verbose and print(f'Right: {right_node.data.name} ({right_node.data.value})')

            new_tree_name: str = ''.join(sorted(f'{left_index}{right_index}'))
            new_tree_value: float = float(left_node.data.value) + float(right_node.data.value)
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

        if tree.right is not None:
            self.__generate_code_recursive(tree.right, code.concat_one_init())

    def encode(self, text: str) -> Encode:
        self.generate_code()

        encoded: Encode = Encode()

        for i in text:
            new_code: Code = self.code_dict[i]
            encoded.add_code(new_code)
        return encoded

    def decode(self, encode: Encode) -> str:
        self.generate_tree()
        decoded_text: str = ''
        current_node: Tree = self.tree
        for code in reversed(encode.codes):
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

    def encode_one_code(self, text: str) -> Code:
        self.generate_code()
        encoded: Code = Code()
        for i in text:
            new_code: Code = self.code_dict[i]
            encoded.concat_init(new_code)
            # encoded = encoded.concat(new_code)
        return encoded

    def decode_one_code(self, code: Code) -> str:
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
