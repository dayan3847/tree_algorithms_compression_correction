from pyswip import Prolog

if __name__ == '__main__':
    prolog = Prolog()
    prolog.assertz("father(michael,john)")

    # prolog.consult('basic_test.pl')
    # c = list(prolog.query("test(X,Y)"))
    # print(c)
