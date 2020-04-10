# 1145 - Logical Sequence 2
X, Y = map(int, input().split())
counter = 0
nums_list = ""
for i in range(1, Y + 1):
    nums_list += str(i)
    counter += 1
    if counter == X:
        nums_list += "\n"
        counter = 0
    else:
        nums_list += " "
final_list = nums_list.strip("\n")
print(final_list)
