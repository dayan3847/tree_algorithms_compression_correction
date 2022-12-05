if __name__ == '__main__':

    a = 257
    for i in range(10):
        print(f'a: {a} : {a:b}')
        a >>= 1

    b = 1
    for i in range(10):
        # add 1 to the end
        b <<= 1
        b |= 1

        print(b)

    # concatenate 2 bynary numbers
    c = 1
    d = 5
    e = c << d.bit_length() | d
    print(f'e = {e}')

    # # get count of bits in number
    # for i in range(10):
    #     print(f'{i} = {i.bit_length()}')
