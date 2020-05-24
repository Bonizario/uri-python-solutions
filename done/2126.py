def main():
    case = 1
    while True:
        try:
            substring = input()
            string = input()
        except EOFError:
            break

        print('Caso #{}:'.format(case))

        qtd = string.count(substring)
        last = string.rfind(substring)

        if qtd:
            print('Qtd.Subsequencias: {}'.format(qtd))
            print('Pos: {}'.format(last + 1))
        else:
            print('Nao existe subsequencia')
        case += 1
        print()

main()
