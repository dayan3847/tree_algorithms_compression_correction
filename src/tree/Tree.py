from pyswip import Prolog

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
        print(self.data.value, end="")
        if None is not self.right:
            self.right.in_order_tour()

    def preorder_tour(self, tree: 'Tree'):
        if tree:
            print(tree.data.value, end=", ")
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
            print(tree.data.value, end=", ")

    def broad_tour(self, nodes: list['Tree']):

        if len(nodes) == 0:
            return

        for node in nodes:
            if node is not None:
                print(node.data.value, end=", ")
        print()

        children = []
        for node in nodes:
            if node is not None:
                children.append(node.left)
                children.append(node.right)

        self.broad_tour(children)

    def get_level(self) -> int:
        left_level: int = 0 if self.left is None else self.left.get_level()
        right_level: int = 0 if self.right is None else self.right.get_level()
        return max(left_level, right_level) + 1


def test_tree():
    tree = Tree(TreeObject('c', 12))

    print(tree)

    tree.add_new_vertex(Tree(TreeObject('b', 6)), tree)
    tree.add_new_vertex(Tree(TreeObject('a', 2)), tree)
    tree.add_new_vertex(Tree(TreeObject('d', 14)), tree)
    tree.add_new_vertex(Tree(TreeObject('e', 8)), tree)
    tree.add_new_vertex(Tree(TreeObject('f', 10)), tree)
    tree.add_new_vertex(Tree(TreeObject('g', 4)), tree)
    tree.add_new_vertex(Tree(TreeObject('h', 18)), tree)
    tree.add_new_vertex(Tree(TreeObject('i', 16)), tree)
    tree.add_new_vertex(Tree(TreeObject('j', 20)), tree)

    prolog = Prolog()

    prolog.consult("../file_manager/prolog_bd.pl")

    close_menu = False
    while not close_menu:
        print("1. Añadir un vértice.")
        print("2. Buscar un vértices.")
        print("3. Eliminar un vértices.")
        print("4. Buscar adyacentes a un vértices.")
        print("5. Recorrer en orden.")
        print("6. Recorrer en preorden.")
        print("7. Recorrer en prefundidad.")
        print("8. Recorrer a lo ancho.")
        print("9. Determinar si un nodo es padre de otro.")
        print("10. Determinar si un nodo es hoja.")
        print("11. Salir.")
        option = int(input("Selecicone una opcion: "))

        tree_prolog = 'tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil,tree(10,nil,nil))),' \
                      'tree(14,nil,tree(18,tree(16,nil,nil),tree(20,nil,nil)))) '

        if option == 1:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                character = input("Introduzca una letra para nombrar al vértice: ")
                value = int(input("Introduzca un valor para el vértice: "))
                tree.add_new_vertex(Tree(TreeObject(character, value)), tree)
            elif option == 2:
                value = input("Introduzca un valor para el vértice: ")
                temp = f"insert({value}, {tree_prolog}, NewTree) "
                result = list(prolog.query(temp))
                print(result)

        elif option == 2:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                character = input("Introduzca la letra del vértice: ")
                value = int(input("Introduzca el valor del vértice: "))
                print(tree.exists_vertex(Tree(TreeObject(character, value)), tree))
            elif option == 2:
                value = input("Introduzca un valor para el vértice: ")
                temp = "exists(" + value + ",) "
                result = bool(list(prolog.query(temp)))
                print(result)

        elif option == 3:
            character = input("Introduzca la letra del vértice: ")
            value = int(input("Introduzca el valor del vértice: "))
            tree.delete_vertex(Tree(TreeObject(character, value)), tree)
            print(tree)

        elif option == 4:
            character = input("Introduzca la letra del vértice: ")
            value = int(input("Introduzca el valor del vértice: "))
            result = tree.adjacent_vertexes(Tree(TreeObject(character, value)), tree)
            for i in result:
                if i is not None:
                    print(i.data.value)

        elif option == 5:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                tree.in_order_tour()
            elif option == 2:
                result = list(prolog.query("tree(T), inorder(T)"))
                print(result)

        elif option == 6:
            print("1. Usar Python.")
            print("2. Usar Prolog.")
            option = int(input("Selecicone una opcion: "))
            if option == 1:
                tree.preorder_tour(tree)
                print()
            elif option == 2:
                result = list(prolog.query("preorder(tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil,tree(10,nil,"
                                           "nil))),tree(14,nil,tree(18,tree(16,nil,nil),tree(20,nil,nil)))), List)."))
                print(result)

        elif option == 7:
            tree.depth_tour(tree)

        elif option == 8:
            tree.broad_tour([tree])

        elif option == 9:
            value_1 = input("Introduzca un valor para el vértice hijo: ")
            value_2 = input("Introduzca un valor para el vértice padre: ")
            temp = "parent(" + value_2 + "," + value_1 + ",tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil," \
                                                         "tree(10,nil,nil))),tree(14,nil," \
                                                         "tree(18,tree(16,nil,nil),tree(20,nil,nil))))) "
            result = bool(list(prolog.query(temp)))
            print(result)

        elif option == 10:
            value = input("Introduzca un valor para el vértice: ")
            temp = "leaf(" + value + ",tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil,tree(10,nil,nil)))," \
                                     "tree(14,nil,tree(18,tree(16,nil,nil),tree(20,nil,nil))))) "
            result = bool(list(prolog.query(temp)))
            print(result)

        elif option == 11:
            close_menu = True

        print()


if __name__ == '__main__':
    test_tree()
