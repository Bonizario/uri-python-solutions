# 1189 - Left Area
operation = input()
matrix = []
for _ in range(12):
    matrix.append([float(input()) for _ in range(12)])

sum_below_sec = 0
for i in range(12):
    for j in range(12):
        if (i > j) and (i + j < 11):
            sum_below_sec += matrix[i][j]

if operation == 'S':
    print('{:.1f}'.format(sum_below_sec))
else:
    print('{:.1f}'.format(sum_below_sec / 30))
