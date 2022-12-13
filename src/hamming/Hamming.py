from src.huffman import Code
from src.matrix import BinaryMatrix


class Hamming:
    k: int = 0
    p: int = 0
    n: int = 0
    matrix_g: BinaryMatrix | None = None
    matrix_h: BinaryMatrix | None = None
    matrix_a: BinaryMatrix | None = None
    matrix_at: BinaryMatrix | None = None

    def encode(self, code: Code, verbose: bool = False) -> Code:
        m_code = BinaryMatrix.gen_matrix_from_code(code)
        self.__set_k(code.length)
        self.__gen_g()
        matrix_r = m_code * self.matrix_g
        if verbose:
            print(code)
            print(self.matrix_g)
            print(self.matrix_a)
            print(matrix_r)
        return matrix_r.to_code()

    def decode(self, code: Code, verbose: bool = False) -> Code:
        m_code = BinaryMatrix.gen_matrix_from_code(code)
        self.__set_n(code.length)
        self.__gen_h()
        matrix_ht = self.matrix_h.transpose()
        # TODO inverse matrix
        correction = m_code * matrix_ht
        correction_code = correction.to_code(True)
        index_of_error_bit = correction_code.code
        clone_code = code.clone()
        if index_of_error_bit > self.p:
            clone_code.edit_bit(index_of_error_bit)
        clone_code.extract(self.p)
        if verbose:
            print(clone_code)
            print(self.matrix_h)
            print(self.matrix_at)
            print(correction)
        return clone_code

    def __set_k(self, k: int):
        self.k = k

        self.p = 0
        while 2 ** self.p < self.k + self.p + 1:
            self.p += 1

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
        return self.matrix_g

    def __gen_a(self) -> BinaryMatrix:
        if self.matrix_a is None:
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
        return self.matrix_h
