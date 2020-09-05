def main():
    from sys import stdin, stdout

    while True:
        n = int(stdin.readline())
        if n == 0:
            break

        trabalho = 0
        vinhos = list(map(int, stdin.readline().split()))

        for i in range(1, len(vinhos)):
            anterior, atual = vinhos[i - 1], vinhos[i]
            trabalho += anterior * (-1 if anterior < 0 else 1)
            vinhos[i] += anterior
        stdout.write(f'{trabalho}\n')

main()
