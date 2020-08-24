def main():
    from sys import stdin, stdout

    t1, t2, t3, t4 = map(int, stdin.readline().split())
    stdout.write('%d\n' % (t1 + t2 + t3 + t4 - 3))

main()
