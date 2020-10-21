def main():
    from sys import stdin, stdout
    while True:
        try:
            n = int(stdin.readline())
        except Exception:
            break
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    stdout.write('2')
                elif i == j:
                    stdout.write('1')
                else:
                    stdout.write('3')
            stdout.write('\n')
main()
