def main():
    from sys import stdin, stdout
    from math import log

    n = int(stdin.readline())
    P = n / log(n)
    stdout.write(f'{P:.1f} {1.25506 * P:.1f}\n')

main()
