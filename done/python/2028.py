def main():
    from sys import stdin, stdout

    case = 1
    while True:
        try:
            n = int(stdin.readline())
        except Exception:
            break

        sequence = ''
        total = 1 + (n + n * n) // 2
        for i in range(1, n + 1):
            sequence += (' ' + str(i)) * i
        stdout.write(f'Caso {case}: {total} {"numero" if total == 1 else "numeros"}\n')
        stdout.write(f'0{sequence}\n\n')
        case += 1

main()
