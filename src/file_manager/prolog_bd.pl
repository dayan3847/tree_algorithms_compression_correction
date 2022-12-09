
tree(12,tree(6,tree(2,nil,tree(4,nil,nil)),tree(8,nil,tree(10,nil,nil))),tree(14,nil,tree(18,tree(16,nil,nil),tree(20,nil,nil)))).

%% exists in tree
%% insert(Node, Tree)
exists(Node, tree(Node, _, _)) :- !.
exists(Node, tree(_, Left, _)) :- exists(Node, Left), !.
exists(Node, tree(_, _, Right)) :- exists(Node, Right), !.
% exists(6,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).
% exists(9,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).
% exists(2,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% is parent
% parent(Parent, Child, Tree)
parent(Parent, Child, tree(Parent, Left, _)) :- exists(Child, Left), !.
parent(Parent, Child, tree(Parent, _, Right)) :- exists(Child, Right), !.
parent(Parent, Child, tree(_, Left, _)) :- parent(Parent, Child, Left), !.
parent(Parent, Child, tree(_, _, Right)) :- parent(Parent, Child, Right), !.
% parent(3,5,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% is a leaf node
% leaf(Leaf, Tree)
leaf(Leaf, tree(Leaf, nil, nil)) :- !.
leaf(Leaf, tree(_, Left, _)) :- leaf(Leaf, Left), !.
leaf(Leaf, tree(_, _, Right)) :- leaf(Leaf, Right), !.
% leaf(2,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil))))).

% insert a node
% insert(Node, Tree, NewTree)
insert(Node, tree(Parent, nil, Right ), tree(Parent, tree(Node, nil, nil), Right)) :- Node < Parent, !.
insert(Node, tree(Parent, Left, nil ), tree(Parent, Left, tree(Node, nil, nil))) :- Node > Parent, !.
insert(Node, tree(Parent, Left, Right), tree(Parent, NewLeft, Right)) :- Node < Parent, insert(Node, Left, NewLeft), !.
insert(Node, tree(Parent, Left, Right), tree(Parent, Left, NewRight)) :- Node > Parent, insert(Node, Right, NewRight), !.
% insert(99,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).
% insert(4.5,tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), NewTree).

% preorder
% preorder(Tree, List)
preorder(nil, []) :- !.
preorder(tree(Node, Left, Right), [Node|List]) :- preorder(Left, LeftList), preorder(Right, RightList), append(LeftList, RightList, List), !.
% preorder(tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))), List).



%preorder(nil, []).
%preorder(tree(Root, Left, Right), [Root|List]) :-
%    preorder(Left, LeftList),
%    preorder(Right, RightList),
%    append(LeftList, RightList, List).
%
%% inorder
%inorder(nil, []).
%inorder(tree(Root, Left, Right), List) :-
%    inorder(Left, LeftList),
%    inorder(Right, RightList),
%    append(LeftList, [Root|RightList], List).
%
%% insert
%insert(X, nil, tree(X, nil, nil)).
%insert(X, tree(Root, Left, Right), tree(Root, NewLeft, Right)) :-
%    X =< Root,
%    insert(X, Left, NewLeft).
%insert(X, tree(Root, Left, Right), tree(Root, Left, NewRight)) :-
%    X > Root,
%    insert(X, Right, NewRight).



%find(E, t(E, _, _)).
%find(E, t(Root, L, _)):- E < Root, find(E, L).
%find(E, t(Root, _, R)):- E > Root, find(E, R).
%
%create([], nil).
%create(List, t(M, L, R)):-
%    length(List, List_Length),
%    Mid is List_Length div 2,
%    length(List_1, Mid),
%    append(List_1, [M|List_2], List),
%    create(List_1, L),
%    create(List_2, R).
%
%broad_tour(t(nil, nil, nil), nil).
%broad_tour(t(E, nil, nil), E).
%broad_tour(t(E, L, R), [E|Children]):-
%    append(L, R, Concat),
%    broad_tour(Concat, Children).
%
%
%tree1(t(2, t(1, nil, nil), t(3, nil, nil))).
%
%/*tree(t(6, t(3, t(1, nil, t(2, nil, nil)), t(4, nil, t(5, nil, nil))), t(7, nil, t(9, t(8, nil, nil), t(10, nil, nil))))).*/
%
%/*exists_vertex(V, t(V, _, _)).
%exists_vertex(V, t(Root, L, _)):- V <= Root, exists_vertex(V, L).
%exists_vertex(V, t(Root, _, R)):- V > Root, exists_vertex(V, L).*/
%
%/*add_new_vertex(X, nil, tree(X, nil, nil)).
%add_new_vertex(X, tree(X, T1, T2), tree(X, T1, T2)).
%add_new_vertex(X, tree(Y, T1, T2), tree(Y, T1N, T2)):- X<Y, add_new_vertex(X, T1, T1N).
%add_new_vertex(X, tree(Y, T1, T2), tree(Y, T1, T2N)):- X>Y, add_new_vertex(X, T1, T2N).*/
%
%tree([1,[2,[4,[7,nil,nil],nil],[5,nil,nil]],[3,[6,[8,nil,nil],[9,nil, nil]],nil]]).
%
%preorder(nil).
%preorder([Node, FG, FD]) :-
%	format('~w ', [Node]),
%	preorder(FG),
%	preorder(FD).
%
%inorder(nil).
%inorder([Node, FG, FD]) :-
%	inorder(FG),
%	format('~w ', [Node]),
%	inorder(FD).
%
%postorder(nil).
%postorder([Node, FG, FD]) :-
%	postorder(FG),
%	postorder(FD),
%	format('~w ', [Node]).
%
%level_order([]).
%
%level_order(A) :-
%	level_order_(A, U-U, S),
%	level_order(S).
%
%level_order_([], S-[],S).
%
%level_order_([[Node, FG, FD] | T], CS, FS) :-
%	format('~w ', [Node]),
%	append_dl(CS, [FG, FD|U]-U, CS1),
%	level_order_(T, CS1, FS).
%
%level_order_([nil | T], CS, FS) :-
%	level_order_(T, CS, FS).
%
%append_dl(X-Y, Y-Z, X-Z).