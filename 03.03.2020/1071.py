# 1071 - Sum of Consecutive Odd Numbers I
Y = int(input())
X = int(input())
sum_of_odd_values = 0

if (X == Y):
    print(0)
else:
    for i in range(X + 1, Y):
        if (i % 2 != 0):
            sum_of_odd_values += i
    print(sum_of_odd_values)
