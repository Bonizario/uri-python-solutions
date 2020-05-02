# 1901 - Butterflies
N = int(input())
forest = []
species = set()

for _ in range(N):
    forest.append([int(num) for num in input().split()])

for _ in range(N * 2):
    x, y = map(lambda x: int(x) - 1, input().split())
    species.add(forest[x][y])

print(len(species))
