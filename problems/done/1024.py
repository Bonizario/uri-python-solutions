# 1024 - Encryption
# -*- coding: utf-8 -*-
def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        message = stdin.readline().rstrip()
        encrypted_message = ''
        for i in range(len(message) - 1, -1, -1):
            c = ord(message[i])
            if (c > 64 and c < 91) or (c > 96 and c < 123):
                c += 3
            if i < len(message) / 2:
                c -= 1
            encrypted_message += chr(c)
        stdout.write('%s\n' % encrypted_message)
if __name__ == '__main__':
    main()
