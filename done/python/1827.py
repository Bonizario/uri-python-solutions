def main():
    from sys import stdin, stdout

    while True:
        try:
            n = int(stdin.readline())
        except Exception:
            break

        m = [['0' for _ in range(n)] for _ in range(n)]

        for i in range(n):  # diagonals
            m[i][i] = '2'
        for i in range(n):
            m[i][n - 1 - i] = '3'

        for i in range(n // 3, n - n // 3):  # matriz 1
            for j in range(n // 3, n - n // 3):
                m[i][j] = '1'

        m[n // 2][n // 2] = '4'  # matriz 4

        for i in range(n):
            stdout.write('%s\n' % ''.join(m[i]))
        stdout.write('\n')

main()
