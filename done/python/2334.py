def main():
    from sys import stdin, stdout

    while True:
        n = int(stdin.readline())
        if n == -1:
            break
        stdout.write(f'{n - 1 if n > 0 else 0}\n')

main()
