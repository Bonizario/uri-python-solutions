# 1159 - Sum of Consecutive Even Numbers
x = int(input())
while x != 0:
    soma = 0
    if x % 2 == 0:
        for i in range(x, x + 9, 2):
            soma += i
    else:
        for i in range(x + 1, x + 10, 2):
            soma += i
    print(soma)
    x = int(input())
