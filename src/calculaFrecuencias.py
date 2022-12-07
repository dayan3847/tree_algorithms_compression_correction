#!/usr/bin/python3
# coding: UTF-8

import sys
import codecs


def countSymbols(L):
    letras = {}
    for fileName in L:
        archivo = codecs.open(fileName, encoding='utf-8-sig')
        for linea in archivo.readlines():
            for x in linea:
                if x not in letras:
                    letras[x] = 1
                else:
                    letras[x] += 1
        archivo.close()
        return sorted(letras.items(), key=lambda t: t[1], reverse=True)


if len(sys.argv) < 2:
    print("Error: se debe pasar una lista de rutas a documentos cuyas frecuencias se deban computar.")
    sys.exit(1)

Symbols = countSymbols(sys.argv[1:])
Freq = {}
cont = 0
for i in Symbols:
    cont += i[1]
for i in Symbols:
    Freq[i[0]] = i[1] / cont
print("Se encontraron %d simbolos diferentes.\n" % (len(Symbols)))
for i in Freq:
    if ord(i) == 10:
        print("'\\n',%d,%f" % (ord(i), Freq[i]))
    else:
        print("'%c',%d,%f" % (i, ord(i), Freq[i]))
