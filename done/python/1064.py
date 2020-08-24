# 1064 - Positives and Average
def positive_and_average_check(array):
    global positives
    global average
    for i in range(len(array)):
        if array[i] > 0:
            positives += 1
            average += array[i]
    average /= positives


positives = 0
average = 0
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
nums_array = [n1, n2, n3, n4, n5, n6]

positive_and_average_check(nums_array)
print("{} valores positivos".format(positives))
print("{:.1f}".format(average))
