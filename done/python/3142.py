def main():
    from sys import stdout

    while True:
        try:
            s = input().strip()
            tamanho = len(s)
            if tamanho == 1:
                stdout.write(f'{ord(s[0]) - 64}\n')
            elif tamanho == 2:
                stdout.write(f'{(ord(s[0]) - 64) * 26 + ord(s[1]) - 64}\n')
            elif tamanho == 3 and s <= 'XFD':
                stdout.write(f'{(ord(s[0]) - 64) * 676 + (ord(s[1]) - 64) * 26 + (ord(s[2]) - 64)}\n')
            else:
                stdout.write('Essa coluna nao existe Tobias!\n')
        except:
            break

main()
