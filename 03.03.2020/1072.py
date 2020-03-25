# 1072 - Interval 2
interval = range(10, 21)
numbers_in_interval = 0
N = int(input())
for _ in range(N):
    X = int(input())
    if (X in interval):
        numbers_in_interval += 1

print("{} in".format(numbers_in_interval))
print("{} out".format(N - numbers_in_interval))
