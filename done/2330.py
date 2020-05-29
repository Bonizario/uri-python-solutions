# 2330 - Telemarketing (PYTHON PRIORITYQUEUE IMPLEMENTATION)
def main():
    from heapq import heappop, heappush
    from sys import stdin, stdout

    N, L = map(int, stdin.readline().split())
    ligacoes = {i: 0 for i in range(1, N+1)}
    vendedores = [[0, i] for i in range(1, N+1)]

    for i in range(L):
        disponivel = heappop(vendedores)
        disponivel[0] += int(stdin.readline())
        ligacoes[disponivel[1]] += 1
        heappush(vendedores, disponivel)

    stdout.write('\n'.join('{} {}'.format(
        i, ligacoes[i]) for i in ligacoes) + '\n')


main()
