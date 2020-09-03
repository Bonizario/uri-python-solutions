def main():
    from sys import stdin, stdout

    while True:
        try:
            n = int(stdin.readline())
        except Exception:
            break

        stdout.write(f'{n - 1}\n')

main()
