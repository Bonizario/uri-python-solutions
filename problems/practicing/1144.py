# 1144 - Logical Sequence
def printSequence(initial_number):
    print("{} {} {}".format(initial_number,
                            initial_number ** 2, initial_number ** 3))
    print("{} {} {}".format(initial_number,
                            initial_number ** 2 + 1, initial_number ** 3 + 1))


N = int(input())
for i in range(1, N + 1):
    printSequence(i)
