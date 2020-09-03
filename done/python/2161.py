def main():
    from sys import stdin, stdout

    aux = 6
    t = int(stdin.readline())
    for _ in range(1, t):
        aux = 6 + 1.0 / aux
    if not t:
        stdout.write('3.0000000000\n')
    else:
        stdout.write(f'{(3 + 1.0 / aux):.10f}\n')

main()
