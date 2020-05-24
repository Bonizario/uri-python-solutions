# 1564 - Brazil World Cup
def main():
    from sys import stdout

    while True:
        try:
            cup = input()
        except EOFError:
            break

        if cup == '0':
            stdout.write('vai ter copa!\n')
        else:
            stdout.write('vai ter duas!\n')

if __name__ == '__main__':
    main()
