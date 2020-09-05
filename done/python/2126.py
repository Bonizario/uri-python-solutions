def main():
    from sys import stdout

    case = 1
    while True:
        try:
            substring = input()
            string = input()
        except Exception:
            break

        stdout.write(f'Caso #{case}:\n')

        qtd = string.count(substring)
        last = string.rfind(substring)

        if qtd:
            stdout.write(f'Qtd.Subsequencias: {qtd}\n')
            stdout.write(f'Pos: {last + 1}\n\n')
        else:
            stdout.write('Nao existe subsequencia\n\n')
        case += 1

main()
