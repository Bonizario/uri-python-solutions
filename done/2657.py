def main():
    from sys import stdin, stdout

    parser = dict()
    G = [0]*10000
    S = [0]*10000
    skills = [[0, False] for _ in range(10000)]

    def Find(a):
        if G[a] == a:
            return a
        G[a] = Find(G[a])
        return G[a]

    def Union(a, b):
        A = Find(a)
        B = Find(b)
        if A == B:
            return

        if (skills[a][0]>5 or skills[b][0]>5
            or skills[A][1] or skills[B][1]):
            skills[A][1] = True
            skills[B][1] = True

        if S[A] < S[B]:
            G[A] = B
            S[B] += S[A]
        else:
            G[B] = A
            S[A] += S[B]

    n, m, q = map(int, stdin.readline().split())
    for i in range(n):
        name, skill = stdin.readline().split()
        parser[name] = i
        G[i] = i
        S[i] = 1
        skills[i][0] = int(skill)

    for i in range(m):
        p1, p2 = stdin.readline().strip().split()
        Union(parser[p1], parser[p2])

    for i in range(q):
        name = stdin.readline().strip()
        Id = parser[name]
        ParentId = Find(Id)

        if S[ParentId] < 2 or skills[Id][0] >= 5:
            status = True
        elif not skills[ParentId][1] and not skills[ParentId][1]:
            status = True
        else:
            status = False

        stdout.write("S\n" if status else "N\n")

main()
