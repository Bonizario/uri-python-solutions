# 1618 - Colision
def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        ax, ay, bx, by, cx, cy, dx, dy, rx, ry = [int(x) for x in stdin.readline().split()]
        if (rx >= ax) and (rx <= bx) and (ry >= ay) and (ry <= dy):
            stdout.write('1\n')
        else:
            stdout.write('0\n')
if __name__ == '__main__':
    main()
