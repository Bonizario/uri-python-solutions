# 1060 Positive Numbers
counter = 0
for _ in range(6):
    number = float(input())
    if number > 0:
        counter += 1
print("{} valores positivos".format(counter))
