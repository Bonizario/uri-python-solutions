# 1028 - Collectable Cards
for _ in range(int(input())):
    x, y = map(int, input().split())
    while y != 0:
        x, y = y, x % y # greatest common divisor
    print(x)
