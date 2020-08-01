def main():
    from sys import stdin, stdout

    t = int(stdin.readline())
    especiais = {'a','A','4','e','E','3','i','I','1','o','O','0','s','S','5'}
    for _ in range(t):
        senha = stdin.readline().strip()
        variacoes = 1
        for i in range(len(senha)):
            if senha[i] in especiais:
                variacoes *= 3
            else:
                variacoes *= 2
        stdout.write('%d\n' % variacoes)
main()
