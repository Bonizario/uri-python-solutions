# 2584 - Pentágono
from math import tan, pi

for _ in range(int(input())):
    N = int(input())
    altura = N / (2 * tan(pi / 5)) # 36° graus
    area = 5 * (N * altura / 2)
    print('{:.3f}'.format(area))
