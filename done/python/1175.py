# 1175 - Array change I
N = [int(input()) for _ in range(20)]
for i in range(20):
    print('N[{}] = {}'.format(i, N[19 - i]))
