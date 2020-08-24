def main():
    from sys import stdin, stdout

    p1_even, p1, p2, p1_cheated, p2_accused = map(int, stdin.readline().split())

    if p1_cheated and p2_accused:
        stdout.write('Jogador 2 ganha!\n')
    elif p1_cheated and not p2_accused:
        stdout.write('Jogador 1 ganha!\n')
    elif not p1_cheated and p2_accused:
        stdout.write('Jogador 1 ganha!\n')
    else:
        if p1_even:
            stdout.write(f'Jogador {2 if (p1 + p2) & 1 else 1} ganha!\n')
        else:
            stdout.write(f'Jogador {1 if (p1 + p2) & 1 else 2} ganha!\n')

main()
