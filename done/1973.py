def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))
    remaining = sum(nums)
    attacked = dict()  # set 1.128s dict 1.096s o.O

    i = 0
    while True:
        if i < 0 or i == n:
            break
        if i not in attacked:
            attacked[i] = 1
        if nums[i] == 0:
            i -= 1
        else:
            if nums[i] & 1:
                nums[i] -= 1
                i += 1
            else:
                nums[i] -= 1
                i -= 1
            remaining -= 1
    stdout.write('%d %d\n' % (len(attacked), remaining))

main()
