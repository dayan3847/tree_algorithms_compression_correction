from src.huffman import Code
from src.matrix import BinaryMatrix


class Hamming:
    k: int = 0
    p: int = 0
    n: int = 0
    additional_parity_bit: int = 1
    matrix_g: BinaryMatrix | None = None
    matrix_h: BinaryMatrix | None = None
    matrix_a: BinaryMatrix | None = None
    matrix_at: BinaryMatrix | None = None
    verbose: bool
    report = True

    def __init__(self, verbose: bool = False):
        self.verbose = verbose

    def encode(self, code: Code) -> Code:
        if self.verbose:
            print(f'Encoding code: {code}')
        m_code = BinaryMatrix.gen_matrix_from_code(code)
        self.__set_k(code.length)
        self.__gen_g()
        matrix_r = (m_code * self.matrix_g).set_name('R')
        encode = matrix_r.to_code()
        if self.verbose:
            print(f'encode: {encode}')
        return encode

    def decode(self, code: Code) -> Code:
        if self.verbose:
            print(f'Decoding code: {code}')
        m_code = BinaryMatrix.gen_matrix_from_code(code)
        self.__set_n(code.length)
        self.__gen_h()
        matrix_ht = self.matrix_h.transpose()
        if self.verbose:
            print(matrix_ht)
        correction = (m_code * matrix_ht).set_name('Correction')
        correction_code = correction.to_code()
        if self.verbose:
            print(correction)

        index_of_error_bit = -1
        if correction_code.code != 0:
            matrix_ht_index = matrix_ht.get_row_index(correction_code)
            if -1 != matrix_ht_index:
                index_of_error_bit = self.n - matrix_ht_index - 1

        if self.verbose:
            print(f'index_of_error_bit: {index_of_error_bit}')

        decoded_code = code.clone()
        if index_of_error_bit >= self.p:
            decoded_code.edit_bit(index_of_error_bit)
        decoded_code.extract(self.p)
        return decoded_code

    def __set_k(self, k: int):
        self.k = k

        self.p = 0
        while 2 ** self.p < self.k + self.p + 1:
            self.p += 1
        self.p += self.additional_parity_bit

        self.n = self.k + self.p

    def __set_n(self, n: int):
        self.n = n

        self.p = 0
        while 2 ** self.p < self.n + 1:
            self.p += 1

        self.k = self.n - self.p

    def __gen_g(self) -> BinaryMatrix:
        if self.matrix_g is None:
            k_identity = BinaryMatrix.identity(self.k)
            self.__gen_a()
            self.matrix_g = k_identity.concatenate(self.matrix_a, 'G')
            if self.verbose:
                # print(self.matrix_a)
                print(self.matrix_g)
        return self.matrix_g

    def __gen_a(self) -> BinaryMatrix:
        if self.matrix_a is None:
            if 8 == self.n and 4 == self.k:
                self.matrix_a = BinaryMatrix.identity(self.k).opposite().set_name('A')
            else:
                self.matrix_a = BinaryMatrix.consecutive(self.k, self.p, 'A')

        return self.matrix_a

    def __gen_at(self) -> BinaryMatrix:
        if self.matrix_at is None:
            self.__gen_a()
            self.matrix_at = self.matrix_a.transpose()
        return self.matrix_at

    def __gen_h(self) -> BinaryMatrix:
        if self.matrix_h is None:
            self.__gen_at()
            p_identity = BinaryMatrix.identity(self.p)
            self.matrix_h = self.matrix_at.concatenate(p_identity, 'H')
            if self.verbose:
                # print(self.matrix_at)
                print(self.matrix_h)
        return self.matrix_h
