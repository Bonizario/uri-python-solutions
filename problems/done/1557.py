# 1557 - Square Matrix III
while True:
    N = int(input()) # 0 <= N <= 15
    if not N:
        break
    spaces = [ # apelei
        ['{:1d}', '{:1d}'],
        ['{:2d}', '{:1d}'],
        ['{:3d}', '{:2d}'],
        ['{:3d}', '{:2d}'],
        ['{:4d}', '{:3d}'],
        ['{:5d}', '{:4d}'],
        ['{:5d}', '{:4d}'],
        ['{:6d}', '{:5d}'],
        ['{:6d}', '{:5d}'],
        ['{:7d}', '{:6d}'],
        ['{:8d}', '{:7d}'],
        ['{:8d}', '{:7d}'],
        ['{:9d}', '{:8d}'],
        ['{:9d}', '{:8d}'],
        ['{:10d}', '{:9d}']
    ]
    if N == 1:
        print(1)
    elif N == 2:
        print('1 2')
        print('2 4')
    else:
        for i in range(N):
            for j in range(N):
                result = 2**(i + j)
                if j == 0:
                    print(spaces[N - 1][1].format(result), end='')
                else:
                    print(spaces[N - 1][0].format(result), end='')
            print()
    print()
