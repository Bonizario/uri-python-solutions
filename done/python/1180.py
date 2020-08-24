# 1180 - Lowest Number and Position
N = int(input())
v = list(map(int, input().split()))
lowest = v[0]
lowest_position = 0
for i in range(1, len(v)):
    if v[i] < lowest:
        lowest = v[i]
        lowest_position = i
print('Menor valor: {}'.format(lowest))
print('Posicao: {}'.format(lowest_position))

# bubble sort (not fast)
# use with small arrays (n <= 10^4, maybe even less)
# def bubble_sort(N, v):
#     is_sorted = 0
#     while is_sorted == 0:
#         is_sorted = 1
#         for i in range(N - 1):
#             if (v[i] > v[i + 1]):
#                 is_sorted = 0
#                 aux = v[i]
#                 v[i] = v[i + 1]
#                 v[i + 1] = aux
#     return v
