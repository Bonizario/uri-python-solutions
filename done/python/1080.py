# 1080 - Highest and Position
nums_array = []
for i in range(100):
    n = int(input())
    nums_array.append(n)

highest = max(nums_array)
highest_position = nums_array.index(highest) + 1
print(highest)
print(highest_position)
