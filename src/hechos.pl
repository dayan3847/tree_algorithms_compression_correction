faster(cat,dog).
faster(car,dog).
faster(plain,dog).
faster(light,sound).
faster(cheetah,tiger).

slower(X,Y):- faster(Y,X).
