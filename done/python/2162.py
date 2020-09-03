def main():
    from sys import stdin, stdout

    n = int(stdin.readline())
    nums = list(map(int, stdin.readline().split()))

    if n == 2:
        stdout.write('1\n' if nums[0] != nums[1] else '0\n')
        return

    ok = 1
    for i in range(1, n - 1):
        if nums[i - 1] == nums[i] or nums[i] == nums[i + 1]:
            ok = 0
            break
        if (nums[i - 1] < nums[i] > nums[i + 1]) or (nums[i - 1] > nums[i] < nums[i + 1]):
            continue
        ok = 0
        break

    stdout.write('0\n' if not ok else '1\n')

main()
