# 1184 - Below the Main Diagonal
operation = input()
matrix = []
for _ in range(12):
    matrix.append([float(input()) for _ in range(12)])

sum_below = 0
for i in range(12):
    for j in range(12):
        if i > j:
            sum_below += matrix[i][j]

if operation == 'S':
    print('{:.1f}'.format(sum_below))
else:
    print('{:.1f}'.format(sum_below / 66))
