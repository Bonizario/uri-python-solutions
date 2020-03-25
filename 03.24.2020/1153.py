# 1153 - Simple Factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


N = int(input())
print(factorial(N))

# Math verifies and returns an Traceback error if N is null or negative

# Factorial using math
# from math import factorial
# N = int(input())
# print(factorial(N))


# Factorial using recursion
# def recur_factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n*recur_factorial(n-1)

# N = int(input())
# print(recur_factorial(N))
