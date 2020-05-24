# 2950 - The Two Towers
def main():
    from sys import stdin, stdout
    n, x, y = [int(i) for i in stdin.readline().split()]
    result = n / (x + y)
    stdout.write('%.2f\n' % result)

if __name__ == '__main__':
    main()
