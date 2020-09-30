def main():
    from sys import stdin, stdout

    while True:
        try:
            years = int(stdin.readline())
        except Exception:
            break
        stdout.write(f'{(years // 100 if years % 100 == 0 else years // 100 + 1)}\n')

main()
