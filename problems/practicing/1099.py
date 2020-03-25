# 1099 - Sum of Consecutive Odd Numbers II
N = int(input())
sum_of_odd_between = 0
for _ in range(N):
    X, Y = map(int, input().split())
    floor = min(X, Y)
    top = max(X, Y)
    if (top == floor) or (top == floor + 1):
        print(0)
    elif (floor % 2 == 0):
        for i in range(floor + 1, top, 2):
            sum_of_odd_between += i
        print(sum_of_odd_between)
        sum_of_odd_between = 0
    elif (floor % 2 != 0) and (top != floor + 2):
        for i in range(floor + 2, top, 2):
            sum_of_odd_between += i
        print(sum_of_odd_between)
        sum_of_odd_between = 0
    elif (floor % 2 != 0) and (top == floor + 2):
        print(0)
