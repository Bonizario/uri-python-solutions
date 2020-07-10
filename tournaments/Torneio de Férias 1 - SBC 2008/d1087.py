def main():
    from sys import stdin, stdout

    while True:
        x1, y1, x2, y2 = map(int, stdin.readline().split())
        if x1 == y1 == x2 == y2 == 0:
            break

        # special case
        if x1 == x2 and y1 == y2:
            stdout.write('0\n')
            continue

        diffx = abs(x1 - x2)
        diffy = abs(y1 - y2)
        if diffx == diffy or x1 == x2 or y1 == y2:
            stdout.write('1\n')
        else:
            stdout.write('2\n')
main()
