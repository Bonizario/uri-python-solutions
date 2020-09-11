def main():
    from sys import stdin, stdout

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    for _ in range(int(stdin.readline())):
        p = int(stdin.readline())
        x, y = fib(p), fib(p - 1)
        num_calls = (2 * x - 1) + (2 * y - 1)
        stdout.write(f'fib({p}) = {num_calls} calls = {x}\n')
main()
