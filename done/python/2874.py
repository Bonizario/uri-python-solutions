# 2874 - Binary Phrase
while True:
    try:
        N = int(input())
        binarys = [input() for _ in range(N)]
        message = ''.join([chr(int(binary, 2)) for binary in binarys])
        print(message)
    except EOFError:
        break

'''
    === bin(), hex(), oct(), "{0:b}".format(X) ===

    the second parameter of the int() function is the base
    it can be 2 (binary), 8 (octal), 16 (hexadecimal), [0, 36]
    1010 is the same as 0b1010 (binary)
    12 is the same as 0o12 (octal)
    A is the same as 0xA (hexadecimal)

    === n-bit representation ===

    get_bin = lambda x, n: format(x, 'b').zfill(n)
    print(get_bin(12, 32))
    output:'00000000000000000000000000001100'
'''
