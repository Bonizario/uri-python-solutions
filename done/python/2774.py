def main():
    from sys import stdin, stdout

    while True:
        try:
            hours, minutes = map(int, stdin.readline().split())
        except Exception:
            break

        qtde = 60 * hours // minutes
        tests = list(map(float, stdin.readline().split()))
        mean = sum(tests) / qtde
        sigma = (sum(map(lambda x: (x - mean) ** 2, tests)) / (qtde - 1)) ** 0.5
        stdout.write(f'{sigma:.5f}\n')

main()
