def main():
    from sys import stdin, stdout

    tabela = {
        'suco de laranja': 120,
        'morango fresco': 85,
        'mamao': 85,
        'goiaba vermelha': 70,
        'manga': 56,
        'laranja': 50,
        'brocolis': 34
    }

    while True:
        t = int(stdin.readline())
        if t == 0:
            break

        consumo = [stdin.readline().strip().split(' ', 1) for _ in range(t)]
        vitamina_c = sum(int(consumo[i][0]) * tabela[consumo[i][1]] for i in range(t))
        if vitamina_c < 110:
            stdout.write(f'Mais {110 - vitamina_c} mg\n')
        elif vitamina_c > 130:
            stdout.write(f'Menos {vitamina_c - 130} mg\n')
        else:
            stdout.write(f'{vitamina_c} mg\n')

main()
