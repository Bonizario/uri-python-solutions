def main():
    from sys import stdin, stdout

    p, n = map(int, stdin.readline().split())
    alturas = list(map(int, stdin.readline().split()))

    perdeu = False
    for i in range(1, n):
        if abs(alturas[i] - alturas[i - 1]) > p:
            perdeu = True

    stdout.write('%s\n' % ('YOU WIN' if not perdeu else 'GAME OVER'))

main()
