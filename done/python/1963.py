def main():
    from sys import stdin, stdout

    a, b = map(float, stdin.readline().split())
    stdout.write('%.2f%%\n' % (b * 100 / a - 100))

main()
