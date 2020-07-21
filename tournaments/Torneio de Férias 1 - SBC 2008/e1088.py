def main():
    from sys import stdin, stdout

    while True:
        entrada = stdin.readline().strip()
        if entrada == '0':
            break

        n, *nums = tuple(map(int, entrada.split()))
        swaps = i = 0
        while i < n:
            curr = nums[i] - 1
            if curr != i:
                # move nums[i] to the correct index
                nums[i], nums[curr] = nums[curr], nums[i]

                # curr swaps to place num[i] in num[num[i]]
                # curr - 1 swaps to place num[num[i]] in num[i]
                # swaps += 2 * curr - 1
                swaps += 1 # 2 * curr - 1 is always odd, we can just increment by 1
            else:
                i += 1
        stdout.write('%s\n' % ('Marcelo' if swaps & 1 else 'Carlos'))

main()
