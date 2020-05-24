# 1164 - Perfect Number
n = int(input())
for _ in range(n):
    perfect = 0
    x = int(input())
    for i in range(1, x):
        if (x % i == 0):
            perfect += i
    if x == perfect:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))

# O conjunto dos números perfeitos é:
# {6, 28, 496, 8128, 33550336, 8589869056, …}

# MACETE :D (input < 10^8)
# perfects = [6, 28, 496, 8128, 33550336]
# n = int(input())
# for _ in range(n):
#     x = int(input())
#     if x in perfects:
#         print('{} eh perfeito'.format(x))
#     else:
#         print('{} nao eh perfeito'.format(x))
