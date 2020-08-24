def main():
    from sys import stdin, stdout

    n, m, p = map(int, stdin.readline().split())
    bairros = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        bairros[a][b] = 1
        bairros[b][a] = 1

    # Floyd Wharshall
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            # se i eh antecessor de k, i sera antecessor de
            # j somente se k eh antecessor de j
            if bairros[i][k]:
                for j in range(1, n + 1):
                    bairros[i][j] |= bairros[k][j]

    for _ in range(p):
        a, b = map(int, stdin.readline().split())
        if bairros[a][b]:
            stdout.write('Lets que lets\n')
        else:
            stdout.write('Deu ruim\n')

main()
