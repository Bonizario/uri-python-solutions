# 1157 - Divisors I
N = int(input())
i = 1
while i <= N:
    if N % i == 0:
        print(i)
    i += 1
