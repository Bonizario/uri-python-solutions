# 2380 - Fusões
def main():
    from sys import stdin, stdout

    def find(x):
        if (x == parent[x]): return x
        parent[x] = find(parent[x])
        return parent[x]


    def join(x, y):
        if x == y: return

        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[x] = y
            rank[y] += 1


    N, B = map(int, stdin.readline().split())
    rank = [0] * (N+1)
    parent = [i for i in range(N+1)]

    for _ in range(B):
        op, bank1, bank2 = stdin.readline().split()
        bank1 = find(int(bank1))
        bank2 = find(int(bank2))
        if op == 'F':
            join(bank1, bank2)
        else:
            if bank1 == bank2:
                stdout.write("S\n")
            else:
                stdout.write("N\n")

main()
