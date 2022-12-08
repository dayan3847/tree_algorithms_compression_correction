from typing import List

from src.huffman.Code import Code


class Encode:
    codes: List[Code]

    def __init__(self):
        self.codes = []

    def add_code(self, code: Code) -> None:
        code_cloned = code.clone()
        if 0 == code_cloned.length:
            return
        if 0 == len(self.codes) or 8 == self.codes[0].length:
            first_part: Code = code_cloned.extract(8)
            self.codes.insert(0, first_part)
            return self.add_code(code_cloned)

        rest: int = 8 - self.codes[0].length
        first_part: Code = code_cloned.extract(rest)
        self.codes[0].concat_init(first_part)
        self.add_code(code_cloned)

    def __str__(self):
        result = ''
        for code in self.codes:
            result += str(code)
        return result
