def main():
    from sys import stdin, stdout

    while True:
        try:
            a, b, c = map(int, stdin.readline().split())
        except Exception:
            break

        d = {a: 'A', b: 'B', c: 'C'}
        t = a + b + c
        if t == 1:
            stdout.write('%s\n' % d[max(a, b, c)])
        elif t == 2:
            stdout.write('%s\n' % d[min(a, b, c)])
        else:
            stdout.write('*\n')

main()
