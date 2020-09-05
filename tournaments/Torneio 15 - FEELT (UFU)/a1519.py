def main():
    from sys import stdin, stdout
    from collections import defaultdict
    from operator import itemgetter

    while True:
        palavras = stdin.readline().split()
        if palavras[0] == '.':
            break

        d = dict()
        repeticoes = defaultdict(int)
        for palavra in palavras:
            repeticoes[palavra] += 1

        for palavra in palavras:
            letra_atual, tamanho = palavra[0], len(palavra)
            if tamanho <= 2:
                continue
            if letra_atual not in d:
                d[letra_atual] = [palavra, tamanho]
            elif (palavra != d[letra_atual][0]) and ((tamanho - 2) * repeticoes[palavra] > (d[letra_atual][1] - 2) * repeticoes[d[letra_atual][0]]):
                d[letra_atual] = [palavra, tamanho]

        ultima = len(palavras) - 1
        abreviado = ''
        for (i, palavra) in enumerate(palavras):
            letra_atual = palavra[0]
            if letra_atual in d and d[letra_atual][0] == palavra:
                abreviado += letra_atual + ('.' if i == ultima else '. ')
            else:
                abreviado += palavra + ('' if i == ultima else ' ')

        stdout.write(f'{abreviado}\n{len(d)}\n')

        ordenado = sorted(d.items(), key=itemgetter(1))

        for (abrv, tripla) in ordenado:
            stdout.write(f'{abrv}. = {tripla[0]}\n')

main()
