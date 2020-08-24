# 1117 - Score Validation
nums_list = []
counter = 1
while counter < 3:
    n = float(input())
    if (n < 0) or (n > 10):
        print("nota invalida")
    else:
        nums_list.append(n)
        counter += 1
average = (nums_list[0] + nums_list[1]) / 2
print("media = {:.2f}".format(average))
