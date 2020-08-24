def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        p1 = stdin.readline().strip()
        p2 = stdin.readline().strip()
        if 'ataque' in (p1, p2):
            if p1 == 'ataque':
                if p2 == 'ataque':
                    stdout.write('Aniquilacao mutua\n')
                else:
                    stdout.write('Jogador 1 venceu\n')
            else:
                stdout.write('Jogador 2 venceu\n')
        elif 'pedra' in (p1, p2):
            if p1 == 'pedra':
                if p2 == 'pedra':
                    stdout.write('Sem ganhador\n')
                else:
                    stdout.write('Jogador 1 venceu\n')
            else:
                stdout.write('Jogador 2 venceu\n')
        else:
            stdout.write('Ambos venceram\n')

main()
