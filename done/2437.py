# 2437 - Manhattan Distance
def main():
    from sys import stdin, stdout
    a, b, c, d = [int(x) for x in stdin.readline().split()]
    manhattan = abs(a-c) + abs(b-d)
    stdout.write('%d\n' % manhattan)
if __name__ == '__main__':
    main()