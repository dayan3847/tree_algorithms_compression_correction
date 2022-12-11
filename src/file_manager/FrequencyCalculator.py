#!/usr/bin/python3
# coding: UTF-8

import sys
import codecs
from typing import List


class FrequencyCalculator:
    file_list: List[str]
    # symbols: List[tuple[str, int]] = []
    frequencies: dict[str, float]

    def __init__(self, file_list: List[str]):
        self.file_list = file_list
        self.symbols = None
        self.frequencies: dict[str, float] = {}

    def count_symbols(self):
        if self.symbols is not None and len(self.symbols) > 0:
            return self.symbols
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
        if len(self.frequencies) > 0:
            return self.frequencies
        self.count_symbols()
        self.frequencies: dict[str, float] = {}
        count = 0
        for s in self.symbols:
            count += s[1]
        for s in self.symbols:
            self.frequencies[str(s[0])] = float(s[1] / count)

        if verbose:
            print("Se encontraron %d simbolos diferentes.\n" % (len(self.symbols)))
            for s in self.frequencies:
                if ord(s) == 10:
                    print("'\\n',%d,%f" % (ord(s), self.frequencies[s]))
                else:
                    print("'%c',%d,%f" % (s, ord(s), self.frequencies[s]))

        return self.frequencies

    def export_json_frequency(self) -> str:
        self.frequency_symbols()
        json = "{"
        for s in self.frequencies:
            key = self.symbol_to_export(s)
            json += "\n\t\"%s\": %f," % (key, self.frequencies[s])
        json = json[:-1]
        json += "\n}"

        return json

    def import_json_frequency(self, json: str) -> dict[str, float]:
        self.frequencies: dict[str, float] = {}
        json = json[1:-1]
        json = json.replace("\n", "")
        json = json.replace("\t", "")
        json = json.replace("\"", "")
        for s in json.split(','):
            s = s.split(':')
            key = str(s[0])
            # key = key[2:-1]
            key = self.symbol_to_import(key)
            value = float(s[1])
            self.frequencies[key] = value
        return self.frequencies

    @staticmethod
    def symbol_to_import(s: str) -> str:
        if s == '$double_quote':
            return '\"'
        elif s == '$new_line':
            return '\n'
        elif s == '$tab':
            return '\t'
        return s

    @staticmethod
    def symbol_to_export(s: str) -> str:
        if s == '\"':
            return '$double_quote'
        elif s == '\n':
            return '$new_line'
        elif s == '\t':
            return '$tab'
        return s


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error: se debe pasar una lista de rutas a documentos cuyas frecuencias se deban computar.")
        sys.exit(1)

    frequencyCalculator = FrequencyCalculator(sys.argv[1:])
    # symbols = frequencyCalculator.count_symbols()
    frequencyCalculator.frequency_symbols(True)
