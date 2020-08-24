def main():
    from sys import stdin, stdout

    qt = int(stdin.readline())
    for _ in range(qt):
        p1, a1, p2, a2 = stdin.readline().split()
        n, m = map(int, stdin.readline().split())
        result = n + m
        if result & 1:
            if a1 == 'IMPAR':
                stdout.write('%s\n' % p1)
            else:
                stdout.write('%s\n' % p2)
        else:
            if a1 == 'PAR':
                stdout.write('%s\n' % p1)
            else:
                stdout.write('%s\n' % p2)

main()
