def main():
    from sys import stdin, stdout

    while True:
        P, N, C = map(int, stdin.readline().split())
        if P == N == C == 0:
            break

        pontos = [stdin.readline().split() for _ in range(N)]
        palitos = [0]*N

        for j in range(P):
            palito = 0
            continuo = False
            for i in range(N):
                if pontos[i][j] == '1' and not continuo:
                    continuo = True
                    palito += 1
                elif pontos[i][j] == '1' and continuo:
                    palito += 1
                elif pontos[i][j] == '0' and continuo:
                    palitos[palito-1] += 1
                    continuo = False
                    palito = 0
            if palito > 0:
                palitos[palito-1] += 1

        counter = 0
        for i in range(N):
            if palitos[i] >= 0 and i >= C-1:
                counter += palitos[i]
        stdout.write(str(counter)+'\n')


main()
