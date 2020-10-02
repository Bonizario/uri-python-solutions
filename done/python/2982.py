def main():
    from sys import stdin, stdout

    d = {'G': 0, 'V': 0}
    for _ in range(int(stdin.readline())):
        t, cash = stdin.readline().split()
        d[t] += int(cash)
    stdout.write('A greve vai parar.\n' if d['V'] >= d['G'] else 'NAO VAI TER CORTE, VAI TER LUTA!\n')

main()
