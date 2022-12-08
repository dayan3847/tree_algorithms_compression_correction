from pyswip import Prolog

from src import TreeObject


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

    def add_new_vertex(self, new_vertex: 'Tree', tree: 'Tree'):
        if new_vertex <= tree:
            if not tree.left:
                tree.left = new_vertex
                new_vertex.parent = tree
                return
            else:
                self.add_new_vertex(new_vertex, tree.left)
        else:
            if not tree.right:
                tree.right = new_vertex
                new_vertex.parent = tree
                return
            else:
                self.add_new_vertex(new_vertex, tree.right)

    def in_order_tour(self):
        if None is not self.left:
            self.left.in_order_tour()
        print(self.data.value)
        if None is not self.right:
            self.right.in_order_tour()

    def preorder_tour(self, tree: 'Tree'):
        if tree:
            print(tree.data.value)
            self.preorder_tour(tree.left)
            self.preorder_tour(tree.right)

    def exists_vertex(self, vertex: 'Tree', tree: 'Tree') -> 'bool':
        if not tree:
            return False
        elif tree == vertex:
            return True
        elif vertex < tree:
            return self.exists_vertex(vertex, tree.left)
        else:
            return self.exists_vertex(vertex, tree.right)

    def get_vertex(self, vertex: 'Tree', tree: 'Tree') -> 'Tree':
        if not tree:
            return None
        elif tree == vertex:
            return tree
        elif vertex < tree:
            return self.get_vertex(vertex, tree.left)
        else:
            return self.get_vertex(vertex, tree.right)

    def delete_vertex(self, vertex: 'Tree', tree: 'Tree') -> 'Tree':

        found_vertex: 'Tree' = self.get_vertex(vertex, tree)

        if found_vertex.left is None and found_vertex.right is None:
            if found_vertex.parent.left is not None and found_vertex.parent.left == found_vertex:
                found_vertex.parent.left = None
            else:
                found_vertex.parent.right = None
        elif found_vertex.left is None:
            self.transplant(found_vertex, found_vertex.right, tree)
        elif found_vertex.right is None:
            self.transplant(found_vertex, found_vertex.left, tree)
        else:
            temp: 'Tree' = found_vertex.right
            while temp.left is not None:
                temp = temp.left

            if temp.parent != found_vertex:
                self.transplant(temp, temp.right, tree)
                temp.right = found_vertex.right
                temp.right.parent = temp
            self.transplant(found_vertex, temp, tree)
            temp.left = found_vertex.left
            temp.left.parent = temp
            if found_vertex.parent is None:
                return temp
        return tree

    def transplant(self, vertex_a: 'Tree', vertex_b: 'Tree', tree: 'Tree'):
        if vertex_a.parent is not None:
            if vertex_a == vertex_a.parent.left:
                vertex_a.parent.left = vertex_b
            else:
                vertex_a.parent.right = vertex_b

        if vertex_b is not None:
            vertex_b.parent = vertex_a.parent

    def adjacent_vertexes(self, vertex: 'Tree', tree: 'Tree') -> list['Tree']:
        if not tree:
            return []
        elif tree == vertex:
            return [tree.left, tree.right, tree.parent]
        elif vertex < tree:
            return self.adjacent_vertexes(vertex, tree.left)
        else:
            return self.adjacent_vertexes(vertex, tree.right)

    def depth_tour(self, tree: 'Tree'):
        if tree:
            self.depth_tour(tree.left)
            self.depth_tour(tree.right)
            print(tree.data.value)

    def broad_tour(self, nodes: list['Tree']):

        if len(nodes) == 0:
            return

        for node in nodes:
            if node is not None:
                print(node.data.value, end=" ")
        print()

        children = []
        for node in nodes:
            if node is not None:
                children.append(node.left)
                children.append(node.right)

        self.broad_tour(children)


def test_tree():
    tree = Tree(TreeObject('c', 6))

    print(tree)

    tree.add_new_vertex(Tree(TreeObject('b', 3)), tree)
    tree.add_new_vertex(Tree(TreeObject('a', 1)), tree)
    tree.add_new_vertex(Tree(TreeObject('d', 7)), tree)
    tree.add_new_vertex(Tree(TreeObject('e', 4)), tree)
    tree.add_new_vertex(Tree(TreeObject('f', 5)), tree)
    tree.add_new_vertex(Tree(TreeObject('g', 2)), tree)
    tree.add_new_vertex(Tree(TreeObject('h', 9)), tree)
    tree.add_new_vertex(Tree(TreeObject('i', 8)), tree)
    tree.add_new_vertex(Tree(TreeObject('j', 10)), tree)

    print(tree)

    print('in_order_tour')
    tree.in_order_tour()
    print()
    tree.preorder_tour(tree)
    print()
    tree.depth_tour(tree)
    print()
    print(tree.exists_vertex(Tree(TreeObject('g', 2)), tree))
    print()

    adjacent_list: list['Tree'] = tree.adjacent_vertexes(Tree(TreeObject('c', 6)), tree)
    if adjacent_list[0]:
        print("left: " + str(adjacent_list[0].data.value))
    if adjacent_list[1]:
        print("right: " + str(adjacent_list[1].data.value))
    if adjacent_list[2]:
        print("father: " + str(adjacent_list[2].data.value))
    print()

    tree.broad_tour([tree])

    tree = tree.delete_vertex(Tree(TreeObject('a', 1)), tree)
    print(tree)
    print()

    prolog = Prolog()

    prolog.consult("prolog_bd.pl")

    list(prolog.query("level_order([[1,[2,[4,[7,nil,nil],nil],[5,nil,nil]],[3,[6,[8,nil,nil],[9,nil,nil]],nil]]])"))

    """resultado1 = list(prolog.query("exists_vertex(8,T)"))
    print(resultado1)"""


if __name__ == '__main__':
    test_tree()
