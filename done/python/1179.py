# 1179 - Array Fill IV
even, odd = [], []
for _ in range(15):
    n = int(input())
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
    if len(even) == 5:
        for i in range(5):
            print('par[{}] = {}'.format(i, even[i]))
        even = []
    if len(odd) == 5:
        for i in range(5):
            print('impar[{}] = {}'.format(i, odd[i]))
        odd = []
if len(odd) > 0:
    for i in range(len(odd)):
        print('impar[{}] = {}'.format(i, odd[i]))
if len(even) > 0:
    for i in range(len(even)):
        print('par[{}] = {}'.format(i, even[i]))
