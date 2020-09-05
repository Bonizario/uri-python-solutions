def main():
    from sys import stdin, stdout

    s = int(stdin.readline())
    quadradonia = list(map(int, stdin.readline().split()))
    noglonia = list(map(int, stdin.readline().split()))

    quadradonia.sort()
    noglonia.sort()

    j = vitorias = 0
    for i in range(len(noglonia)):
        if noglonia[i] > quadradonia[j]:
            vitorias += 1
            j += 1
    stdout.write(f'{vitorias}\n')

main()
