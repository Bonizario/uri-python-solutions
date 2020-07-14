def main():
    from sys import stdin, stdout

    while True:
        n, d = map(int, stdin.readline().split())
        if n == 0 and d == 0:
            break

        stack = {}
        nums = stdin.readline().strip()
        top = -1
        erased = 0
        for num in nums:
            while top > -1 and erased < d and num > stack[top]:
                top -= 1
                erased += 1
            if top + 1 < n - d:
                top += 1
                stack[top] = num
        stdout.write('%s\n' % ''.join(stack[i] for i in stack))

main()
