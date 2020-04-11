# 1435 - Square Matrix I
while True:
    N = int(input())
    if not N:
        break

    for i in range(N):
        print('  ', end='')
        for j in range(N):
            a = min(i + 1, N - i) # i + 1 for lines before middle, N - i for lines after
            b = min(j + 1, N - j) # j + 1 for columns before middle, N - j for columns after
            result = min(a, b)
            if j:
                print('{:4d}'.format(result), end='')
            else:
                print('{:1d}'.format(result), end='')
        print()
    print()
