# 1073 - Even Square
N = int(input())
if (N % 2 == 0):
    for i in range(2, N+1, 2):
        print("{}^2 = {}".format(i, i**2))
else:
    for i in range(2, N, 2):
        print("{}^2 = {}".format(i, i**2))
