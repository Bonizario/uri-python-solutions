# 1142 - PUM
def main():
    from sys import stdin, stdout
    N = int(stdin.readline())
    for i in range(1, N + N*3, 4):
        stdout.write("%d %d %d PUM\n" % (i, i+1, i+2))

if __name__ == '__main__':
    main()
