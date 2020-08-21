def main():
    from sys import stdin, stdout

    n, m, p = map(int, stdin.readline().split())
    bairros = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, stdin.readline().split())
        bairros[a][b] = 1
        bairros[b][a] = 1

    # Floyd Wharshall
    for k in range(n):
        for i in range(n):
            if bairros[i][k]:
                for j in range(n):
                    bairros[i][j] |= bairros[k][j]

    for _ in range(p):
        a, b = map(lambda x: int(x) - 1, stdin.readline().split())
        if bairros[a][b]:
            stdout.write('Lets que lets\n')
        else:
            stdout.write('Deu ruim\n')

main()
