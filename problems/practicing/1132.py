# 1132 - Multiples of 13
X = int(input())
Y = int(input())
not_divisible_by_13 = 0
floor = min(X, Y)
top = max(X, Y)
for i in range(floor, top + 1):
    if (i % 13 != 0):
        not_divisible_by_13 += i
print(not_divisible_by_13)
