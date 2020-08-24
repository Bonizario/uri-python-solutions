# 1534 - Array 123
while True:
    try:
        N = int(input())
        for i in range(N):
            for j in range(N):
                if i + j == N - 1:
                    result = 2
                    print(result, end='')
                    continue
                if i == j:
                    result = 1
                    print(result, end='')
                else:
                    result = 3
                    print(result, end='')
            print()
    except EOFError:
        break
