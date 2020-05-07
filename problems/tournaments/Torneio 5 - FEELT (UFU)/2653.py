# 2653 - Dijkstra
jewels = set()

while True:
    try:
        jewels.add(input())
    except EOFError:
        break

print(len(jewels))
