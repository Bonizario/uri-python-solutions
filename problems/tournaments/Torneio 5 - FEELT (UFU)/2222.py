# 2222 - Playing with Sets
for _ in range(int(input())):
    sets = []
    for _ in range(int(input())):
        size, *nums = map(int, input().split())
        nums = set(nums)
        sets.append(tuple((size, nums)))

    for _ in range(int(input())):
        op, X, Y = map(int, input().split())

        # X and Y are tuples: (size, [nums])
        if op == 1:
            result = sets[X-1][1].intersection(sets[Y-1][1])
        else:
            result = sets[X-1][1].union(sets[Y-1][1])

        print(len(result))
