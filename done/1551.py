def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    for _ in range(n):
        letras = {}
        frase = stdin.readline().strip()
        for i in range(len(frase)):
            letra = frase[i]
            if 'a' <= letra <= 'z' and letra not in letras:
                letras[letra] = 0
        tamanho = len(letras)
        if tamanho == 26:
            stdout.write('frase completa\n')
        elif 13 <= tamanho < 26:
            stdout.write('frase quase completa\n')
        else:
            stdout.write('frase mal elaborada\n')
main()
