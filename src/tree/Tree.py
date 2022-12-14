from src.tree.TreeObject import TreeObject


class Tree:
    data: TreeObject
    left: 'Tree'
    right: 'Tree'
    parent: 'Tree'

    def __init__(self, data: TreeObject, left: 'Tree' = None, right: 'Tree' = None, parent: 'Tree' = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

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
