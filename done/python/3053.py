def main():
    from sys import stdin, stdout

    cups = [0, 0, 0]
    n = int(stdin.readline())
    start = ord(stdin.readline().strip()) - 65
    cups[start] = 1

    for _ in range(n):
        movement = int(stdin.readline())
        if movement == 1:
            cups[0], cups[1] = cups[1], cups[0]
        elif movement == 2:
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]
    stdout.write('%s\n' % chr(cups.index(1) + 65))

main()
