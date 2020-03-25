# 1070 - Six Odd Numbers
X = int(input())
if (X % 2 == 0):
    for i in range(X+1, X+12, 2):
        print(i)
elif (X % 2 != 0):
    for i in range(X, X+12, 2):
        print(i)
