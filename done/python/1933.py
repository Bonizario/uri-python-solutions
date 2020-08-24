def main():
    from sys import stdin, stdout

    a, b = map(int, stdin.readline().split())
    if a > b:
        stdout.write('%d\n' % a)
    else:
        stdout.write('%d\n' % b)

main()
