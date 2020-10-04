def main():
    from sys import stdin, stdout
    from collections import defaultdict

    races = defaultdict(int)
    for _ in range(int(stdin.readline())):
        races[stdin.readline().strip()[-1]] += 1

    stdout.write('%d Hobbit(s)\n' % races['X'])
    stdout.write('%d Humano(s)\n' % races['H'])
    stdout.write('%d Elfo(s)\n' % races['E'])
    stdout.write('%d Anao(s)\n' % races['A'])
    stdout.write('%d Mago(s)\n' % races['M'])

main()
