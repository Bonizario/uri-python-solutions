def main():
    from sys import stdin, stdout

    def computeVictories(S, V1, V2):
        i = j = victories = 0
        while True:
            while i < S and V2[i] <= V1[j]:
                i += 1
            if i == S:
                return victories
            victories += 1; i += 1; j += 1

    S = int(stdin.readline())
    V1 = sorted(map(int, stdin.readline().split()))
    V2 = sorted(map(int, stdin.readline().split()))
    victories = computeVictories(S, V1, V2)
    stdout.write('%d\n' % victories)

main()
