def main():
    from sys import stdin, stdout

    n = int(stdin.readline())

    if n == 0:
        stdout.write('E\n')
    elif 1 <= n <= 35:
        stdout.write('D\n')
    elif 36 <= n <= 60:
        stdout.write('C\n')
    elif 61 <= n <= 85:
        stdout.write('B\n')
    else:
        stdout.write('A\n')

main()
