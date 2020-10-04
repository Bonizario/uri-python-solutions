def main():
    from sys import stdin, stdout

    n = int(stdin.readline()) - 1
    carlos = int(stdin.readline())
    for _ in range(n):
        random = int(stdin.readline())
        if random > carlos:
            stdout.write('N\n')
            return
    stdout.write('S\n')

main()
