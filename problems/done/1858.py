# 1858 - Theon's Answer
N = int(input())
persons = list(map(int, input().split()))

lowest_pos = 0
for i in range(N):
    if i == 0:
        lowest = persons[i]
        continue
    if persons[i] < lowest:
        lowest = persons[i]
        lowest_pos = i
print(lowest_pos + 1)
