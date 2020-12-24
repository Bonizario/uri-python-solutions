def main():
    adj = [[] for _ in range(101)]
    component = [-1] * 101

    def dfs(node):
        for i in range(len(adj[node])):
            v = adj[node][i]
            if component[v] == -1:
                component[v] = component[node]
                dfs(v)

    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    connections = 0
    for i in range(1, n + 1):
        if component[i] == -1:
            connections += 1
            component[i] = connections
            dfs(i)
    print('COMPLETO' if connections == 1 else 'INCOMPLETO')

main()


'''
def main():
    G = [0] * 101
    S = [1] * 101

    def Find(A):
        if A == G[A]:
            return A
        G[A] = Find(G[A])
        return G[A]

    def Union(A, B):
        A, B = Find(A), Find(B)
        if S[A] > S[B]:
            G[B] = A
            S[A] += 1
        else:
            G[A] = B
            S[B] += 1

    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        Union(a, b)
    ok = set()
    for i in range(1, n + 1):
        print(G[i])
        ok.add(G[i])
    print('COMPLETO' if len(ok) == 1 else 'INCOMPLETO')

main()
'''
