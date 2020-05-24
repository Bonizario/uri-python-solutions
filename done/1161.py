# 1161 - Factorial Sum
from math import factorial
while True:
    try:
        m, n = map(int, input().split())
        result = factorial(m) + factorial(n)
        print(result)
    except EOFError:
        break
