# 1478 - Square Matrix II
while True:
    N = int(input())
    if not N:
        break

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            result = abs(i - j) + 1
            if j != 1:
                print('{:4d}'.format(result), end='')
            else:
                print('{:3d}'.format(result), end='')
        print()
    print()
