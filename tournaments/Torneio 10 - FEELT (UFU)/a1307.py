def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    pair = 1
    for i in range(n):
        x = int(stdin.readline().strip(), 2)
        y = int(stdin.readline().strip(), 2)
        while y != 0:
            x, y = y, x % y
        if x > 1:
            stdout.write('Pair #%d: All you need is love!\n' % pair)
        else:
            stdout.write('Pair #%d: Love is not all you need!\n' % pair)
        pair += 1

main()
