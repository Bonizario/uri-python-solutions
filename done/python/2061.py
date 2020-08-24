# 2061 - As Abas de Péricles
def main():
    from sys import stdin, stdout
    n, m = map(int, stdin.readline().split())
    for _ in range(m):
        action = stdin.readline().rstrip()
        if action == 'fechou':
            n += 1
        else:
            n -= 1
    stdout.write(str(n) + '\n')

main()
