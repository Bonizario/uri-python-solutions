def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    for _ in range(n):
        t = int(stdin.readline())
        if t >= 2015:
            stdout.write('%d A.C.\n' % (t - 2014))
        else:
            stdout.write('%d D.C.\n' % (2015 - t))

main()
