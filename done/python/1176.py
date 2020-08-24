# 1176 - Fibonacci Array
# fibonacci using index!
t = int(input())
for _ in range(t):
    n = int(input())
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    print('Fib({}) = {}'.format(n, a))
