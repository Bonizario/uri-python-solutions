# 3047 - A idade de Dona Mônica
def main():
    from sys import stdin, stdout
    m = int(stdin.readline())
    a = int(stdin.readline())
    b = int(stdin.readline())
    oldest = max(a, b, m - a - b)
    stdout.write(str(oldest) + '\n')

if __name__ == '__main__':
    main()
