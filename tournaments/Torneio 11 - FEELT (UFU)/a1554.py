def main():
    from sys import stdin, stdout
    from math import sqrt

    for _ in range(int(stdin.readline())):
        N = int(stdin.readline())
        bolas = [list(map(int, stdin.readline().split())) for _ in range(N + 1)]

        primeira = bolas.pop(0)
        a = primeira[0]
        b = primeira[1]

        dists = []
        for i in range(N):
            x = bolas[i][0] - a
            y = bolas[i][1] - b
            result = sqrt(x*x + y*y)
            dists.append([result, i])

        dists.sort(key=lambda k: (k[0], k[1]))
        stdout.write('%d\n' % (dists[0][1] + 1))

main()
