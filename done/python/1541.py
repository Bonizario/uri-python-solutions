# 1541 - Building Houses
while True:
    nums = input()
    if nums == '0':
        break
    height, width, percentage = map(int, nums.split())
    desired_area = height * width * 100 / percentage # requires an area 100/percentage bigger
    side = int(desired_area**(0.5))
    print(side)
