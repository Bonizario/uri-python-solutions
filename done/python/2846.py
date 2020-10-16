def main():
    from sys import stdin, stdout

    ans = 3
    k = int(stdin.readline())
    fib = set((1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, \
                1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393))
    while k:
        ans += 1
        if ans not in fib:
            k -= 1
    stdout.write(f'{ans}\n')

main()
