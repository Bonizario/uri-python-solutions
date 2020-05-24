# 1837 - Preface
def main():
    from sys import stdin, stdout

    a, b = [int(x) for x in stdin.readline().split()]
    # a = b * q + r
    if a > 0 and b > 0:
        q = a // b
        r = a % b
        stdout.write('%d %d\n' % (q, r))
    elif a > 0 and b < 0:
        q = -(a // abs(b))
        r = a - b * q
        stdout.write('%d %d\n' % (q, r))
    elif a < 0 and b > 0:
        q = a // b
        r = a - b * q
        stdout.write('%d %d\n' % (q, r))
    else:
        b = abs(b)
        q = a // b
        r = a - b * q
        stdout.write('%d %d\n' % (abs(q), abs(r)))

if __name__ == '__main__':
    main()
