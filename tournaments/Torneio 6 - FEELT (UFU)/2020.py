def main():
    from sys import stdin, stdout

    lista = 1
    n = int(stdin.readline())
    while True:
        linha = list(range(26))
        letras = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        presentes = []

        for _ in range(n):
            nums = list(map(int, stdin.readline().split()))
            presente = ''
            for num in nums:
                if num == 27:
                    presente += ' '
                    continue
                num -= 1
                linha.append(linha.pop(num))
                letras.append(letras.pop(linha[-1]))
                presente += letras[-1]
            presentes.append(presente)

        stdout.write('LISTA #{}:\n'.format(lista))
        lista += 1

        presentes.sort()
        stdout.write('\n'.join(presentes)+'\n')

        try:
            n = int(stdin.readline())
        except Exception:
            break

        stdout.write('\n')


main()
