class TreeObject:
    name = str
    value = float

    def __init__(self, name: str = '', value: float = 0):
        self.name = name
        self.value = value

    def __gt__(self, other: 'TreeObject'):
        return self.value > other.value

    def __lt__(self, other: 'TreeObject'):
        return self.value < other.value

    def __eq__(self, other: 'TreeObject'):
        return self.value == other.value

    def __ge__(self, other: 'TreeObject'):
        return self.value >= other.value

    def __le__(self, other: 'TreeObject'):
        return self.value <= other.value

    def __ne__(self, other: 'TreeObject'):
        return self.value != other.value


class Tree:
    data: TreeObject
    left: 'Tree'
    right: 'Tree'

    def __init__(self, data: TreeObject, left: 'Tree' = None, right: 'Tree' = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        tree_str = '{'
        tree_str += f'"name":"{self.data.name}"'
        tree_str += f',"value":"{str(self.data.value)}"'
        # left
        tree_str += ',"left":'
        if self.left is not None:
            tree_str += str(self.left)
        else:
            tree_str += '"None"'
        # right
        tree_str += ',"right":'
        if self.right is not None:
            tree_str += str(self.right)
        else:
            tree_str += '"None"'
        tree_str += '}'
        return tree_str

    def __gt__(self, other: 'Tree'):
        return self.data > other.data

    def __lt__(self, other: 'Tree'):
        return self.data < other.data

    def __eq__(self, other: 'Tree'):
        return self.data == other.data

    def __ge__(self, other: 'Tree'):
        return self.data >= other.data

    def __le__(self, other: 'Tree'):
        return self.data <= other.data

    def __ne__(self, other: 'Tree'):
        return self.data != other.data


def test_tree():
    tree = Tree(TreeObject('a', 5), Tree(TreeObject('b', 2)), Tree(TreeObject('c', 7)))
    print(tree)


if __name__ == '__main__':
    test_tree()
