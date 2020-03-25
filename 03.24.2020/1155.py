# 1155 - S Sequence
S = 0
for i in range(1, 101):
    S += 1 / i
print("{:.2f}".format(S))
