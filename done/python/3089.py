def main():
    from sys import stdin, stdout

    while True:
        n = int(stdin.readline())
        if not n:
            break

        nums = list(map(int, stdin.readline().split()))
        caro = nums[-1]
        barato = 2 * nums[0]
        j = -1
        for i in range(n):
            par = nums[i] + nums[j]
            if caro < par:
                caro = par
            if barato > par:
                barato = par
            j -= 1

        stdout.write(f'{caro} {barato}\n')

main()
