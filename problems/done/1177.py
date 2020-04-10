# 1177 - Array Fill II
t = int(input())
i = 0
while i < 1000:
    for j in range(t):
        if i < 1000:
            print('N[{}] = {}'.format(i, j))
            i += 1
        else:
            break
