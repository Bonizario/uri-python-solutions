# 2783 - Cup Stickers
N, C , M = map(int, input().split())
special_stickers = input().split()
bought_stickers = set(input().split())

missing = 0
for special in special_stickers:
    if special not in bought_stickers:
        missing += 1
print(missing)
