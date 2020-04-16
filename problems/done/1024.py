# 1024 - Encryption
def encrypt(message):
    encrypted_message = ''
    for i in range(len(message) - 1, -1, -1):
        c = ord(message[i])
        if (c > 64 and c < 91) or (c > 96 and c < 123): # ascii table for [a-z, A-Z]
            c += 3
        if i < len(message) / 2:
            c -= 1
        encrypted_message += chr(c)
    return encrypted_message


for _ in range(int(input())):
    message = input()
    print(encrypt(message))
