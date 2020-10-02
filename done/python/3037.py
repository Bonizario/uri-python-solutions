def main():
    from sys import stdin, stdout

    for _ in range(int(stdin.readline())):
        joao = maria = 0
        for _ in range(3):
            x, d = map(int, stdin.readline().split())
            joao += x * d
        for _ in range(3):
            x, d = map(int, stdin.readline().split())
            maria += x * d
        stdout.write('JOAO\n' if joao > maria else 'MARIA\n')
main()
