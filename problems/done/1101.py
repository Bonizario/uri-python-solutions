# 1101 - Sequence of Numbers and Sum
M, N = map(int, input().split())
sequence = ""
total_sum = 0
while (M > 0) and (N > 0):
    floor = min(M, N)
    top = max(M, N)
    for i in range(floor, top+1):
        if (floor != top):
            sequence = sequence + str(i) + " "
            total_sum += i
        else:
            sequence = sequence + str(i) + " " + str(i) + " "
            total_sum += i * 2
    print("{}Sum={}".format(sequence, total_sum))
    M, N = map(int, input().split())
    total_sum = 0
    sequence = ""
