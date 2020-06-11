int gcd(int x, int y) {
    return (y == 0 ? x : gcd(y, x % y));
}

// PYTHON 3
/*
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x
*/

/* mdc from n numbers
def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    x = nums[0]
    for i in range(n-1):
        y = nums[i+1]
        while y != 0:
            x, y = y, x % y
    stdout.write('%d\n' % x)
main()
*/

/* a/b + c/d algorithm
def main():
    from sys import stdin, stdout

    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    a, b, c, d = map(int, stdin.readline().split())
    denominador = b*d // gcd(b, d)
    a *= denominador//b
    c *= denominador//d
    numerador = a + c
    mdc = gcd(numerador, denominador)
    stdout.write('%d %d\n' % (numerador//mdc, denominador//mdc))
main()
*/
