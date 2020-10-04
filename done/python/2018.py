def main():
    from sys import stdin, stdout
    from operator import itemgetter

    stdout.write('Quadro de Medalhas\n')
    medals = dict()
    while True:
        try:
            _ = input()
        except EOFError:
            break

        first = input()
        second = input()
        third = input()

        if first not in medals:
            medals[first] = [-1, 0, 0]
        else:
            medals[first][0] -= 1

        if second not in medals:
            medals[second] = [0, -1, 0]
        else:
            medals[second][1] -= 1

        if third not in medals:
            medals[third] = [0, 0, -1]
        else:
            medals[third][2] -= 1

    medals = sorted(medals.items(), key=lambda country: (country[1], country[0]))

    for country in medals:
        stdout.write('{} {} {} {}\n'.format(country[0], *map(lambda m: -1 * m, country[1])))

main()
