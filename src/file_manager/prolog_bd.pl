
tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil,tree(10,nil,nil))),tree(14,nil,tree(18,tree(16,nil,nil),tree(20,nil,nil)))).

% Find (Ordered Search)
% find(Node, Tree)
find(Node, tree(Node, _, _)) :- !.
find(Node, tree(Parent, Left, _)) :- Node < Parent, find(Node, Left), !.
find(Node, tree(Parent, _, Right)) :- Node > Parent, find(Node, Right), !.
% find(6,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% Parent (Direct Parent)
% parent(Parent, Child, Tree)
parent(Parent, Child, tree(Parent, tree(Child, _, _), _)) :- !.
parent(Parent, Child, tree(Parent, _, tree(Child, _, _))) :- !.
parent(Parent, Child, tree(Root, Left, _)) :- Parent < Root, parent(Parent, Child, Left), !.
parent(Parent, Child, tree(Root, _, Right)) :- Parent > Root, parent(Parent, Child, Right), !.

% Predecessor (Is Predecessor)
% predecessor(Predecessor, Child, Tree)
predecessor(Predecessor, Child, tree(Predecessor, Left, _)) :- find(Child, Left), !.
predecessor(Predecessor, Child, tree(Predecessor, _, Right)) :- find(Child, Right), !.
predecessor(Predecessor, Child, tree(_, Left, _)) :- predecessor(Predecessor, Child, Left), !.
predecessor(Predecessor, Child, tree(_, _, Right)) :- predecessor(Predecessor, Child, Right), !.
% predecessor(3,5,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% adyacent(Node, Adyacents, Tree)
adyacent(Node, append(LeftNode, RightNode, ParentNode), tree(Node, Left, Right)) :- adyacent(Left, AdyacentsLeft), adyacent(Right, AdyacentsRight), append(AdyacentsLeft, AdyacentsRight, Adyacents), !.

% Leaf (Is a leaf node)
% leaf(Leaf, Tree)
leaf(Leaf, tree(Leaf, nil, nil)) :- !.
leaf(Leaf, tree(_, Left, _)) :- leaf(Leaf, Left), !.
leaf(Leaf, tree(_, _, Right)) :- leaf(Leaf, Right), !.
% leaf(2,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% Level (Level of a Tree)
% level(Level, Tree)
level(0, nil) :- !.
level(max(LeftLevel, RightLevel) + 1, tree(_, Left, Right)) :- level(LeftLevel, Left), level(RightLevel, Right), !.
% level(Level,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% Insert (Insert a node)
% insert(Node, Tree, NewTree)
insert(Node, tree(Parent, nil, Right ), tree(Parent, tree(Node, nil, nil), Right)) :- Node < Parent, !.
insert(Node, tree(Parent, Left, nil ), tree(Parent, Left, tree(Node, nil, nil))) :- Node > Parent, !.
insert(Node, tree(Parent, Left, Right), tree(Parent, NewLeft, Right)) :- Node < Parent, insert(Node, Left, NewLeft), !.
insert(Node, tree(Parent, Left, Right), tree(Parent, Left, NewRight)) :- Node > Parent, insert(Node, Right, NewRight), !.
% insert(99,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).
% insert(4.5,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).

% Delete a node
% delete(Node, Tree, NewTree)
delete(Node, tree(Node, nil, nil), nil) :- !.
delete(Node, tree(Node, Left, nil), Left) :- !.
delete(Node, tree(Node, nil, Right), Right) :- !.
delete(Node, tree(Node, Left, Right), tree(Parent, NewLeft, Right)) :- find(Parent, Left), delete(Parent, Left, NewLeft), !.
delete(Node, tree(Node, Left, Right), tree(Parent, Left, NewRight)) :- find(Parent, Right), delete(Parent, Right, NewRight), !.
delete(Node, tree(Parent, Left, Right), tree(Parent, NewLeft, Right)) :- Node < Parent, delete(Node, Left, NewLeft), !.
delete(Node, tree(Parent, Left, Right), tree(Parent, Left, NewRight)) :- Node > Parent, delete(Node, Right, NewRight), !.
% delete(9,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).
% delete(6,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).


% Preorder
% preorder(Tree, List)
preorder(nil, []) :- !.
preorder(tree(Node, Left, Right), [Node|List]) :- preorder(Left, LeftList), preorder(Right, RightList), append(LeftList, RightList, List), !.
% preorder(tree(6,nil,nil),List).
% preorder(tree(6,tree(5,nil,nil),nil),List).
% preorder(tree(6,tree(3,tree(1,nil,nil),tree(4,nil,nil)),nil),List).
% preorder(tree(6,tree(3,tree(1,nil,nil),tree(4,nil,nil)),tree(7,nil,tree(9,nil,nil))),List).
% preorder(tree(6,tree(3,tree(1,nil,nil),tree(4,nil,nil)),tree(7,nil,tree(9,nil,tree(10,nil,nil)))),List).
% preorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,nil)),tree(7,nil,tree(9,nil,tree(10,nil,nil)))),List).
% preorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,nil,tree(10,nil,nil)))),List).
% preorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))),List).
% preorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))),List).

% Inorder
% inorder(Tree, List)
inorder(nil, []) :- !.
inorder(tree(Node, Left, Right), List) :- inorder(Left, LeftList), inorder(Right, RightList), append(LeftList, [Node|RightList], List), !.
% inorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))),List).

% Postorder
% postorder(Tree, List)
postorder(nil, []) :- !.
postorder(tree(Node, Left, Right), List) :- postorder(Left, LeftList), postorder(Right, RightList), append(LeftList, RightList, TempList), append(TempList, [Node], List), !.
% postorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))),List).
