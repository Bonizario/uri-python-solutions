def main():
    from sys import stdin, stdout

    while True:
        k = int(stdin.readline())
        if k == 0:
            break

        n, m = map(int, stdin.readline().split())
        residencias = [list(map(int, stdin.readline().split())) for _ in range(k)]

        for residencia in residencias:
            if residencia[0] == n or residencia[1] == m:
                stdout.write('divisa\n')
            elif residencia[0] > n and residencia[1] > m:
                stdout.write('NE\n')
            elif residencia[0] < n and residencia[1] > m:
                stdout.write('NO\n')
            elif residencia[0] < n and residencia[1] < m:
                stdout.write('SO\n')
            else:
                stdout.write('SE\n')

main()
