faster(cat, dog).

t(2, t(1), t(3)).

find(E, t(E, _, _)).

/*tree(t(6, t(3, t(1, nil, t(2, nil, nil)), t(4, nil, t(5, nil, nil))), t(7, nil, t(9, t(8, nil, nil), t(10, nil, nil))))).*/

/*exists_vertex(V, t(V, _, _)).
exists_vertex(V, t(Root, L, _)):- V <= Root, exists_vertex(V, L).
exists_vertex(V, t(Root, _, R)):- V > Root, exists_vertex(V, L).*/

/*add_new_vertex(X, nil, tree(X, nil, nil)).
add_new_vertex(X, tree(X, T1, T2), tree(X, T1, T2)).
add_new_vertex(X, tree(Y, T1, T2), tree(Y, T1N, T2)):- X<Y, add_new_vertex(X, T1, T1N).
add_new_vertex(X, tree(Y, T1, T2), tree(Y, T1, T2N)):- X>Y, add_new_vertex(X, T1, T2N).*/