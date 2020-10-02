def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        h, d, b = map(int, stdin.readline().split())
        if 200 <= h <= 300 and 50 <= d and 150 <= b:
            stdout.write('Sim\n')
        else:
            stdout.write('Nao\n')
main()
