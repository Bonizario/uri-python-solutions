def main():
    from sys import stdin, stdout

    while True:
        try:
            h, m = map(int, stdin.readline().split())
        except Exception:
            break
        stdout.write(f'{h // 30:02d}:{m // 6:02d}\n')
main()
