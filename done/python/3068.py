def main():
    from sys import stdin, stdout

    case = 1
    while True:
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        if x1 == y1 == x2 == y2 == 0:
            break
        if x2 < x1:
            x2, x1 = x1, x2
            y2, y1 = y1, y2

        fell_inside_farm = 0
        for _ in range(int(stdin.readline())):
            x, y = map(int, stdin.readline().split())
            if x1 <= x <= x2 and (y1 <= y <= y2 or y2 <= y <= y1):
                fell_inside_farm += 1
        stdout.write(f'Teste {case}\n{fell_inside_farm}\n')
        case += 1

main()
