# 1606 - The Hints of Ali Baba
while True:
    try:
        K, N = map(int, input().split())
    except EOFError:
        break

    nums = input().split()
    permuted = set()
    result = ''
    size = 0
    for i in range(K):
        num = nums[i]
        if num not in permuted:
            permuted.add(num)
            size += 1
            if size < N:
                result += num+' '
        if size == N:
            result += num
            break

    print(result)
