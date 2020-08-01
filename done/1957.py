def main():
    from sys import stdin, stdout

    v = int(stdin.readline())
    stdout.write('%s\n' % hex(v).lstrip('0x').upper())

main()
