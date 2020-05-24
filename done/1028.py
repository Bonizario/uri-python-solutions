# 1028 - Collectable Cards
def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    for _ in range(n):
        x, y = [int(x) for x in stdin.readline().split()]
        while y != 0:
            x, y = y, x % y # greatest common divisor
        stdout.write('%d\n' % x)

if __name__ == '__main__':
    main()
