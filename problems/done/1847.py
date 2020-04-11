# 1847 - Welcome to the Winter!
A, B, C = map(int, input().split())
temp1 = B - A
temp2 = C - B

if (temp1 < 0) and (temp2 >= 0):
    print(':)')
elif (temp1 > 0) and (temp2 <= 0):
    print(':(')
elif (temp1 > 0) and (temp2 > 0) and (temp1 - temp2 > 0):
    print(':(')
elif (temp1 > 0) and (temp2 > 0) and (temp1 - temp2 <= 0):
    print(':)')
elif (temp1 < 0) and (temp2 < 0) and (temp1 - temp2 < 0):
    print(':)')
elif (temp1 < 0) and (temp2 < 0) and (temp1 - temp2 >= 0):
    print(':(')
elif (temp1 == 0) and (temp2 > 0):
    print(':)')
elif (temp1 == 0) and (temp2 <= 0):
    print(':(')
