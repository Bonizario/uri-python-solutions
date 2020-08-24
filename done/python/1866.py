def main():
    from sys import stdin, stdout
    n = int(stdin.readline())
    for _ in range(n):
        m = int(stdin.readline())
        if m & 1:
            stdout.write('1\n')
        else:
            stdout.write('0\n')
main()
