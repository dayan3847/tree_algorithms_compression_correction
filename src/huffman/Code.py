class Code:
    code: int
    length: int

    def __init__(self, code: int = 0, length: int = 0):
        self.code = code
        if length == 0 and code != 0:
            self.length = code.bit_length()
        else:
            self.length = length

    # clone code
    def clone(self) -> 'Code':
        return Code(self.code, self.length)

    # extract the 'length' least significant bits
    def extract(self, length: int) -> 'Code':
        if length >= self.length:
            result = self.clone()
            self.code = 0
            self.length = 0
            return result

        # create a new code with the last length bits
        extra = 1
        for _ in range(length - 1):
            extra <<= 1
            extra |= 1

        result = Code(self.code & extra, length)
        self.code = self.code >> length
        self.length -= length
        return result

    def __str__(self):
        result = f'{self.code:b}'
        if len(result) < self.length:
            result = '0' * (self.length - len(result)) + result
        return result

    # Concatena un cero a la derecha de un número binario
    def concat_zero(self) -> 'Code':
        new_code_code = self.code << 1
        return Code(new_code_code, self.length + 1)

    # Concatena un uno a la derecha de un número binario
    def concat_one(self) -> 'Code':
        new_code_code = self.code << 1 | 1
        return Code(new_code_code, self.length + 1)

    # Concatena un cero a la izquierda de un número binario
    def concat_zero_init(self) -> 'Code':
        return Code(self.code, self.length + 1)

    # Concatena un uno a la izquierda de un número binario
    def concat_one_init(self) -> 'Code':
        new_code_code = 1 << self.length | self.code
        return Code(new_code_code, self.length + 1)

    # def concat(self, other: 'Code') -> 'Code':
    #     new_code_code = self.code << other.length | other.code
    #     return Code(new_code_code, self.length + other.length)

    # Concatena dos números binarios
    def concat_init(self, other: 'Code') -> 'Code':
        new_code_code = other.code << self.length | self.code
        self.code = new_code_code
        self.length += other.length
        return self

    def complete_byte(self) -> 'Code':
        if self.length % 8 == 0:
            return self
        self.length = self.length + 8 - self.length % 8
        return self

    def edit_bit(self, bit_index: int):
        self.code ^= 1 << bit_index

    def __eq__(self, other: 'Code') -> bool:
        return self.code == other.code and self.length == other.length

    # def concat_init(self, other: 'Code') -> 'Code':
    #     new_code_code = other.code << self.length | self.code
    #     return Code(new_code_code, self.length + other.length)

    @staticmethod
    def get_code_from_string(string_code: str):
        code = int(string_code, 2)
        length = len(string_code)
        return Code(code, length)
