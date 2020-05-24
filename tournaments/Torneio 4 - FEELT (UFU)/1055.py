# 1055 - Elegant Permuted Sum
from collections import deque

for case in range(1, int(input()) + 1):
    size, *nums = map(int, input().split())
    nums.sort()

    permuted = deque()
    switch = False
    for i in range(size // 2):
        if switch:
            permuted.append(nums[i])
            permuted.appendleft(nums[size-i-1])
        else:
            permuted.append(nums[size-i-1])
            permuted.appendleft(nums[i])
        switch = not switch

    if size % 2 != 0:
        middle = size // 2
        rest_start = abs(permuted[0] - nums[middle])
        rest_end = abs(permuted[size-2] - nums[middle])

        if rest_start > rest_end:
            permuted.appendleft(nums[middle])
        else:
            permuted.append(nums[middle])

    elegant_sum = 0
    for i in range(size - 1):
        elegant_sum += abs(permuted[i] - permuted[i+1])

    print('Case {}: {}'.format(case, elegant_sum))

"""
for case in range( 1,int(input())+1 ):
    size, *nums = map( int,input().split() )
    nums.sort()

    left, right = nums[size//2 + size%2:], nums[:size//2]
    left[::2], right[::-2] = right[::-2], left[::2]

    if size%2:
        if abs( nums[size//2]-left[0] ) > abs( nums[size//2]-right[-1] ):
            nums = [nums[size//2]] + left + right
        else:
            nums = left + right + [nums[size//2]]
    else:
        nums = left + right

    s = 0
    for i in range( size-1 ):
        s += abs( nums[i]-nums[i+1] )

    print( "Case {}: {}".format(case,s) )
"""
