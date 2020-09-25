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
                nums[i], nums[curr] = nums[curr], nums[i]
                swaps += 1 # 2 * curr - 1
            else:
                i += 1
        stdout.write(f'{"Marcelo" if swaps & 1 else "Carlos"}\n')
main()
