#!/usr/bin/python3
# coding: UTF-8

import sys
import codecs
from typing import List


class FrequencyCalculator:
    file_list: List[str]

    def __init__(self, file_list: List[str]):
        self.file_list = file_list
        self.symbols = None

    def count_symbols(self):
        letras = {}
        for fileName in self.file_list:
            archivo = codecs.open(fileName, encoding='utf-8-sig')
            for linea in archivo.readlines():
                for x in linea:
                    if x not in letras:
                        letras[x] = 1
                    else:
                        letras[x] += 1
            archivo.close()
        self.symbols = sorted(letras.items(), key=lambda t: t[1], reverse=True)
        return self.symbols

    def frequency_symbols(self, verbose: bool = False) -> dict[str, float]:
        if self.symbols is None:
            self.count_symbols()
        frequencies: dict[str, float] = {}
        count = 0
        for s in self.symbols:
            count += s[1]
        for s in self.symbols:
            frequencies[str(s[0])] = float(s[1] / count)

        if verbose:
            print("Se encontraron %d simbolos diferentes.\n" % (len(self.symbols)))
            for s in frequencies:
                if ord(s) == 10:
                    print("'\\n',%d,%f" % (ord(s), frequencies[s]))
                else:
                    print("'%c',%d,%f" % (s, ord(s), frequencies[s]))

        return frequencies


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: se debe pasar una lista de rutas a documentos cuyas frecuencias se deban computar.")
        sys.exit(1)

    frequencyCalculator = FrequencyCalculator(sys.argv[1:])
    # symbols = frequencyCalculator.count_symbols()
    frequencyCalculator.frequency_symbols(True)
