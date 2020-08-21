def main():
    from sys import stdin, stdout

    dist = [[0] * 64 for _ in range(64)]
    for i in range(64):
        for j in range(64):
            dist[i][j] = 9999 if i != j else 0

    for i in range(8):
        for j in range(8):
            curr = 8 * i + j
            if i > 1:
                if j > 0:
                    dist[curr][8 * (i - 2) + j - 1] = 1
                if j < 7:
                    dist[curr][8 * (i - 2) + j + 1] = 1
            if i < 6:
                if j > 0:
                    dist[curr][8 * (i + 2) + j - 1] = 1
                if j < 7:
                    dist[curr][8 * (i + 2) + j + 1] = 1
            if j > 1:
                if i > 0:
                    dist[curr][8 * (i - 1) + j - 2] = 1
                if i < 7:
                    dist[curr][8 * (i + 1) + j - 2] = 1
            if j < 6:
                if i > 0:
                    dist[curr][8 * (i - 1) + j + 2] = 1
                if i < 7:
                    dist[curr][8 * (i + 1) + j + 2] = 1

    for k in range(64):
        for i in range(64):
            for j in range(64):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    while True:
        try:
            entry1, entry2 = stdin.readline().split()
            a, pos1, b, pos2 = entry1[0], int(entry1[1]), entry2[0], int(entry2[1])
        except Exception:
            break

        # dist[8 * i1 + j1][8 * i2 + j2]
        moves = dist[8 * (ord(a) - 97) + pos1 - 1][8 * (ord(b) - 97) + pos2 - 1]
        stdout.write(f'To get from {a}{pos1} to {b}{pos2} takes {moves} knight moves.\n')

main()
