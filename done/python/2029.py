def main():
    from sys import stdin, stdout

    while True:
        try:
            v = float(stdin.readline())
            d = float(stdin.readline())
        except Exception:
            break
        area = 3.14 * d * d / 4
        stdout.write(f'ALTURA = {(v / area):.2f}\nAREA = {area:.2f}\n')

main()
