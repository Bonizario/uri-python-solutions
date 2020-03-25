# 1158 - Sum of Consecutive Odd Numbers III
def sum_consecutive_odd_3(X, Y):
    step = 2
    if (X % 2 == 0):  # increment if X is even
        X += 1  # X must be odd before going to the loop
    if (X % 2 != 0):
        result = X  # result starting value is X (odd number)
        for _ in range(Y - 1):  # Y - 1 to avoid exceeding the limit
            X += step
            result += X
        return result


N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    print(sum_consecutive_odd_3(X, Y))
