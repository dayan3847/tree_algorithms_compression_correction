
tree(6,tree(3,tree(1,nil,tree(2,nil,nil)),tree(4,nil,tree(5,nil,nil))),tree(7,nil,tree(9,tree(8,nil,nil),tree(10,nil,nil)))).

% is parent
% no search other results
parent(Parent, Child) :- tree(Parent, tree(Child,_,_), _); tree(Parent, _, tree(Child,_,_)).
parent(Parent, Child) :- parent(Parent, X), parent(X, Child).

% es un nodo hoja
leaf(Leaf) :- tree(Leaf, nil, nil).

% es un nodo interno
internal(Internal) :- tree(Internal, _, _).
internal(Internal) :- tree(Internal, _, _), not(leaf(Internal)).

% preorder
preorder(nil, []).
preorder(tree(Root, Left, Right), [Root|List]) :-
    preorder(Left, LeftList),
    preorder(Right, RightList),
    append(LeftList, RightList, List).

% inorder
inorder(nil, []).
inorder(tree(Root, Left, Right), List) :-
    inorder(Left, LeftList),
    inorder(Right, RightList),
    append(LeftList, [Root|RightList], List).

% insert
insert(X, nil, tree(X, nil, nil)).
insert(X, tree(Root, Left, Right), tree(Root, NewLeft, Right)) :-
    X =< Root,
    insert(X, Left, NewLeft).
insert(X, tree(Root, Left, Right), tree(Root, Left, NewRight)) :-
    X > Root,
    insert(X, Right, NewRight).



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