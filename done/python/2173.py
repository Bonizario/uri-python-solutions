'''
Gabriel de Souza Bonizário
--------------------------
URI Online Judge | 2173
Caixa Dois
Por Guilherme Silva, ITA BR Brazil
Timelimit: 2
'''

# Casos testes foram feitos de maneira não inteligente, rs
# Há uma ou mais linhas em branco entre uma entrada e outra
# A descrição do problema não afirma isso já que em C/C++ não faz diferença
# Em Python só é possível ler a linha inteira, como o getline() em C/C++
# O motivo dos Runtime Errors era a leitura de strings vazias no input

def main():
    from sys import stdin, stdout

    G = [0] * 10001
    S = [0] * 10001

    def Find(A):
        if (G[A] == A):
            return A
        G[A] = Find(G[A])
        return G[A]

    def Union(A, B):
        A = Find(A)
        B = Find(B)
        if A == B:
            return 0
        if S[A] < S[B]:
            G[A] = B
            S[B] += S[A]
            return B
        else:
            G[B] = A
            S[A] += S[B]
            return A

    while True:
        while True:
            tmp = stdin.readline().strip()
            if tmp != '':
                n, m = map(int, tmp.split())
                break
        if n == 0 and m == 0:
            break

        for i in range(1, n + 1):
            G[i] = i
            S[i] = 1

        E = []
        while True:
            tmp = stdin.readline().strip()
            if tmp != '':
                E.append(list(map(int, tmp.split())))
            if len(E) == m:
                break

        esq = roubo_min = roubo_max = 0

        E.sort(key=lambda x: x[2])
        for i in range(m):
            esq = Union(E[i][0], E[i][1])
            if esq != 0:
                roubo_min += E[i][2]
                if S[esq] == n:
                    break

        for i in range(1, n + 1):
            G[i] = i
            S[i] = 1

        E.sort(key=lambda x: x[2], reverse=True)
        for i in range(m):
            esq = Union(E[i][0], E[i][1])
            if esq != 0:
                roubo_max += E[i][2]
                if S[esq] == n:
                    break

        stdout.write('%d\n' % (roubo_max - roubo_min))

main()
