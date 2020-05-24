# 1174 - Array Selection I
A = []
for i in range(100):
    v = float(input())
    A.append(v)
    if v <= 10:
        print('A[{}] = {:.1f}'.format(i, A[i]))
