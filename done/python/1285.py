# 1285 - Different Digits
while True:
    try:
        N, M = map(int, input().split())
    except EOFError:
        break

    counter = 0
    for i in range(N, M + 1):
        nums = list(str(i))
        validate = set(nums)
        if len(nums) == len(validate):
            counter += 1
    print(counter)

# while True:
#     try:
#         N, M = map(int, input().split())
#     except EOFError:
#         break
#     result = 0
#     for i in range(N, M + 1):
#         unique = True
#         nums = ''
#         for s in str(i):
#             if s in nums:
#                 unique = False
#                 break
#             else:
#                 nums += s
#         if unique:
#             result += 1
#     print(result)
