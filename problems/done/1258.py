# 1258 - T-Shirts
mask = {'P': '{0}', 'M': '{1}', 'G': '{2}'}
N = int(input())

while N:
    shirts = []
    for _ in range(N):
        name = input()
        color, size = input().split()

        size = mask[size]
        shirts.append(color + ' ' + size + ' ' + name)

    for shirt in sorted(shirts):
        print(shirt.format('P', 'M', 'G'))

    N = int(input())
    if N:
        print()
