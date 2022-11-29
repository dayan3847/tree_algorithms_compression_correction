class Tree:
    __value = int
    __left: any  # Tree | None
    __right: any  # Tree | None

    def __init__(self, value: int = 0, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def __str__(self) -> str:
        tree_str = '{'
        # left
        tree_str += '"left":'
        if self.__left is not None:
            tree_str += str(self.__left)
        else:
            tree_str += '"None"'
        tree_str += f',"value":"{str(self.__value)}"'
        # right
        tree_str += ',"right":'
        if self.__right is not None:
            tree_str += str(self.__right)
        else:
            tree_str += '"None"'
        tree_str += '}'
        return tree_str


if __name__ == '__main__':
    tree = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
    print(tree)
