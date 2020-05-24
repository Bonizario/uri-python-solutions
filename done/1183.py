# 1183 - Above the Main Diagonal
operation = input()
matrix = []
for _ in range(12):
    matrix.append([float(input()) for _ in range(12)])

sum_above = 0
for i in range(12):
    for j in range(12):
        if j > i:
            sum_above += matrix[i][j]

if operation == 'S':
    print('{:.1f}'.format(sum_above))
else:
    print('{:.1f}'.format(sum_above / 66))
