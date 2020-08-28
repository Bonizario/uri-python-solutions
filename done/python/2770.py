def main():
    from sys import stdin, stdout

    while True:
        try:
            x, y, m = map(int, stdin.readline().split())
        except Exception:
            break

        for _ in range(m):
            a, b = map(int, stdin.readline().split())
            if x > y:
                x, y = y, x
            if a > b:
                a, b = b, a
            if a <= x and b <= y:
                stdout.write('Sim\n')
            else:
                stdout.write('Nao\n')

main()
