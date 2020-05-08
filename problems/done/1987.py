# 1987 - Divisibility by 3
def main():
    from sys import stdin, stdout
    while True:
        try:
            size, num = stdin.readline().split()
            size = int(size)

            s = 0
            for i in range(size):
                s += int(num[i])

            if s % 3 == 0:
                stdout.write('%d sim\n' % s)
            else:
                stdout.write('%d nao\n' % s)
        except Exception:
            break

if __name__ == '__main__':
    main()
