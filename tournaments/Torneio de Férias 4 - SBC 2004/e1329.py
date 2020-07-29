def main():
    from sys import stdin, stdout
    while True:
        n = int(stdin.readline())
        if not n:
            break
        nums = list(map(int, stdin.readline().split()))
        john = sum(nums)
        mary = len(nums) - john
        print('Mary won {} times and John won {} times'.format(mary, john))
main()
