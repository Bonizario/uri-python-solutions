# 1118 - Several Scores with Validation
nums_list = []
new_calculate = 1.0
while new_calculate != 2.0:
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
    print("novo calculo (1-sim 2-nao)")
    new_calculate = float(input())
    while (new_calculate < 1.0) or (new_calculate > 2.0):
        print("novo calculo (1-sim 2-nao)")
        new_calculate = float(input())
    average = 0
    nums_list = []
