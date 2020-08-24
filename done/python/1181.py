# 1181 - Line in Array
L = int(input())
T = input()
matrix = []
for _ in range(12):
    matrix.append([float(input()) for _ in range(12)])

line_sum = sum(matrix[L])
if T == 'S':
    print('{:.1f}'.format(line_sum))
else:
    print('{:.1f}'.format(line_sum / 12))
