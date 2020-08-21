def main():
    from sys import stdin, stdout

    while True:
        try:
            n, m = map(int, stdin.readline().split())
        except Exception:
            break

        dist = [[0] * n for _ in range(n)]
        for _ in range(m):
            a, b, p = map(int, stdin.readline().split())
            a, b, p = a - 1, b - 1, p * 0.01
            dist[a][b] = dist[b][a] = p

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

        print(f'{dist[0][n - 1] * 100:.6f} percent')

main()
