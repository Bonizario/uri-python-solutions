# 3089 - Presentes de Natal
def main():
    from sys import stdin, stdout
    while True:
        n = int(stdin.readline())
        if not n:
            break
        nums = list(map(int, stdin.readline().split()))
        nums.sort()
        caro = 0
        barato = 2 * nums[-1]
        j = -1
        for i in range(n):
            par = nums[i] + nums[j]
            if caro < par:
                caro = par
            if barato > par:
                barato = par
            j -= 1
        stdout.write('%d %d\n' % (caro, barato))

main()
