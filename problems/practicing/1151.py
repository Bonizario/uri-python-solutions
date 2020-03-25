# 1151 - Easy Fibonacci
n = int(input())
fib_list = [0, 1]
n = n - 1
for i in range(1, n):
    fib_list.append(fib_list[i] + fib_list[i - 1])

fib_string = ' '.join([str(item) for item in fib_list])
print(fib_string)

# fibonacci using max value
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b
