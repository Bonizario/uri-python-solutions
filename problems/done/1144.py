# 1144 - Logical Sequence
def main():
    from sys import stdin, stdout

    for i in range(1, int(stdin.readline()) + 1):
        stdout.write('%d %d %d\n' % (i, i*i, i*i*i))
        stdout.write('%d %d %d\n' % (i, i*i + 1, i*i*i + 1))

if __name__ == '__main__':
    main()
