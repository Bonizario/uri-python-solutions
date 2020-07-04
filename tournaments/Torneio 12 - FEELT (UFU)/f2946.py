def main():
    from sys import stdin, stdout

    n = int(stdin.readline(), 2)
    m = int(stdin.readline())
    nums = [int(stdin.readline()) for _ in range(m)]
    nums.sort()

    ans = [i for i in nums if n % i == 0]

    if len(ans) != 0:
        stdout.write(' '.join(str(a) for a in ans) + '\n')
    else:
        stdout.write('Nenhum\n')

main()
