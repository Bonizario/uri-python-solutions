# 1241 - Fit or Dont Fit II
def main():
    from sys import stdin, stdout
    N = int(stdin.readline())
    for _ in range(N):
        s1, s2 = stdin.readline().rstrip().split()
        if s1[-len(s2):] == s2:
            stdout.write('encaixa\n')
        else:
            stdout.write('nao encaixa\n')

if __name__ == '__main__':
    main()
