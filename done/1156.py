# 1156 - S Sequence II
S = 1
i = 3
j = 2
while (i <= 39) and (j <= 524288):
    # print("{} / {}".format(i, j)) Show fractions
    S += i / j
    i += 2
    j *= 2

print("{:.2f}".format(S))
