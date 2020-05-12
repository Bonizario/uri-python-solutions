# 1249 - Rot13
def main():
    from sys import stdout

    rot13 = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')

    while True:
        try:
            message = input()
        except EOFError:
            break
        message = str.translate(message, rot13)
        stdout.write(message + '\n')

if __name__ == '__main__':
    main()
