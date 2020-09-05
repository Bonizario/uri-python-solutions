def main():
    from sys import stdin, stdout

    a, b = map(int, stdin.readline().split())
    stdout.write(f'{((a + b) * (b - a + 1) / 2.0):.0f}\n')

main()
