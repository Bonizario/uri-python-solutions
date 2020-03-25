# 1142 - PUM
def printSequence(initial_value):
    print("{} {} {} PUM".format(initial_value,
                                initial_value + 1, initial_value + 2))


N = int(input())
for i in range(1, N + N * 3, 4):
    printSequence(i)
