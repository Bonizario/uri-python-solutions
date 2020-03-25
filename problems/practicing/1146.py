# 1146 - Growing Sequences
X = int(input())
nums_list = ""
while X != 0:
    for i in range(1, X + 1):
        nums_list += str(i)
        nums_list += " "
    nums_list = nums_list.strip(" ")
    print(nums_list)
    nums_list = ""
    X = int(input())
